# Practice Questions

1.  When using the Gmail API, what are the **credentials** and **token** files?

credentials - `credentials.json`
token - `token.pickle`

2.  In the **Gmail API**, what’s the difference between **“thread”** and **“message”** objects?

- `Thread` is a collection of messages in a conversation
- `Message` is a single email

3.  Using `ezgmail.search()`, how can you find emails that have file attachments?

- You can use an argument `has_attachment=True`

4.  What are some of the disadvantages of using an SMS email gateway to send text messages?

There are many disadvantages:
- It is not a very robust solution, sometimes it works and sometimes it doesn't
- There is no way to know if text arrived or not
- There is no way of knowing how fast text arrives
- Recipient has no way of replying
- You may get blocked if you send too many emails, and there is no way of knowing the limit

5.  What Python library can send and receive notifications to ntfy?

`requests` module