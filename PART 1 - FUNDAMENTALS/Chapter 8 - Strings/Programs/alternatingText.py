import pyperclip

text = pyperclip.paste() #  get txt off clipboard
alt_text = '' #this str holds alternating case
make_uppercase = False
for char in text:
    #go through each char and add it to the the alt_text
    if make_uppercase:
        alt_text += char.upper()
    else:
        alt_text += char.lower()
    
    #Set make_uppercase to alternating val
    make_uppercase = not make_uppercase

pyperclip.copy(alt_text) #put result into the clipboard
print(alt_text) # print the result too