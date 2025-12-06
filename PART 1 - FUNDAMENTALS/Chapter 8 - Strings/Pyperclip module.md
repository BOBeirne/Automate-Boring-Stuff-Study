
# Pyperclip module

The pyperclip module needs to be installed first!

You don't need to rely on the `input()` to read text from files or keyboard, you can instead use **pyperclip module** to read text from clipboard

```python
import pyperclip # import the module
text = pyperclip.paste() # obtain the input text from the clipboard
# do some operations on the text here
pyperclip.copy(text) # copy the input text back to the clipboard
```

More info in the [pyperclip documentation](https://pypi.org/project/pyperclip/)