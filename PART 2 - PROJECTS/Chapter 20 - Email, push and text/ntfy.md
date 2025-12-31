# Push Notifications

## HTTP pub-sub

- HTTP notification services allowing you to **send and receive short messages** over `HTTP web requests `- **Chapter 13 for more info** on requests

## ntfy

- [Docs](https://docs.ntfy.sh/)
- ntfy is a **free service**, that lets you send push notifications to your phone or desktop via scripts from any computer, using simple HTTP PUT or POST requests
  - **Free users are limited to 250 messages per day**
  - messages can be 4,096 bytes in size
- To receive notifications on your phone, **install the app and subscribe to a "topic" of your choosing.**
  - Topics are **case-sensitive**
  - **Anyone** in the world can **send** messages to a topic, and anyone in the world can **subscribe** to a topic to read these messages, so **don't use it for sensitive info**
  - To create a secret / private topic you need to use a radom token such as a hash name and keep it private
- Messages **support emojis and markdown formatting** but you need to enable it `headers={ "Markdown": "yes" })`

### Sending notification

- It is essentially **making an HTTP request to ntfy webserver**
- `requests` module is used to make HTTP requests, there is no need for fancy 3rd party packages
- use `requests.post()` to make a POST HTTP request to send a notification
- there is **no way to determine who posted a message** to a topic, so you may want to include “To” and “From” labels

```python
import requests
requests.post('https://ntfy.sh/AlSweigartZPgxBQ42', 'Hello, world!')
#<Response [200]>
```

- This is a **great thing to include in programs** that run for a longer time to notify you once they're done with the boring task

### Transmitting Metadata

- ntfy **supports transmitting** `metadata` with each notification, such as `title`, `priority` and `tags`
  - `title` - similar to **subject** line
  - `priority` - 1-5, **default 3**
  - `tag` - keywords used to **filter** messages or name of [emoji](https://docs.ntfy.sh/publish/#tags-emojis) to use
- It is **included in HTTP requests as `headers`** - require a **dictionary** as a **second argument** to `requests.post()`

```python
import requests
requests.post('https://ntfy.sh/AlSweigartZPgxBQ42', 'The rent is too high!', headers={'Title':'Important: Read this!', 'Tags': 'warning,neutral_face', 'Priority':'5'})
#
```

### Receiving Notifications

- You can also read the messages posted to topic by making HTTP requests with the `resuests` module
- Notice the URL ends with `/json?poll=1`
- 
- You can also add additional parameter, like `since=1h` to receive only messages send in the last hour
  - `since=1737866912` Retrieves all messages since the `Unix epoch` timestamp of 1737866912
  - `since=wZ22cjyKXw1F` Retrieves all messages after the message that had the **ID of 'wZ22cjyKXw1F'.**
  - Separate additional URL parameters by an ampersand (&) -  `https://ntfy.sh/AlSweigartZPgxBQ42/json?poll=1&since=10m`

```python
import requests
resp = requests.get('https://ntfy.sh/AlSweigartZPgxBQ42/json?poll=1')
resp.text
# '{"id":"plHuKebqLlA7","time":1767172751,"expires":1767215951,"event":"message","topic":"AlSweigartZPgxBQ42","message":"Hello, world!"}\n{"id":"vsyyGdQqHgfo","time":1767174271,"expires":1767217471,"event":"message","topic":"AlSweigartZPgxBQ42","title":"Important: Read this!","message":"The rent is too high!","priority":5,"tags":["warning","neutral_face"]}\n'
```

### API

- You can subscribe to HTTP stream to receive messages instantly as they are posted
- [Docs](https://docs.ntfy.sh/subscribe/api/)

### JSON

-  `json.loads() function` converts the JSON text from ntfy **into a Python dictionary**
	- `"id"`:"wZ22cjyKXw1F" The 'id' key’s value is a unique identification string that can help differentiate multiple notifications even if they have the same text.
	- `"time"`:1797823712 The 'time' key’s value is a **Unix epoch timestamp of when the notification was created**. Calling `str(datetime.datetime .fromtimestamp 1797823712)` returns the **human-readable string '2026 -12-20 21:28:32'.**
	- `"expires"`:1797866912 The 'expires' key’s value is a** Unix epoch timestamp of when the notification will be deleted** from the ntfy server.
	- `"event"`:"message" The 'event' key’s value can be either 'message', 'open', 'keepalive', or 'poll_request'. These event types are explained in the online documentation, but for now, you’re probably only interested in 'message' events.
	- `"topic"`:"AlSweigartZPgxBQ42" The topic **part of the URL** is repeated in the **'topic' key’s value.**
	- `"title"`:"Important: Read this!" **If the notification has a title, there will be a 'title' key **with it as a string value.
	- `"message"`:"The rent is too high!" The 'message' key’s value is a **string** of the **notification’s text**.
	- `"priority"`:5 **If the notification has a priority, there will be a 'priority' key** with an integer value from 1 to 5.
	- `"tags"`:["warning","neutral_face"] **If the notification has tags, there will be a 'tags' key** with it as a list of string values. These string values may be the **names of emoji characters** to display.

```python
import json, requests, time
resp = requests.get('https://ntfy.sh/AlSweigartZPgxBQ42/json?poll=1')
#print(f"Response status code: {resp.status_code}") # Check if it's 200 (OK)
#print(f"Content of resp.text: '{resp.text}'") # See what's actually in resp.text
resp.text
notifications = []
time.sleep(2) # script runs too fast for response to come back in time
for json_text in resp.text.splitlines():
	notifications.append(json.loads(json_text))
	#print(json_text)
	# {"id":"plHuKebqLlA7","time":1767172751,"expires":1767215951,"event":"message","topic":"AlSweigartZPgxBQ42","message":"Hello, world!"}
	# {"id":"vsyyGdQqHgfo","time":1767174271,"expires":1767217471,"event":"message","topic":"AlSweigartZPgxBQ42","title":"Important: Read this!","message":"The rent is too high!","priority":5,"tags":["warning","neutral_face"]}
#print(notifications)
# [{'id': 'plHuKebqLlA7', 'time': 1767172751, 'expires': 1767215951, 'event': 'message', 'topic': 'AlSweigartZPgxBQ42', 'message': 'Hello, world!'}, {'id': 'vsyyGdQqHgfo', 'time': 1767174271, 'expires': 1767217471, 'event': 'message', 'topic': 'AlSweigartZPgxBQ42', 'title': 'Important: Read this!', 'message': 'The rent is too high!', 'priority': 5, 'tags': ['warning', 'neutral_face']}]
notifications[0]['message']
# 'Hello, world!'
notifications[1]['message']
# 'The rent is too high!'
```