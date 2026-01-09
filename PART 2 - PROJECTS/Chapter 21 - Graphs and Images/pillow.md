# Pillow

- 3rd party module that allows you to open and edit images
- It **has functions such as cropping, resizing and editing image content**
- to **install** use `pip install pillow`
- **importing**:
  - to import **color recognition** use `from PIL import ImageColor`
  - to import **image editing** use `from PIL import Image`
  - to import **image drawing** use `from PIL import ImageDraw`


## Computer Image Fundamentals

- To be able to work with computer images, first you need to understand how they work.
- Computers **represent color** in and image as `RGBA` value - `Red`, `Green` `Blue` and `ALPHA` (transparent)
- each value is an integer 0-255 in a tuple `(R, G, B, A)`
  - Full strength `red` is `(255, 0, 0, 255)`
  - Full strength `green` is `(0, 255, 0, 255)`
  - Full strength `blue` is `(0, 0, 255, 255)`
  - `Black` is `(0, 0, 0, 255)`
  - `White` is `(255, 255, 255, 255)`
- `ALPHA` is the **transparency** of the image, the **lower** the **value**, the **more transparent the image is**

## ImageColor

- Pillow uses the **same standard color** names as **HTML**

### .getcolor()

- `ImageColor.getcolor()` returns a tuple of `(R, G, B, A)` if passed a string with color name
- get the **FULL LIST of color names** (100+) in the keys of `ImageColo,colormap` dictionary


```python
from PIL import ImageColor
ImageColor.getcolor("red", 'RGBA')
# (255, 0, 0, 255)
ImageColor.getcolor('chocolate', 'RGBA')
# (210, 105, 30, 255)
ImageColor.getcolor('CornflowerBlue', 'RGBA')
# (100, 149, 237, 255)
```

## coordinates

- **Coordinates** are in the `tuple` format and use `x` and `y` coordinates, where `x` is the horizontal position and `y` is the vertical position
- `Pillow functions` usually expect 4 arguments:
  - `Left` - x of Leftmost edge fo the box
  - `Top` - y of top edge of the box
  - `Right` x of one pixel to the right of Rightmost edge of the box (must be greater than `Left` argument)
  - `Bottom` - y of one pixel below the bottom edge of the box (must be greater than `Top` argument)
- Remember that **Right and bottom arguments are not included!**
  - for eg. Tuple (3, 1, 9, 6) would represent coordinates of a box with 
  - `left` edge at `x=3`, 
  - `top` edge at `y=1`, 
  - `right` edge at `x=8` **(NOT 9!)** 
  - `bottom` edge at `y=5` **(NOT 6!)**


## Manipulating Images

- We will be working with `zophie_original.jpg` from exercise files.

### Image.open()

- `Image.open()` returns an **Image object** that can be used to **manipulate** the image

```python
from PIL import Image
cat_img = Image.open('zophie_original.jpg') # open the image file
cat_img.show() # show the image in a image viewer
```

### Image Object

```python
from PIL import Image
cat_img = Image.open('zophie_original.jpg') # open the image file
###

cat_img.size # get the size of the image as a tuple
# (350, 467)

width, height = cat_img.size # split tuple into 2 variables
width # get width
# 350
height # get height
# 467
cat_img.filename # get the filename
# 'zophie_original.jpg'
cat_img.format_description
# 'Portable network graphics'

###
cat_img.save('zophie.jpg') #  dont forget to save at the end
```

### Image.new()

- returns `image object` just like `Image.open()` except this **image is blank**
- can be used to **create new images**
- You can **pass** the following **arguments** to the `Image.new()` function:
  - string `RGBA` - sets **color mode** to RGBA (there are other modes)
  - tuple `(width, height)` - sets the **size** of the image
  - tuple `(R, G, B, A)` - sets the **background color** of the image or a **string with the color name**
  - If you don't specify the color, the image will be transparent

Example:

```python
from PIL import Image
img = Image.new('RGBA', (100, 200), 'purple')
img.save('purpleImage.png')

img2 = Image.new('RGBA', (20,20))
img2.save('transparentImage.png')
```

### crop()

- `cropping` is selecting rectangular region inside an image and removing everything outside of it
- `crop()` method takes box tuple and returns Image object recpresenting the cropped image
- Original image is left unchanged, `crop()` method returns a new image

