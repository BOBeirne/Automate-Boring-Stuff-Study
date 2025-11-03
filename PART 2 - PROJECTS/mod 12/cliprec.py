import pyperclip, time

print('Recording clipboard...')

previous_content = ''
try:
	while True:
		content = pyperclip.paste() # get the clipboard contents

		if content != previous_content: # if it's different from previous
			print(content) # print it
			previous_content = content
		time.sleep(0.01) # pause to avoid hogging CPU
except KeyboardInterrupt:
	pass