# Pyperclipimg module

- Just like pyperclip module, but for images
- `pyperclipimg.copy()` function takes a Pillow Image object and copies it to the clipboard
- `pyperclipimg.paste()` function returns a Pillow Image object that is a copy of the image in the clipboard

```python
from PIL import Image
import pyperclipimg

img = Image.open('zophie_original.jpg')
pyperclipimg.copy(img) # copy image to the clipboard
pasted_img = pyperclipimg.paste() # paste image from the clipboard
pasted_img.show()
```