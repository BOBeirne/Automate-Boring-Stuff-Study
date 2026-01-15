# OCR

- **OCR** stands for **optical character recognition**
- It is a module that **reads text from images**
- **Installs and recognizes English** text by default
- You can install **extra language packs** for other languages from [here](https://github.com/tesseract-ocr/tessdata_fast)
  - These language packs have filenames identifying the language and a `.traineddata` extension, such as `jpn.traineddata` for **Japanese**
- It **installs with** `Pillow` module by default as it needs it to work
- Install with pip by `pip install pytesseract`
- Use `import pytesseract` to **import module** along with `from PIL import Image`

## Installation of Tesseract OCR engine

### Windows

- **Install** OCR by going to project's [github Page](https://github.com/UB-Mannheim/tesseract/wiki) and following the instructions
- You can install **optional languages** during the installation or using the command line later
- You need to **add** the program to your **PATH** environment variable on windows path: `C:\Program Files\Tesseract-OCR`

### macOS

- use [Homebrew](https://brew.sh/) package manager to install OCR
  - `brew install tesseract`
  - `brew install tesseract-lang` for **extra language packs**

### Linux

- use `sudo apt-get install tesseract-ocr` to **install the package**
- for any **additional language** `sudo apt install tesseract-ocr-all` or replace `all` with package name in **three-character ISO 639 language code**

### PIP

- After installing the engine, use pip to install the module 
- `pip install pytesseract`

## Basic data extraction

```python
import pytesseract as tess
from PIL import Image

img = Image.open('ocr-example.png')
text = tess.image_to_string(img)
print(text)
"""
This book provides you with practice examples of how programming
concepts are applied, with a collection of over 80 games, simulations, and dig-
ital art programs. These aren't code snippets; they're full, runnable Python (...)
"""
```

## Preprocessing 

- By default, tessaract is intended for print documents, rather than photos or handwritten text
- You can preprocess the image by cropping to only text area, adjusting the contrast so text is more visible, rotating image so text is straight, etc. in order to increase the chances of successful OCR

Best steps to ensure image is OCR readable:
- Crop to only text area
- Adjust contrast
- Rotate image so text is straight
- Reduce noise
- split multicolumnt images into separate image files
- Do not use handwritten text
- Use conventional fonts
- Dark font on light background
- [More information](https://autbor.com/preprocessingocr)

Common OCR output issues
- output strings do not conserve font or size information
- string will maintain any end-of-line hyphenations 
- whitespaces may not match
- it may incorrectly recognise similar characters such as `j` and `i`
- If there are columns of texts or tables, the data may be out of order 
- Numbers are prone to mistakes and should be paid special attention to

## Using LLMs to fix the OCR output

- LLMs are a great tool to perform the spellcheck and fix any OCR errors
- The downside is that they can hallucinate some of the output so make sure to use them with caution and check output for errors

```python
import pytesseract as tess
from PIL import Image
img = Image.open('frankenstein.png')
text = tess.image_to_string(img)
print(text)
"""
THE MODERN PROMETHEUS. 43

CHAPTER V.

Iv was on a dreary night of November, that I beheld the 
accomplishment of my toils. With an anxiety that almost
amounted to agony, I collected the instruments of life
around me, that I might infuse a spark of being into the
lifeless thing that lay at my feet. It was already one in
the morning ; the rain pattered dismally against the panes,
and my candle was nearly burnt out, when, by the glimmer
of the half-extinguished light, I saw the dull yellow eye
of the creature open ; it breathed hard, and a convulsive
motion agitated its limbs.
"""
# notice the Iv instead of Iv on the first line
```

### LLM Prompt

```text
The following is the text output from an OCR scan. Correct any spacing, missing characters, or inaccurately recognized characters from it. Do not correct spelling or grammar mistakes that exist in the original text. Put paragraphs on a single line and undo the hyphenated words that are broken across the end of a line. Only give the corrected text without explaining what OCR is or any other preface. Here is the text:
```

### LLM output:

```text
THE MODERN PROMETHEUS. 43 CHAPTER V. I was on a dreary night of November, that I beheld the accomplishment of my
  toils. With an anxiety that almost amounted to agony, I collected the instruments of life around me, that I might
  infuse a spark of being into the lifeless thing that lay at my feet. It was already one in the morning ; the rain
  pattered dismally against the panes, and my candle was nearly burnt out, when, by the glimmer of the half-extinguished
  light, I saw the dull yellow eye of the creature open ; it breathed hard, and a convulsive motion agitated its limbs.
```

- Notice misspelling of "I" instead it "It1", it did however fix the rest of the text into easier-to read string

#### **Always remember that LLMs are prone to overconfidence. You should always verify their output.**

## Other languages

- To get a **list of all installed languages** use: `tess.get_languages()`
- The strings in the list are mostly **three-character ISO 639-3 language codes, with a few exceptions.**
- To specify used language pass the `lang='xxx'` parameter as a 2nd argument to the `image_to_string()` function

### Japanese

```python
import pytesseract as tess
from PIL import Image
img = Image.open('frankenstein_jpn.png') # Japanese edition
text = tess.image_to_string(img, lang='jpn')
print(text)
"""
第 5 剖 私が自分の労苦の成果を目の当たりにしたのは、11 月の芝鬱な夜でした。 ほとんど苦
痛に等しい不安を抱えながら、私は足元に横たわる生命のないものに存在の輝きを吹き込むこ
とができるように、身の回りの生命の道具を集めました。 もう午前一時だった。 雨が窓ガラス
"""
```

### Multiple languages

- You can use `tess.image_to_string(img, lang='eng+jpn')` to get both English and Japanese if you suspect there are more than 1 language being used

```python
import pytesseract as tess
from PIL import Image
img = Image.open('frankenstein_jpn.png') # Japanese edition
text = tess.image_to_string(img, lang='eng+jpn')
print(text)
"""
第 5 剖 私 が 自分 の 労苦 の 成果 を 目の当たり に し た の は 、11 ADBBERKCLE, ほとん ど 苦
痛 に 等 し い 不 安 を 抱え な が ら 、 私 は 足元 に 横たわる 生命 の な いも の に 存在 の 輝き を 吹き 込む こ
と が で きる よう に 、 身 の 回 り の 生命 の 道具 を 集め まし た 。 も う 午 前 一 時 だ っ た 。 雨 が 窓 ガ ラス
"""
```