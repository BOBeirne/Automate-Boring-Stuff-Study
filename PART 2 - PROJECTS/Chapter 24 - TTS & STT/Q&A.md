# Practice Questions

## 1  How can you make pyttsx3’s voice speak faster?

```python
import pyttsx3 as tts
engine = tts.init()
engine.setProperty('rate', 300) # set speech here
``` 
to set the speech speed to 300 words per minute, default i 200

## 2 What audio format does pyttsx3 save to?

Wav files 

## 3.  Do pyttsx3 and Whisper rely on online services?

pyttsx3: fully offline, relies on system's TTS engine
Whisper: you need to first download the trained model, once it's downloaded it can be run locally

## 4.  Do pyttsx3 and Whisper support other languages besides English?

Yes with caveats:

for pyttsx3 you need to download the language pack for os
for Whisper all models currently provided by whisper except turbo have option to translate 99 languages

## 5.  What is the name of Whisper’s default machine learning model for speech recognition?

There are few to choose from, there is no default.

- `tiny` - **Very fast, low resource**. work well on clear audio with little noise.
- `base` - general purpose transcription on **limited hardware, slightly better accuracy** than `tiny`
- `small` - **everyday choice of balance** between accuracy and speed
- `medium` - focused on **high accuracy** with accents and long speech, **sacrifices on speed**
- `large` - **highest accuracy but slowest**, **requires a powerful machine** to run on. mostly **use for offline batch** jobs.
- `turbo` - high speed with good accuracy, near real-time transcription, **NOT trained for translations**. Use other models if translating.

## 6.  What are two common subtitle text file formats?

SRT and VTT

## 7.  Can yt-dlp download videos from websites besides YouTube?

yes, https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md