# pyttsx3

- `py` for Python, `tts` from text-to-speech, `x` from extended from pytts package, `3` for Python v3
- Text-to-Speech Engine module using native OS built-in TTS engine and is run locally
  - Windows: Microsoft Speech API (SAPI5)
  - macOS: NSSpeechSynthesizer
  - Linux: eSpeak (may need espeak installed first - `sudo apt install espeak`)
- Install using `pip install pyttsx3`
- import using `import pyttsx3`


## pyttsx3 engine issue

- I (BOBeirne) have encountered an issue when running the exercise code with pyttsx3 on windows 11
- It looks like the **pyttx will not release the engine properly and requires a function wrapper** if TTS is to speak on more than one occasion during program.
- This seems to be a **well known behavior causing issues for years.**

The workaround wrapper code:

```python
import pyttsx3

def speak(text):
	engine = pyttsx3.init() # initialise the engine
	engine.say(text) # queue the speech text
	engine.startLoop(False) # Start event loop in non-blocking mode
                            # False = don't block, let us control iteration
                            # True = would block like runAndWait() - runAndWait() does steps 3-7 internally, but doesn't clean up properly between calls
	engine.iterate() # start the speech
	while engine.isBusy(): # while audio is playing...
		engine.iterate()	# process the events until it finishes
	engine.endLoop() # clean up the event loop
```

## say()

- To generate speech simply use those 3 steps:
  - initialize the engine: `engine = pyttsx3.init()`
  - call `.say()` function: `engine.say('TTS text here')`
  - `engine.runAndWait()`  Waits until the computer finishes speaking.
- Check `hello_tts.py` in `Programs` folder

## getProperty()

- You can control a computer voice by passing strings like `rate` `volume` and `voices` to the `getProperty()` method

```python
import pyttsx3 as tts

engine = tts.init()
engine.getProperty('volume') # volume level, where 1.0 = 100% volume
# 1.0
engine.getProperty('rate') # words per minute
# 200
engine.getProperty('voices')
# [<pyttsx3.voice.Voice object at 0x00000161B171FCB0>, <pyttsx3.voice.Voice object at 0x00000161B1762710>]
for voice in engine.getProperty('voices'): # list all the available voices
	print(voice.name, voice.gender, voice.age, voice.languages)
# Microsoft Hazel Desktop - English (Great Britain) Female Adult ['en-GB']
# Microsoft Zira Desktop - English (United States) Female Adult ['en-US']
```

## setProperty()

- You can change the properties of the voices

```python
import pyttsx3 as tts

engine = tts.init()
engine.setProperty('rate', 100)
engine.setProperty('volume', 0.5)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('The quick brown fox jumps over the yellow lazy dog.')
engine.runAndWait()
```

## save_to_file()

- You can save speech output to a WAV file (`.wav`)
- You will not hear the output of the generated file
- it does not support other audio formats

```python
import pyttsx3 as tts

engine = tts.init()
engine.save_to_file('Hello. How are you doing?', 'hello.wav')
engine.runAndWait()
```