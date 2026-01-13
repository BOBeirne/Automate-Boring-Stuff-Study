"""
In a practice program in Chapter 17, you created custom invitations from a list of guests in a plaintext file. 
As an additional project, use Pillow to create images that will serve as custom seating cards for your guests. 

For each of the guests listed in the guests.txt file from the book’s online resources, generate an image file with the guest’s name and some flowery decoration. 
A public domain flower image is also available in the book’s resources.

To ensure that each seating card is the same size, add a black rectangle to the edges of the invitation image; 
that way, when you print the image, you’ll have a guideline for cutting. 
The PNG files that Pillow produces are set to 72 pixels per inch, so a 4×5-inch card would require a 288×360-pixel image.
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

src = 'guests.txt'

def make_card(name):
	print(f'Creating card for {name}')
	img = Image.new('RGBA', (288, 360), 'white') # make new placeholder with selected size
	draw = ImageDraw.Draw(img) # get the draw object
	
	# add flower
	flower = Image.open('flower.png')
	flower2 = flower.copy()
	img.paste(flower, (0,50))
	#print('added flower') # test

	# add rectangle
	draw.rectangle((0, 0, 288, 360), outline='black', width=10)
	#print('added rectangle') # test

	arial_font = ImageFont.truetype('arial.ttf', 25)
	draw.text((80,35), name, fill='Black', font=arial_font)
	#print('added text') # test

	img.save('Card for '+ name + '.png')
	img.show()

# get the list of guests as a list
p = Path('guests.txt')
guestsList = [] # list of guests
guests = p.read_text()
guests = guests.splitlines()
#print(guests)
for line in guests:
	guestsList.append(line)
print(guestsList)

# try & except blocks
try:
	for guest in guestsList:
		make_card(guest)
	print('Completed.')
except Exception as err:
	print(f'An exception occured: {err}')