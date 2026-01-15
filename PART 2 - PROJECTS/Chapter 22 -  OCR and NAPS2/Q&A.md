# Practice Questions

## 1  What language does Tesseract recognize by default?

English

## 2  Name a Python image library that PyTesseract works with.

Pillow

## 3  What PyTesseract function accepts an image object and returns a string of the text in the image?

`pytesseract .image_to_string(Pillow_image_object)`

## 4  If you take a photo of a street sign, will Tesseract be able to identify the sign text in the photo?

Not by default. 
You would need to pre-process the sign by cropping to only text area, adjusting the contrast so text is more visible, rotating image so text is straight, etc.

## 5  What function returns the list of language packs installed for Tesseract?

`pytesseract.get_languages()`

## 6  What keyword argument do you specify to PyTesseract if an image contains both English and Japanese text?

`'eng+jpn'` as a 2nd variable in `.image_to_string()` function
`text = pytesseract.image_to_string(img_object, lang='eng+jpn')`

## 7  What application lets you create PDFs with embedded OCR text?

NAPS2