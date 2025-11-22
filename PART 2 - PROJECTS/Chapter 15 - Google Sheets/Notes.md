# EZSheets 

- Docs: https://github.com/AlSweigart/EZSheets
- needs to be installed `python -m pip install EZSheets`
- **Requires a setup** to obtain a **token** file from Google to access the API and to grant the API access to your account for Sheets and Drive

## Setting Up EZSheets

- Before your Python scripts can use EZSheets to access and edit your Google Sheets spreadsheets, you need a **credentials JSON file and two token JSON files.**
- Setup is as follows:
	1) Create a **new Google Cloud project**.
	2) Enable the Google **Sheets API and Google Drive API** for your project.
	3) Configure the **OAuth consent** screen.
	4) Create **credentials file**.
	5) **Log in** with the credentials file to generate **token files**.
- This setup needs to be done **only once per project.**

#### This setup UI has been slightly changed since the book was written, this is the updated way as of November 2025

### 1) Create New Google Cloud Project

 1) got to [Google Cloud Console](https://console.cloud.google.com/)
 2) Create a new project and give it a name (e.g. EZSheets)
	- Free Google accounts can have up to 12 projects but you only need 1 project for this setup

### 2) Enable APIs

1) Select the project you just created from the list of projects
2) Open the side menu -> Click on the **APIs & Services** -> Library
3) search for **Sheets API** or **Drive API**
4) Enable the API (click on the **Enable** button)
5) repeat for the other one

### 3) Enable OAuth Consent Screen

1) Open the **side menu** -> Click on the **APIs & Services** -> **OAuth** consent screen
2) Run the setup -> Click on the **Create** button and make it **External**
3) Click on the **Create** button

### 4) Select Scopes for each API

1) In the OAuth side menu, select the Data access page
2) Select "Add or remove scopes"
3) Select the **Sheets** `.../auth/spreadsheets` and **Drive** `.../auth/drive`scopes for your project
4) Click on the **Save** button and then again **Save**

### 5) Add Test User(s)

1) Open the side menu -> Click on the **APIs & Services** -> Audience
2) Click on the **+ Add users** button
3) Type in the google email address of a test user
4) Click on the **Save** button

### 6) Create Credentials .json file

1) Open the side menu -> Click on the **APIs & Services** -> Clients
2) Select **+Create Client**
3) Create access for Desktop application and name it whatever you want
4) Click on the **Save** button
5) Download the **credentials.json** file to a safe location
6) rename the file to something more simple to understand as the name of the file is long and hard to remember / understand

### 7) Generate token files

- Navigate to location of the .json file and run `import ezsheets`. 
	- EZSheets automatically checks the current working directory for the credentials JSON file by calling the `ezsheets.init() function`. 
- If the file is found, EZSheets launches your **web browser** to the **OAuth consent** screen to generate token files. 
- EZSheets also requires token files, named `token-drive.pickle` and `token-sheets .pickle`, along with the `credentials file` to access spreadsheets. 
	- Generating **token** files is a **one-time setup** step that won’t happen the next time you run `import ezsheets`.
	- Sign in with your test user account
	- You will receive a message "“Google hasn’t verified this app”" which you can ignore as it is not an actual app and you are the creator.
	- needs to be repeated for each API (in this case the Sheets and Drive APIs)
	- After closing the second window, you should now see token-drive.pickle and token-sheets.pickle files in the same folder as your credentials JSON file.
--- 

### Revoking the Credentials File

- If ever needed to delete the credentials you need to remove the link to them in console.
- In the [Google Console](https://console.developers.google.com/) go to credentials and click the **bin icon** to delete the credentials associated with the project. 
- This will revoke any connection between the **.json and token files** and the project. There is no need to delete the token files.