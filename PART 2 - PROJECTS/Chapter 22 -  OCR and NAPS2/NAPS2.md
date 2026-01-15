# Not Another PDF Scanner 2

- Open source software for PDF generation
- It can be used with tesseract OCR
- It can combine multiple images into a single PDF with embedded text

## Installation

- [Download page](https://www.naps2.com/download)

### Windows & macOS

- Download exe and run the installed

### Linux

- **download** the Flatpak **installer** for Tesseract
- run `flatpak install naps2-X.X.X-linux-x64.flatpak` to install
- to run the program run `flatpak run com.naps2.Naps2`

### pip

- there is no naps2 module in pip, you will use subprocess to run the installed naps2 software
- Pass it extra CLI agruments or in the subprocess, for eg `subprocess.run(+['arguments'])`

## Usage

```python
import subprocess
naps2 = [r'C:\Program Files\NAPS2\Naps2.Console.exe'] # use the console version!
# macOS: naps2 = ['/Applications/NAPS2.app/Contents/MacOS/NAPS2', 'console']
# Linux: naps2 = ['flatpak', 'run', 'com.naps2.Naps2', 'console']
process = subprocess.run(naps2 + ['-i', 'frankenstein.png', '-o', 'output.pdf', '--install', 'ocr-eng', '--ocrlang', 'eng', '-n', '0', '-f', '-v'])
"""output:
Installing ocr-eng...
Importing...
Imported file 1 of 1.
Exporting...
Exporting page 1 of 1.
System.IO.EndOfStreamException: End of stream reached with 4 byte left to read.
   at SixLabors.Fonts.BigEndianBinaryReader.ReadInternal(Byte[] data, Int32 size)
   at SixLabors.Fonts.BigEndianBinaryReader.ReadUInt32()
   at SixLabors.Fonts.Tables.TableHeader.Read(BigEndianBinaryReader reader)
   at SixLabors.Fonts.FontReader..ctor(Stream stream, TableLoader loader)
   at SixLabors.Fonts.FontReader..ctor(Stream stream)
   at SixLabors.Fonts.FontDescription.LoadDescription(String path)
   at PdfSharpCore.Utils.FontFileInfo.Load(String path)
   at PdfSharpCore.Utils.FontResolver.SetupFontsFiles(String[] sSupportedFonts)
Successfully saved PDF file to output.pdf
"""
```

## Console Arguments

All commands: https://www.naps2.com/doc/command-line

- `-i` set the input as image file
- `-o` output PDF file as `output.pdf` to hold the OCR results
- `-install` install OCR engine 
  - `ocr-eng` install English language
- `-ocrlang` set the OCR language 
  - `eng` the specified language
- `-n` set the page number
  - `0` if set to `0` it prevents error messages when not using flatbed scanner
- `-f` force NAPS2 to overwrite the output file if it already exists
- `-v` verbose mode - print more information

## Specifying Input

- NAPS2 has it's own "mini-language" for specyfying multiple inputs following `-i`

### Using multiple images:
- for example: `'-i', 'cat.png;dog.png;moose.png' `
- creates a PDF with `cat.png` used for the **first page**, `dog.png` used for the **second page**, and `moose.png` used for the **third page**.

### Using pdf page index
- `'-i', 'spam.pdf[0];spam.pdf[5];eggs.pdf'`
- creates a PDF with **page 1** of `spam.pdf`, followed by **page 6** of `spam.pdf`, and **then all pages** of `eggs.pdf`.

- Use index `[-1]` to specify the last page of pdf document
- You can also use index slices: `spam.pdf[0:2]`
- `'-i', 'spam.pdf[0:2];eggs.pdf[-1]'` combines the **first two pages** of `spam.pdf` with the **last page** from `eggs.pdf`.


## ocrmypdf 

- [Link](https://pypi.org/project/ocrmypdf/)
- Alternative to NAPS2
- It can also generate pdfs with embedded text