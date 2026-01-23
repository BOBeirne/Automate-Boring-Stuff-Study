# Speech Recognition

- **Pre-requisite**: [FFmpeg](https://ffmpeg.org/download.html)
  - Install using `winget install ffmpeg` on Windows
- [OpenAI API Docs](https://platform.openai.com/docs/guides/speech-to-text)
- [GitHub](https://github.com/openai/whisper)

- Models **made by OpenAI**
- **install** using `pip install openai-whisper`
- the **first time you call** the `load_model()` **it will download** the speech recognition **model** which can be quite large and takes a while
- **Supports** all formats that `ffmpeg` can:
  - **Audio**: mp3, wav, flac, ogg, m4a, aac, wma, opus, webm
  - **Video** (extracts audio track): mp4, mkv, avi, mov, webm
- By default, Whisper uses your CPU but you can set it up for GPU use. e.g. for NVIDIA use `device='cuda'` ad an optional argument
  - `whisper.load_model('base', device='cuda')`

## Models

| Size   | Parameters | English-only model | Multilingual model | Required VRAM | Relative speed |
| ------ | ---------- | ------------------ | ------------------ | ------------- | -------------- |
| `tiny`   | 39 M       | tiny.en            | tiny               | ~1 GB         | ~10×           |
| `base`   | 74 M       | base.en            | base               | ~1 GB         | ~7×            |
| `small`  | 244 M      | small.en           | small              | ~2 GB         | ~4×            |
| `medium` | 769 M      | medium.en          | medium             | ~5 GB         | ~2×            |
| `large`  | 1550 M     | N/A                | large              | ~10 GB        | 1×             |
| `turbo`  | 809 M      | N/A                | turbo              | ~6 GB         | ~8×            |

- `tiny` - **Very fast, low resource**. work well on clear audio with little noise.
- `base` - general purpose transcription on **limited hardware, slightly better accuracy** than `tiny`
- `small` - **everyday choice of balance** between accuracy and speed
- `medium` - focused on **high accuracy** with accents and long speech, **sacrifices on speed**
- `large` - **highest accuracy but slowest**, **requires a powerful machine** to run on. mostly **use for offline batch** jobs.
- `turbo` - high speed with good accuracy, near real-time transcription, **NOT trained for translations**. Use other models if translating.

## transcribe()

- `whisper.load_model()` can be any of the optional models listed, it returns a `mode.Whisper` object
- call `.transcribe()` method and pass it a file name to transcribe
  - You can specify language with a secondary optional argument e.g. `model.transcribe('hello.wav', language='English')`

```python
import whisper
model = whisper.load_model('tiny') # returns model.Whisper object 
result = model.transcribe('hello.wav')
print(result['text'])
#  Hello. How are you doing?
```

## utils.get_writer()

- `whisper` can output files into `SRT`, `VTT`, `JSON`, `TXT` and `TSV` formats

```python
import whisper
model = whisper.load_model('tiny')
result = model.transcribe('hello.wav') # returns dictionary

write_function = whisper.utils.get_writer('srt','.') # 1st arg is format, . means cwd
write_function(result, 'audio') # use function to pass the resulting dictionary and output file name
```


### SRT

`SRT` - SubRip Subtitle, uses `.srt` extension, older but more commonly used

**SRT example:**
```text
1
00:00:00,000 --> 00:00:05,640
Dinosaurs are a diverse group of reptiles of the clade dinosauria. They first

2
00:00:05,640 --> 00:00:14,960
appeared during the triassic period. Between 245 and 233.23 million years ago.
```
### VTT

`VTT` - Web Video Text Tracks, uses `.vtt` extension, usually used in modern websites

**VVT Example:**
```text
WEBVTT

00:00.000 --> 00:05.640
Dinosaurs are a diverse group of reptiles of the clade dinosauria. They first

00:05.640 --> 00:14.960
appeared during the triassic period. Between 245 and 233.23 million years ago.
```

