# PDF documents

- PDF stands for Portable Document Format
- uses `.pdf` extension
- They are binary files, containing font, color, layout etc. information which makes them much more complex than plaintext (same as word files)
	- as they are more complex, you cannot use `open()` to read them
	- You can use `PyPDF` library to read them
- this chapter focuses on 3 tasks: 
	- extracting text from PDF
	- extracting images from PDF
	- creating PDF files from existing documents

## PyPDF

- [docs](https://pypdf.readthedocs.io/en/latest/)
- To install using pip, run `pip install pypdf`
	- You can also install it from [PyPI](https://pypi.org/project/pypdf/)
- Calling the `Page` object’s `extract_text()` method, returns a `string` that we can `concatenate` to the `text variable`.

## pdfminer.six

- In the book Al uses also `pdfminer` library
- Newer version of `pdfminer` is `pdfminer.six` which supports bot Python 3 and 2 (3*2=6, hence the name six)
	- the older version `pdfminer` supports Python 2.7 and above but it's no longer maintained
- install using `pip install pdfminer.six`
- to import use `import pdfminer.high_level`
- Module's `extract_text() function` obtains the PDF's contents as a **single string**, rather than operating one page at a time (like PyPDF)


### Extracting text from PDF

- `pages attribute` of a `PdfReader object` returns a list of `Page objects`that represent **individual pages** in the PDF
	- you can pass it to `len()` to get the number of pages

```python
import pypdf # or from pypdf import PdfReader
reader = pypdf.PdfReader('Recursion_Chapter1.pdf') # open PDF file
print(len(reader.pages)) # get number of pages
#18 # number of pages
```

- To extract output to text file, you need to use `extract_text()` method

```python
import pypdf 
import pdfminer.high_level # module for extracting text from PDF, used as a backup

PDF_FILENAME =  'Recursion_Chapter1.pdf'
TXT_FILENAME = 'recursion.txt'

text = '' # empty string to hold text

try:
	reader = pypdf.Pdfreader(PDF_FILENAME)
	for page in reader.pages:
		text += page.extract_text()
except Exception:
	text = pdfminer.high_level.extract_text(PDF_FILENAME)
with open(TXT_FILENAME, 'w', encoding='utf-8') as file_obj:
	file_obj.write(text)
```

#### Post-processing extracted text

- PDF was never intended to be used for writing, so it's not formatted like plaintext. It was made for printing.
	- This produces a lot of extra whitespace and newlines.
- [List of tips for post-processing PDFs](https://pypdf.readthedocs.io/en/latest/user/post-processing-in-text-extraction.html)

- LLMs are capable of cleaning up this formatting with a prompt like this:
	- Make sure to review the output as in Al's case, the LLM removed a sentence "chapter number 1" from the text.

- **Example prompt:** (I have refined this prompt from the one in Al's book)
```
The following is text extracted from a PDF from a book on recursive algorithms. 
Clean up this text by putting paragraphs on a single, separate line, removing the footer and header text from each page, and get rid of the hyphens at the end of each line for words split up across the line. 
Do not make any spelling, grammar corrections, or rewording.
```

### Extracting images from PDF

- `PyPDF` can also extract images from PDFs

- Each `Page object` has an `images attribute` containing a `list-like data structure` of `Image objects`
	- They can be `written in bytes` to an image file using `wb` mode and `image.data attribute`
	- `Image objects` have also `name attribute` containing the name of the image, call it using `image.name`

```python
import pypdf
PDF_FILENAME = 'Recursion_Chapter1.pdf'

reader = pypdf.PdfReader(PDF_FILENAME)
image_nr = 0
for i, page in enumerate(reader.pages): # enumerate() returns a tuple, i is the index
print(f'Reading page {i+1} - {len(page.images)} images found...')
	try:
		for image in page.images:
			with open(f'{image_nr}.jpg', 'wb') as image_file:
				image_file.write(image.data)
			print(f'Wrote {image_nr}_page{i+1}_{image.name} ...')
			image_nr += 1
	except Exception as exc_name:
		pint(f'Failed to extract images from page nr {i+1}: {exc_name}')
```

### Creating PDF files from existing PDFs

- `PyPDF` can also create PDF files but can only operate on other PDF files
- It can copy, merge, crop and transform pages from other PDF files

```python
import pypdf

writer = pypdf.PdfWriter() # create a PdfWriter object, a blank PDF
writer.append('Recursion_Chapter1.pdf', (0,5)) # appends pages 1-5 from Recursion_Chapter1.pdf,0 is 1st page's index, does not include 6th page (5th index)
# tuple provided to append method can have 3 attributes (see notes below*)
with open('FirstFivePages.pdf', 'wb') as file_obj:
	writer.write(file_obj) # generate new PDF file with pages 1-5
```

#### .append() method in pypdf*

- **This is specific only to `pypdf` module!!!**

- `.append() pypdf method` can be used to copy pages from other PDF files but **it does not work the same as the `.append() method` in a list** as it **does NOT include the last index from the tuple range**. It matches the `.range()` method in a list instead.
- `.append()` method in this case can contain **either 2 or 3 integer attributes**
	- `1st integer` is the **first index of the page** to be copied (1st page is index 0)
	- `2nd integer` is the **one before last index of the page** to be copied (5th page is index 4), unlike a list which includes the last index
	- `3rd integer` is OPTIONAL and you can use it to skip pages, like so:
- Example of the `.append()` method compared to the `.range()` method using a list

```python
list(range(0, 5))  # Passing (0, 5) makes append() copy these pages:
# [0, 1, 2, 3, 4]
list(range(0, 5, 2))  # Passing (0, 5, 2) makes append() copy these pages:
# [0, 2, 4]
```

- `append()` method can also **accept** a `list argument` with page `number integers` for **each page to append**.
- instead of using a tuple, you can use a list of pages

```python
writer.append('Recursion_Chapter1.pdf', [0, 1, 2, 3, 4])
# [0, 1, 2, 3, 4] are the indexes of the pages to append
```

### Rotating PDF pages

- `PyPDF` can also **rotate** pages **in 90 degree increments** 
	- use 90, 180, 270 degrees for clockwise rotation or 
	- -90, -180, or -270 degrees for anti-clockwise rotation

**Example:**

```python
import pypdf
writer = pypdf.PdfWriter() # create a PdfWriter object, a blank PDF
writer.append('Recursion_Chapter1.pdf') # copy all the pages from Recursion_Chapter1.pdf

for page in range(len(writer.pages)):
	writer.pages[page].rotate(90) # rotate page 90 degrees clockwise

with open('rotated90.pdf', 'wb') as file_obj: # generate new PDF file with rotated pages
	writer.write(file_obj)
```

### inserting blank PDF pages

- `PyPDF` can **insert** a **blank page** into a `PDFWriter object` using `.insert_blank_page(index=nr`) and `.add_blank_page()` methods
- `index=nr` is the index of the page to insert the blank page before

**Example**:
- we will insert a blank page after page 2 (on page 3) and at the end of the document

```python
import pypdf
writer = pypdf.PdfWriter() # create a PdfWriter object, a blank PDF
writer.append('Recursion_Chapter1.pdf') # copy all the pages from Recursion_Chapter1.pdf

writer.add_blank_page() # insert a blank page at the end of the document
writer.insert_blank_page(index=2) # insert a blank page before page 3

with open('with_blanks.pdf', 'wb') as file_obj: # generate new PDF file with blank pages
	writer.write(file_obj)
```

### Adding Watermarks and Overlays

- `PyPDF` can overlay the contents of on page of top of another, which is useful for adding logo, timestamp or watermarks
- For merging pages, use the `.merge_page()` method
	- by **default** it **merges** selected page** on top of selected page**
	- to merge **under** use `.merge_page(page, over=False)` for watermarks
**Example:**
- We will be using `watermark.pdf` from exercise files

```python
import pypdf
writer = pypdf.PdfWriter() # create a PdfWriter object, a blank PDF
writer.append('Recursion_Chapter1.pdf') # copy all the pages from Recursion_Chapter1.pdf

watermark_page = pypdf.PdfReader('watermark.pdf').pages[0] # read watermark page

for page in writer.pages:
	page.merge_page(watermark_page) # merge watermark page on top of page

with open('with_watermark.pdf', 'wb') as file_obj: # generate new PDF file with watermark
	writer.write(file_obj)
```

### Encrypting and Decrypting PDFs

- You can **encrypt the PDF with a password,** but encryption is only as strong as the password
- use `encrypt() method` on `PdfWriter obj` to **encrypt it**
- There is **no way to reset the password**
- **Recommended** algorithm is `AES-256`

**Example:**
```python
import pypdf
writer = pypdf.PdfWriter() # create blank PdfWriter object
writer.append('Recursion_Chapter1.pdf') # copy file content to the writer object

writer.encrypt('swordfish', algorithm='AES-256')

with open('encrypted.pdf', 'wb') as file_obj:
	writer.write(file_obj)
```

- use `is_encrypted` method to check if a PDF is encrypted or not

```python
import pypdf
reader = pypdf.PdfReader('encrypted.pdf')
writer = pypdf.PdfWriter() # create blank PdfWriter object

reader.is_encrypted
# True
reader.pages[0]
# (exception...) raise FileNotDecryptedError("File has not been decrypted")
reader.decrypt('wring_pw').name
# 'NOT_DECRYPTED'
reader.decrypt('swordfish').name
# 'OWNER_PASSWORD'
""" This method below is unreliable for working on files modified (decrypted) in the memory, use page by page """
writer.append(reader) # copy file content to the writer object - This will NOT work with decrypted files that have more than 1 pages!!!
""" Use this instead for pdf files with 1+ pages """
for page in reader.pages: # this works, Must use a page-by-page loop to ensure the writer copies the content after it has been unlocked/decrypted in memory
 writer.add_page(page)

with open('decrypted.pdf', 'wb') as file_obj:
	writer.write(file_obj)
```

#### User and owner passwords

- PDFs can have **user** and **owner** passwords
  - User password is used to **decrypt** the PDF to **view** its contents **only**, it is a **first argument** in `encrypt()` method
  - Owner password is used to **encrypt** the PDF and be able to **modify** its contents, it is a **second (optional) argument** in `encrypt()` method
  - If only one password is provided, it will be used for both user and owner passwords
- To decrypt a PDF with owner password, use `decrypt(pw)` method, this returns `PasswordType object`
  - `PasswordType.name` attribute returns the type of password - `OWNER_PASSWORD`, `USER_PASSWORD` or `NOT_DECRYPTED` if it's a wrong password