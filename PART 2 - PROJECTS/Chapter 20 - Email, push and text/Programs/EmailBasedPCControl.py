# use popen to launch torrent downloader and download file if there is a ntfy message with password
# magnet: magnet:?xt=urn:btih:019f401abc505c88c5347a7b20989cd90d61e2ee&dn=babalablabsTestFile.txt&xl=22
"""
1. Loop forever, checking ntfy/email every 15 minutes
2. When message found, verify it contains your password
3. Extract the torrent link from the message
4. Launch qBittorrent with that link using subprocess.Popen()
5. Send yourself confirmation that download started
6. Optionally: use .wait() to know when download finishes, then notify again
7. Log everything to a file
8. Delete/mark the message as processed
"""

import time, subprocess, requests, json, re

REGEX = re.compile(r'magnet:\S+')
PASSWORD = "super_uber_secret_password"
NTFY_TOPIC = "https://ntfy.sh/Babalablabs-testing/json?poll=1"
PROCESSED = set()

while True :
	r = requests.get(NTFY_TOPIC) # pull all the messages
	#print(f"Status: {r.status_code}") # test
	#print(f"Response: '{r.text}'") # test
	lines = r.text.strip().splitlines()
	#print(response.text) # test, returns each message in separate lines

	for message in lines: # loop though each line
		#print(message) # {"id":"de2S4jnNWbxz","time":1767301798,"expires":1767344998,"event":"message","topic":"Babalablabs-testing","message":"super_uber_secret_password link: magnet:?xt=urn:btih:019f401abc505c88c5347a7b20989cd90d61e2ee\u0026dn=babalablabsTestFile.txt\u0026xl=22"}
		json_text = json.loads(message) # convert json into a python dictionary
		#print(json_text) # test
		msg_id = json_text['id'] # get the mssage ID
		if msg_id in PROCESSED: # check if message has already been processed
			continue
		PROCESSED.add(msg_id)
		print(f"Message ID: {msg_id} marked as checked")
		msg_body = json_text['message']
		
		if PASSWORD in msg_body: # grab message body
			print('password found in the message! Launching torrent...')
			link = REGEX.search(msg_body) # pull the match for the link
			magnet_link = link.group()
			print(f'got the magnet! {link.group()}') # test
			qbProcess = subprocess.Popen(['C:\\Program Files\\qBittorrent\\qbittorrent.exe', magnet_link]) # open torrent file in qbittorrent using magnet
			time.sleep(2) # give it a moment to open
			if qbProcess.poll() == None:
				print('Download started successfully...') # dry tun
				requests.post('https://ntfy.sh/Babalablabs-testing/', 'Download started successfully...')
				qbProcess.wait() # wait for program to close after downloading
				print('Download finished successfully!')
				requests.post('https://ntfy.sh/Babalablabs-testing/', 'Download finished successfully!')

	time.sleep(900) # 15min pause



# tst magnet msg to ntfy
# requests.post('https://ntfy.sh/Babalablabs-testing', 'super_uber_secret_password link: magnet:?xt=urn:btih:019f401abc505c88c5347a7b20989cd90d61e2ee&dn=babalablabsTestFile.txt&xl=22')