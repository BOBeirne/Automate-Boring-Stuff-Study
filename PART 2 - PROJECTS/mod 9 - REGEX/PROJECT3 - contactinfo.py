"""
Say you’ve been given the boring task of finding every phone number and email address in a long web page or document.

For example, your phone number and email address extractor will need to do the following:

Get the text from the clipboard.
Find all phone numbers and email addresses in the text.
Paste them onto the clipboard.
"""
import re, pyperclip

# Phone regex
phone_re = re.compile(r'''
                      (\d{3} | (\d{3})) # area code
                      (\s | - | \.)? # optional separator
                      (\d{3}) # first 3 digits of the nr after area code
                      (\s | - | \.) # separator
                      (\d{4}) # last 4 digits
                      (\s*(ext | x | ext\.) \s*(\d{2,5}))? # optional extension
                      ''' , re.VERBOSE)

# Email regex
email_re = re.compile(r'''
                         (
                             [a-zA-Z0-9._%+-]+ #  username
                             @ # literally "@" symbol
                             [a-zA-Z0-9.-]+ # domain name
                             (
                                 \.[a-zA-Z]{2,4}
                             ) # . something
                         )
                         ''' , re.VERBOSE)

# find matches in the clipboard txt
text = str(pyperclip.paste())
matches = []

for groups in phone_re.findall(text):
    phone_num = '-'.join([groups[0],groups[3],groups[5]])
    if groups[6] != '':
        phone_num += ' x' + groups[8]
    matches.append(phone_num)

for groups in email_re.findall(text):
    matches.append(groups[0])

# copy result back tio clipboard

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('copied to clipboard')
    print('\n'.join(matches))
else:
    print('no phone nrs or addresses found')