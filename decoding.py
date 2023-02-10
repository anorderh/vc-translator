from queue import Queue
from threading import Thread
import numpy as np
import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS


class Decoder:
    def __init__(self, model):
        self.states = {"recording": False, "processing": False}
        self.model = model

        self.bytes = Queue()
        self.transcriptions = []
        self.id = 1

        self.original = self.translated = self.output_lang = self.input_lang = None

    def start_recording(self, input_lang, output_lang):
        """
        Record and transcribe audio. Processes per SpeechRecognizer segment.
        :param input_lang:
        :param output_lang:
        :return:
        """
        self.states["recording"] = True

        self.input_lang = input_lang
        self.output_lang = output_lang

        record = Thread(target=self.record_microphone)
        record.start()  # Start recording

        transcribe = Thread(target=self.realtime_transcribe)
        transcribe.start()  # Start transcribing

    def record_microphone(self):
        r = sr.Recognizer()
        # Speech Recognizer settings
        r.non_speaking_duration = 0.1
        r.pause_threshold = 0.3
        r.energy_threshold = 300

        with sr.Microphone(sample_rate=16000) as source:
            while self.states["recording"]:  # Recording
                self.states["processing"] = True  # Processing started

                audio = r.listen(source)  # Blocking until 'pause_threshold' met
                self.bytes.put(audio.get_raw_data())

    def realtime_transcribe(self):
        while any(self.states.values()):  # If either recording or processing ongoing
            if not self.bytes.empty():  # Skip if no bytes queued
                frames = self.bytes.get()

                # Translating np.array holding bytes into Tensor, per OpenAI Whisper formatting
                # https://github.com/openai/whisper/discussions/450
                np_audio = (np.frombuffer(frames, np.int16).flatten().astype(np.float32) / 32768.0)

                result = self.model.transcribe(np_audio, language=self.input_lang)
                self.transcriptions.append(result["text"])

                # Debug printing
                # print(result["text"])  # Print each excerpt separately
                # print(" ".join(manager.transcription))      # Print each excerpt together

                self.states["processing"] = False  # Processing ended

    def stop_recording(self):
        """
        Stop recording, translate whole transcription, and generate speech.
        :return:
        """
        self.states["recording"] = False  # "OFF"
        while self.states["processing"]:  # Waiting for transcription to complete
            pass

        self.original = " ".join(self.transcriptions)[1:]   # Remove extra space on end
        self.translate(self.original)
        return self.generateSpeech()    # Returning file name

    def translate(self, text):
        self.translated = GoogleTranslator(source=self.input_lang, target=self.output_lang).translate(text)

    def generateSpeech(self):
        tts = gTTS(self.translated, lang=self.output_lang)

        # Generate file w/ unique ID
        identifier = "recordings/" + str(self.id) + ".mp3"
        tts.save(identifier)
        self.id += 1

        return identifier

    def reset(self):
        self.transcriptions = []
        self.original = self.translated = self.output_lang = self.input_lang = None
