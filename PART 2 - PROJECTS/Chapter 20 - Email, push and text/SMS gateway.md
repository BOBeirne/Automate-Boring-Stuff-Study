# SMS Email Gateways

- You can **send SMS messages using an email gateway**
- You can write a program to send these emails using `EZGmail` or the `smtplib` module.
- **some** providers offer this service for **free**
- Usually, **the phone number and phone company’s email server make up the recipient email address** - eg. `2125551234@vtext.com`
- `SMS` has usually **limit of 160 chars**
- `MMS` has **no character limit, you can also attach files**
- **Many CONS:**
  - It is not a very robust solution, sometimes it works and sometimes it doesn't
  - There is no way to know if text arrived or not
  - There is no way of knowing how fast text arrives
  - Recipient has no way of replying
  - You may get blocked if you send too many emails, and there is no way of knowing the limit