# ![voicebridge logo](assets/voicebridge.png)

*A speech-to-speech translation desktop app powered by Whisper and Google Translate*

![GitHub last commit](https://img.shields.io/github/last-commit/anorderh/voice-bridge)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/anorderh/voice-bridge)
![GitHub contributors](https://img.shields.io/github/contributors/anorderh/voice-bridge)
![GitHub](https://img.shields.io/github/license/anorderh/voice-bridge)

![video](assets/demo.mp4)

## Goal

This repo's goal was to develop an appliction testing Whisper's capabilities for real-time voice transcription. Implementing python package `speech_recognition` made this possible by processing audio input per lingual pauses.

## Features

1. Record and efficiently transcribe, translate, and synthesize speech for CPU-dependent hardware between <u>85 different languages.</u>



2. Save up to <u>7 different recordings</u> at a time.



## Usage

1. Run the executable `voicebridge`.
2. Select your *input* and *output* languages.
3. Press REC to start recording.
4. Press again to stop recording.
5. Press PLAY to play the current recording.
6. Press SAVE to turn saving *ON*.
   1. When enabled, press presets 1-6 to store the current recording there.
7. Press presets 1-6 when saving is *OFF* to play the saved recording.

## Requirements

- [OpenAI Whisper (Open-vino)](https://github.com/zhuzilin/whisper-openvino)
- deep_translator
- [speech_recognition](https://github.com/Uberi/speech_recognition)
- gTTs
- tkinter

## Educational

    This application utilizes multithreading to simutaneously record and transcribe audio. The front-end is implemented using Python package [tkinter](https://github.com/TomSchimansky/CustomTkinter). Object-orientated design is demonstrated via `Base` and `Decoder` objects. The app has integration with Google Translate APIs and invokes offline package `openai-whisper`.

## Limitations

Voicebridge requires an internet connection due to Google API use.

- To implement offline functionality, look into [Argos Translate](https://github.com/argosopentech/argos-translate) and [pyttsx3](https://github.com/nateshmbhat/pyttsx3)

## Extensions

- This software could be paired with voicechat applications to enable real-time translation and speech synthesis between users who speak different languages.

- This software could be deployed on small devices for people to use when traveling overseas.
  
  - Extra helpful if offline functionality is implemented

## Contributing

Pull requests are welcomed. For major changes, please open an issue first to discuss what you would like to change. 
