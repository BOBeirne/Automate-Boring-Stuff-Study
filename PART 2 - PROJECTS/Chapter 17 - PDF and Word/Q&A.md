# 📚 Practice Questions: PDF and Word Document Automation

## 📄 PDF Processing with `PyPDF2`

1.  **What modes does the File object for `PdfWriter` objects need to be opened in to save the PDF file?**

`with open('filename', 'wb')` - open method using **write binary** mode

1.  **How do you acquire a `Page` object for page 5 from a `PdfReader` or `PdfWriter` object?**

`reader.pages[4]` or `writer.pages[4]` 

1.  **If a `PdfReader` object’s PDF is encrypted with the password `swordfish`, what must you do before you can obtain `Page` objects from it?**

You need to **provide the password** using `reader.decrypt('swordfish')`

1.  **If the `rotate()` method rotates pages clockwise, how do you rotate a page counterclockwise?**

pass the `rotate()` method a **negative integer argument in multiplies of 90** (do instead of 90, use -90 for anti-clockwise rotation)

---

## 📝 Word Document Processing with `python-docx`

5.  **What method returns a `Document` object for a file named `demo.docx`?**

use a `docx.Document()` method `doc = docx.Document('demo.docx')`

6.  **What is the difference between a `Paragraph` object and a `Run` object?**

**Run object** is a **contagious** segment of text with the **same formatting style**
**Paragraph** is created **every time** a user presses `ENTER` or `RETURN` when typing in word

7.  **How do you obtain a list of `Paragraph` objects for a `Document` object that’s stored in a variable named `doc`?**

`doc.paragraphs`

1.  **What type of object has `bold`, `underline`, `italic`, `strike`, and `outline` variables?**

`Run object`

1.  **What is the difference between setting the `bold` variable to `True`, `False`, or `None`?**

It's an attribute that can be set on styles in a Run
- `True` - always enabled, regardless of what other styles are applied
- `False` - always disabled
- `none` - default's to whatever run's style is applied to it

1.  **How do you create a `Document` object for a new Word document?**

`doc = docx.Document()`

2.  **How do you add a paragraph with the text `'Hello, there!'` to a `Document` object stored in a variable named `doc`?**

`doc.add_paragraph('Hello, world')`

3.  **What integers represent the levels of headings available in Word documents?**

1-9