```python
from PIL import Image
cat_img = Image.open('zophie_original.jpg')
cropped_img = cat_img.crop((335, 345, 565, 565)) # crop from x=335, y=345 to x=564, y=559

cropped_img.save('cropped.png')

cropped_img.show()
```

### copy() and paste()

- `copy()` method **returns a new image** that is a copy of the original image
- The `paste()` method **modifies** its `Image object` in place, it doesn't return an `Image object` with the pasted image
  - to **keep untouched version of original**, you need to first `copy()` image and then call `paste()` on the copy
  - 
```python
from PIL import Image
cat_img = Image.open('zophie_original.jpg')
cat_copy = cat_img.copy()
face_img = cat_img.crop((335, 345, 565, 560))
print(face_img.size)
# (230, 215)

cat_copy.paste(face_img, (0, 0)) # paste face image on top left corner
cat_copy.paste(face_img, (400, 500)) # paste face image on bottom right corner
cat_copy.save('pasted.png') 
cat_copy.show()
```

#### Using loops

You can create an image pattern using loops

```python
from PIL import Image

cat_img = Image.open('zophie_original.jpg') # get th original image
width, height = cat_img.size # get the size of the image and split it into 2 vars
cat_copy = cat_img.copy() # copy the original

face_img = cat_img.crop((350, 450, 650, 600)) # get the face image
face_width, face_height = face_img.size 

for left in range(0, width, face_width): # loop through widths
	for top in range(0, height, face_height): # loop through heights
		print(left, top) # print coordinates
		cat_copy.paste(face_img, (left, top))

cat_copy.save('tiled.png') # save copy as new file
cat_copy.show() # see the result
```

### resize()

- `resize()` method is used to **resize** an image
- `resize()` method takes integer tuple `(width, height)`
  - it accepts only integers so you need to wrap then in `int()`
- It returns a new `Image object` that is a resized version of the original image

```python
from PIL import Image
img = Image.open('zophie_original.jpg')
width ,height = img.size

quarter_sized = img.resize((int(width/2), int(height/2))) # resize to quarter size
quarter_sized.show()
quarter_sized.save('quarter_sized.png')

svelte_img = img.resize((width, height + 300)) # you can also just change one variable like height only
svelte_img.show()
svelte_img.save('svelte.png')  # slimmed zophie
```

### rotate()

- `rotate()` method is used to **rotate** an image by `increments of 90 degrees` `counterclockwise`
- It accepts and optional keyword argument `expand` that can be set to `True` to expand the image to fit the entire rotated image

```python
from PIL import Image
img = Image.open('zophie_original.jpg')

img.rotate(90).save('rotated90.png')
img.rotate(180).save('rotated180.png')
img.rotate(270).save('rotated270.png')

# Optional expand argument
img.rotate(6).save('rotated6.png')
img.rotate(6, expand=True).save('rotated6_expanded.png')
img.rotate(90, expand=True).save('rotated90.png')
```

### transpose()

- Used to flip an image
- It accepts an argument `Image.Transpose` that can be set to `Image.Transpose.FLIP_LEFT_RIGHT` or `Image.Transpose.FLIP_TOP_BOTTOM`
- It returns a new `Image object` that is a transposed version of the original image

```python
from PIL import Image

img = Image.open('zophie_original.jpg')
img.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
img.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')
```

### getpixel() and putpixel()

- `getpixel()` method is used to **get** the color of a specific pixel
- It accepts an integer tuple `(x, y)` where `x` is the horizontal position and `y` is the vertical position
- `putpixel()` method is used to **set** the color of a specific pixel
  - it takes an additional argument for the color:
    - RGB tuple `(R, G, B)` where `R`, `G`, and `B` are integers between 0 and 255
    - RGBA tuple `(R, G, B, A)` where `R`, `G`, `B`, and `A` are integers between 0 and 255

```python
from PIL import Image
img = Image.new('RGBA',(100, 100)) # create new RGBA pic 100x100px

img.getpixel((0,0)) # get color of top left pixel
# (0, 0, 0, 0)

for x in range(100):
	for y in range(50):
		img.putpixel((x, y), (210, 210, 210)) # color half the image with this color value

img.show()

from PIL import ImageColor
for x in range(100):
	for y in range(50, 100):
		img.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA')) # color the other half

img.show()

img.getpixel((0,0)) # get color of top left pixel again
# (210, 210, 210, 255)
img.getpixel((0, 50)) # get color of pixel in the other half
# (169, 169, 169, 255)

img.save('putPixel.png')
```


