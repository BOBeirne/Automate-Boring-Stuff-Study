# Questions

  1.  What is an RGBA value?

`R` - amount of Red in the pixel (0-255)
`G` - Amount of Green
`B` - Amount of Blue

`A` transparency value 0-255 also, where 0 is most transparent


  2.  How can you get the RGBA value of 'CornflowerBlue' from the Pillow module?

you need to import `from PIL import ImageColor`
and then get value of color in `ImageColor.colormap` using `ImageColor.getcolor('CornflowerBlue', 'RGBA')`

  3.  What is a box tuple?

it's a set of box coordinates from x,y of top left corner to the bottom right xy corner coordinates 1 pixel past the box in the last 2 coordinates

  4.  What function returns an Image object for, say, an image file named zophie.png?

`image = Image.open('zophie.png')`

  5.  How can you find out the width and height of an Image object’s image?

using `.size` atrribute lets say `image.size` or you can split it into 2 values with `width, height = image.size` and then call on each variable separately

  6.  What method would you call to get the Image object for the lower-left quarter of a 100×100 image?

- 1. You get the image object of the original file
- 2. get the cropped value of img using `cropped = img.crop((0,50, 50, 100))` the image object would be then in the cropped value

  7.  After making changes to an Image object, how could you save it as an image file?

call on `.save()` method, `img.save('image.png')`

  8.  What module contains Pillow’s shape-drawing code?

`ImageDraw`

  9.  Image objects do not have drawing methods. What kind of object does? How do you get this kind of object?

`ImageDraw object`
You get it by using `ImageDraw.Draw(image)` method, where image is the variable of the image object

10.  Which Matplotlib functions create a line graph, scatter plot, bar graph, and pie chart?

`.plot()` creates line graph
`.scatter()` creates scatter plot
`.bar()` creates bar
and `.pie()` creates a pie chart

11.  How can you save a Matplotlib graph as an image?

use `.savefig()` method just like `.save()` on image object

12.  What does the plt.show() function do, and why can’t you call it twice in a row?

it shows the resulting plot
the data resets (gets closed) after calling that method so if you want to save changes do it before calling the `.show`