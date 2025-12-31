# EZGMail module

- **Written by** man himself - **Al Sweigart** 
- [Documentation](https://github.com/asweigart/ezgmail)
- helps with **automating email tasks**
- It is highly recommended to have a **test email account** for API testing
- It is also recommended to **"dry run" your code before sending emails**
- To **install the module** use `pip -m install ezgmail`
- To check, for **which e-mail address does `token.json` belongs to**, use `ezgmail.EMAIL_ADDRESS`

## Gmail API

- require to use `ezgmail` module
- Identical instructions to [[EZSheets]] module
- To activate the `credentials.json` run `ezgmail.init()` in the python console after importing the module and authenticate your account


## Sending e-mail

- to send an email, use a simple function:

```python
import ezgmail
ezgmail.send('recipient@mail.com', 'subject', 'Body of email')
```

### Attaching files to the emails

- to add an attachment add a 4th argument as a list of files names

```python
import ezgmail
ezgmail.send('recipient@mail.com', 'subject', 'Body of email', ['file1.txt', 'file2.txt'])
```

## CC and BCC

- `CC` stand for `carbon copy` is simply an email **address you send a copy of email to**
  - To add a person to CC, add it as an **attribute** of the `.send() function` in the following format: `cc='friend@example.com'`
- `BCC` stands for `blind - carbon copy` - it's the **same as a CC, but the receiver do not get visibility of who else was the email sent to**
  - To add a person to BCC, add it as an **attribute** of the `.send() function` in the following format: `bcc='otherfriend@example.com'`


## Automatic Spam filter

- As **part of security and anti-spam features** Gmail may **not send repeated email with same text**
- It may also **filter out** emails containing `.zip` or `.exe` files


## Reading e-mails

- EZGmail has `GmailThread` and `GmailMessage` objects to represents a conversation threads and individual e-mails respectively
  - `GmailThread object` has `messages attribute`, It holds a list of `GmailMessage objects`
  - Use the `unread()` function to get **25 most recent UNREAD emails** as a **list of `GmailThread objects`**
  - Use the `recent()` function to get 25 most recent threads as a list of `GmailThread objects`
  - To change the number of returned results, pass the attribute with the integer nr of results to `maxResults=50` for example to return 50 messages
    - That list can be passed to `ezgmail.summary` to print out a summary of the conversation threads in that list

### .unread()

```python
import ezgmail
unread_threads = ezgmail.unread() # return a list of GmailThread objects

# ---------------------------
len(unread_threads)
# 4 <- how many threads are unread
str(unread_threads[0])
# "<GmailThread numMessages=1 snippet='2-Step Verification turned on babalablabs@gmail.com Your Google Account babalablabs@gmail.com is now protected with 2-Step Verification. When you sign in on a new or untrusted device, you&#39;ll need'>"

# ---------------------------
str(unread_threads[3])
# "<GmailThread numMessages=1 snippet='Hi Babalablabs, Welcome to Google. Your new account comes with access to Google products, apps and services. Confirm your options are right for you Review and change your privacy and security options.'>"
len(unread_threads[3].messages)
# 1 <- how many messages are in the thread
str(unread_threads[3].messages[0])
# "<GmailMessage from='Google <no-reply@google.com>' to='babalablabs@gmail.com' timestamp=datetime.datetime(2025, 11, 22, 10, 27, 50) subject='Information about your new Google Account' snippet='Hi Babalablabs, Welcome to Google. Your new account comes with access to Google products, apps and services. Confirm your options are right for you Review and change your privacy and security options.'>"
str(unread_threads[3].messages[0].subject)
# 'Information about your new Google Account' <- E-mail subject
str(unread_threads[3].messages[0].body)
# 'Hi Babalablabs,\r\nWelcome to Google. Your new account comes with access to Google products,  \r\napps and services.\r\n\r\nConfirm your options are right for you\r\n\r\nReview and change your privacy and security options.\r\n\r\nConfirm  \r\n<https://c.gle/APy2Ad1glcY0-13Sxawr91UbIv1 (...) r\nlikely has the answer you\'re looking for.\r\n\r\nGoogle Ireland Ltd, Gordon House, Barrow Street, Dublin 4, Ireland.\r\n1800710212\r\nsupport-eu@google.com\r\n\r\nThis email was sent to you because you created a Google Account.\r\n' <- body of the email
str(unread_threads[3].messages[0].timestamp)
# '2025-11-22 10:27:50'
str(unread_threads[3].messages[0].sender)
# 'Google <no-reply@google.com>'
str(unread_threads[3].messages[0].recipient)
# 'babalablabs@gmail.com'
```

### .summary()

```python
import ezgmail
unread_threads = ezgmail.unread() 
ezgmail.summary(unread_threads) # print out a summary of the conversation threads
# Google - 2-Step Verification turned on babalablabs@gmail.com Your Google Account babalablabs@gmail.com is now protected with 2-Step Verification. When you sign in on a new or untrusted device, you&#39;ll need - Dec 30
# Google, Google, Google, Google, Google - New passkey added to your account babalablabs@gmail.com If you didn&#39;t add a passkey, someone might be using your account. Check and secure your account now. Check activity You can also see security - Dec 30
# Google - Hi Babalablabs, we updated your settings babalablabs@gmail.com Google couldn&#39;t confirm that you&#39;re an adult, so some account settings have changed Try it out SafeSearch is on Google may hide - Dec 04
# Google - Hi Babalablabs, Welcome to Google. Your new account comes with access to Google products, apps and services. Confirm your options are right for you Review and change your privacy and security options. - Nov 22
```

### .recent()

- `ezgmail.recent()` function will return the **25 most recent threads** in your Gmail account
- Works very similarly to `.unread()`
- To change the number of returned results, pass the attribute with the integer nr of results to `maxResults=50` for example to return 50 messages

```python
import ezgmail
recent_threads = ezgmail.recent()
ezgmail.summary(recent_threads) # print out a summary of the conversation threads
#Google - 2-Step Verification turned on babalablabs@gmail.com Your Google Account babalablabs@gmail.com is now protected with 2-Step Verification. When you sign in on a new or untrusted device, you&#39;ll need - Dec 30
#Help - Google Account community Hi Babalablabs, Your question has been posted to the Google Account Community. Most questions receive a reply within 24 hours. We&#39;ll send you an email notification when - Dec 30
#Google, Google, Google, Google, Google - New passkey added to your account babalablabs@gmail.com If you didn&#39;t add a passkey, someone might be using your account. Check and secure your account now. Check activity You can also see security - Dec 30
#Reddit - Enter your verification code to finish signing up. ##### If you didn&#39;t make this request, you can ignore this email and carry on as usual. If you need any more help logging in to your Reddit - Dec 12
#Google - Hi Babalablabs, we updated your settings babalablabs@gmail.com Google couldn&#39;t confirm that you&#39;re an adult, so some account settings have changed Try it out SafeSearch is on Google may hide - Dec 04
#Google - Hi Babalablabs, Welcome to Google. Your new account comes with access to Google products, apps and services. Confirm your options are right for you Review and change your privacy and security options. - Nov 22

len(recent_threads)
# 6
```

## Searching e-mails

- EZGmail has a `search()` function to search for e-mails
- You can use special search operators to search for specific e-mails
  - 'label:UNREAD' - Unread emails
  - 'from:email@address.com' - filter by e-mail address
  - 'to:email@address.com' - filter by e-mail address
  - 'subject:subjectbody' - filter by subject
  - 'has:attachment' - filter for e-mails with attachments
  - [full list of operators here](https://support.google.com/mail/answer/7190)

## Downloading Attachments

- `GmailMessage object` has `attachments` attribute which is a **list of filenames** if attached to the email
- You can pass them to `.downloadAttachment()` method to download **single file** or use `.downloadAllAttachments()` to **download all of them at once**
- You can also **specify a folder name for all the attachments to put into** by passing an attribute `downloadFolder='FolderName'` to the `.downloadAllAttachments()` method, as EZGmail by default downloads all to cwd
- Keep in mind if the file of the same name already exists it will be overwritten by default

```python
import ezgmail
threads = ezgmail.search('vacation photos')
threads[0].messages[0].attachments # Get the list of all attachments in the first thread in the first message
# ['vacation1.jpg', 'vacation2.jpg', 'vacation3.jpg'] (example)
threads[0].messages[0].downloadAttachment('vacation1.jpg') # Download the first attachment
threads[0].messages[0].downloadAllAttachments(downloadFolder='vacation2026') # download all attachments and save them into the folder
# ['vacation1.jpg', 'vacation2.jpg', 'vacation3.jpg']