## Drawing Images

- [Documentation](https://pillow.readthedocs.io/en/latest/reference/ImageDraw.html)
- You can use `Pillow module` to draw simple shapes on an image
- It uses a `ImageDraw` part of the module, import it using `from PIL import ImageDraw`
- It returns a `ImageDraw object` that can be used to draw on the image



```python
from PIL import Image, ImageDraw
img = Image.new('RGBA', (200, 200), 'white') # create white image
draw = ImageDraw.Draw(img) # create draw object
```

- It has OPTIONAL `fill` and `outline` parameters that can be used to set the color of the shape

### Point

- `point(xy, fill)` method draws a **point** at the specified coordinates
- It can be a **list** of **tuples** `(x, y)` where `x` is the horizontal position and `y` is the vertical position
- It can also have **just** `y` or `x` **coordinates** (eg. `[x1, y1, x2, y2, x3, y3 ...]` etc)
- `fill` argument is **optional** and used for **coloring**

### Line

- `line(xy, fill, width)` method **draws a line between the specified coordinates**
- It can be a **list of tuples** `(x, y)` or a **list of integers** `[x1, y1, x2, y2, x3, y3 ...]`
- `fill` argument is **optional** and used for **coloring**
- `width` is also **optional**, used to specify the **width of the lines** and **defaults to 1** if not specified

### Rectangle

- `rectangle(xy, fill, outline, width)` method draws a **rectangle between the specified coordinates**
- The `xy` argument is a **box tuple of the form `(left, top, right, bottom)`**
- `fill, outline, width` are **optional** and used for **coloring**, **outline** and **width** respectively

### Ellipse

- `ellipse(xy, fill, outline, width)` method draws an **ellipse between the specified coordinates**
- **If the `width` and `height` of the ellipse are identical**, this method will draw a **circle**
- The `xy` argument is a box tuple `(left, top, right, bottom)` representing a **box that precisely contains the ellipse**
- `fill, outline, width` are **optional** and used for **coloring**, **outline** and **width** respectively

### Polygon

- `polygon(xy, fill, outline, width)` method draws a **polygon between the specified coordinates**
- The `xy` argument is a list of tuples, such as` [(x, y), (x, y), ...]`, or integers, such as `[x1, y1, x2, y2, ...]`, representing the **connecting points of the polygon’s sides**
- `fill, outline, width` are **optional** and used for **coloring**, **outline** and **width** respectively

```python
from PIL import Image, ImageDraw
img = Image.new('RGBA', (200, 200), 'white') # create white image
draw = ImageDraw.Draw(img) # create draw object

draw.line([(0,0), (199, 199), (0,199), (0,0)], fill='black') # draw black line
draw.rectangle((20, 30, 60, 60), fill='blue') # draw blue rectangle
draw.ellipse((120, 30, 160, 60), fill='red') # draw red ellipse
draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)), fill='brown') # draw brown polygon

for i in range(100, 200, 10): # draw 10 green lines
    draw.line([(i,0),(200, i-100)], fill='green') # draw green lines
img.save('drawing.png') # save image
img.show() # show image
```

## Adding Text

- `ImageDraw object` also has a `text()` method for drawing text onto an image
- It takes 4 arguments
  - `xy` - the location of the text, upper left corner of the text box
  - `text` - the string
  - `fill` - color
  - `font` - optional `ImageFont` object used to set `typeface` and `size` of text

### ImageFont

- You import is from `PIL import ImageFont`
- `ImageFont object` is used to set the **typeface** and **size** of the text
- You can **access the font** by calling `ImageFont.truetype('font.ttf', size)`, where the `.ttf` is the actual **font file**
  - usual path is :
    - **Windows**: `C:\Windows\Fonts` 
    - **macOS**: `/Library/Fonts`
    - **Linux**: ` /usr/share/fonts/truetype`
  - You **don't need to specify path because Pillow knows where to search for it**
- `size` is in **points** `(1 point = 1/72 inch)`
- It returns an **ImageFont object** that can be used to draw text on an image

```python
from PIL import Image, ImageDraw, ImageFont
import os

img = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(img)

draw.text((20, 150), 'Hello', fill='purple') # draw text

arial_font = ImageFont.truetype('arial.ttf', 32) # specify arial font 32 points in size
draw.text((100, 150), 'Howdy', fill='gray', font=arial_font)

img.save('text.png') # save file
img.show() # show image
```