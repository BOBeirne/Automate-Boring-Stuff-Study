# finds all unsubscribe links in the inbox and opens them in a browser (webbrowser module)

import ezgmail, webbrowser, requests, base64, bs4


# find all emails with the word 'unsubscribe'
for thread in ezgmail.search('unsubscribe'):
	#print(thread)
	# found: [<GmailThread numMessages=1 snippet='resources. <b>Unsubscribe</b> from notifications for this question. Google Support © 2025 Google Inc. 1600 Amphitheatre Parkway'>]
	for message in thread.messages:
		#print(dir(message))
		#print(f'ID: {message.id}')
		#print(f'Body: {message.originalBody}')
		message_id = message.id
		# Find HTML contents of the e-mail
		#print(dir(ezgmail))
		messageContent = ezgmail.SERVICE_GMAIL.users().messages().get(userId='me', id=message_id, format='full').execute() # get the full message content
		#print(messageContent['payload']['parts'][1]['body']['data'])
		HTMLContent = messageContent['payload']['parts'][1]['body']['data'] # find the encoded HTML content 
		decodedMessage = base64.urlsafe_b64decode(HTMLContent)
		#print(decodedMessage)

		# Parse HTML using beautifulsoup
		soup = bs4.BeautifulSoup(decodedMessage, 'html.parser')
		linkElement = soup.select('a') #find link element
		#print(f'\n {linkElement}')
		for elem in linkElement:
			link = elem.get('href')
			#print(link)
			if 'unsubscribe' in link:
				print(f'Found a link to unsubscribe! \n {link}')
				webbrowser.open_new_tab(link)