- Deployment - making software usable outside of code editors
- Program - complete piece of software with instructions that computer carries out
- Script - program that interpreter runs from source code rather than compiled form
- Command - program often run from CLI, no GUI. Config is done up front with arguments
- Shell Script - single txt file that runs bundled up CLI commands in one batch
	- .sh - Linux & MacOS
	- .bat - Windows
- Application - program that has GUI. Usually have several files that installer sets up.
- App - commonly used for mobile application but can also be installed on computer
- WebApp - Program that runs on web server interacted with via a a web browser

## [[CLI]] - Command Line Interface

### Accessing CLI

#### Windows
- Start / Windows Key -> enter command prompt / Powershell / Terminal
- commands display '>' sign as a prompt
- `> python` to run python environment 

#### Linux
- Windows Key -> terminal / use shortcut CTRL + ALT + T
- commands display '$' sign as a prompt
- `$ python3` to run python environment 

#### macOS
- Spotlight icon (or press mac + spacebar) -> terminal
- commands display '%' sign as a prompt
- `% python3` to run python environment 

### Running programs via CLI

While in the CLI you can run program files by entering:

- **Absolute path** - you can enter for example c:\user\dodo\pythonprograms\projectfile.py 
- **Relative Path** - like projectfile.py **if your CWD is where project file is**
	- Windows - enter name of program **with or without `.exe`** extension. for example `project.exe`
	- Linux and macOs - you **must enter ./** followed program name. For example `./project.exe`

### cd, pwd, dir and ls

- cd - is used to navigate directories
	-  cd absolute\path - will change cwd to that location
	-  cd \foldername\ - will navigate to that folder in the current directory (if it exists) 
	-  cd .. - goes one directory up
	-  cd D: - will change location to specified drive 
- dir / ls
	- Windows - uses dir to list contents of CWD
	- macOS and Linux use ls
	- you can filter for specified arguments by using:
		- `dir *.exe` on Windows
		- `file * | grep` on Linux

### [[PATH]] Environment Variable

The **PATH** is one of the most fundamental environment variables in any operating system, whether it's Windows, macOS, or Linux.
It allows you to run widely-used system utilities (like `ipconfig` or `powershell`) from _any_ location on your disk without having to type the full, absolute file path every single time (e.g., `C:\Windows\System32\ipconfig.exe`).
Adding installation folders for scripting languages like Python to the PATH makes those tools instantly accessible from any shell window.

PATH behaviour is slightly different for each OS:
- Windows - first check CWD for program of that name, then the PATH
	- To see the contents of PATH, run `echo %PATH%`
	- The value of PATH is **long string composed of folder names and separated by semicolons**
- macOS & Linux - check only PATH (does not check CWD at all)
	- To see the contents of PATH, run `echo $PATH`
	- PATH values are **separated by colons**

#### PATH editing

It is recommended to keep all your scripts in your **home folder**:

- Windows - **C:\Users\al\Scripts** 
- macOS - **/Users/al/scripts**
- Linux - **/home/al/Scripts**

Adding "Scripts" folder to PATH

##### Windows:

- 2 sets of PATH environments:
	- Users - overrides the system variables but apply to current user only
	- System
- You can edit them by going to Start -> Edit Environment Variables -> User / System -> Edit -> Add a path for script -> OK

##### macOS & Linux:
- To add new entries to PATH variable you need to edit the terminal start-up script.
- Files are located in the Home folder. To add new entry simply add following to the bottom of the file:
	- macOS - **.zshrc** - `export PATH=/Users/al/Scrips:$PATH`
	- Linux - **.bashrc** - `export PATH=/home/al/Scrips:$PATH`

#### Which and Where

To find out location of the PATH variable you can use:
Windows - **Where** `C:\Users\Al>`
macOs and Linux - **Which** `al@Als-McBook Pro ~ % which python3`


### Virtual Environments (venv)

- Python can create it's own virtual environments with venv module
- Separate installations of Python that have their own set of installed 3-rd party packages.
- Solution to multiple programs using different Python versions to avoid reinstalling Python.
- Each Python application you create needs it's own virtual environment but for small scripts you can just run them on one venv
- Virtual Environments in Python will be fresh installs with only default packages 
	- `python -m pip list` to confirm

#### Creating Virtual Environment ([[venv]])

`cd` to `\Scripts` folder and run `python -m venv .venv`

This will create venv files in `.venv` folder

#### Activating Virtual Environment

To actually use the virtual environment version of Python you need to activate it using **activate.bat** file in **.venv\Scripts** folder

##### Windows:

`cd .venv\Scripts`
`activate.bat`
to confirm you're running the correct environment use where command:
`where python.exe`

##### Linux

macOs and Linux require slightly different approach due to security issues

`cd .venv\bin`
`source activate`
`which python3` to confirm version

### [[pip]] - pip installs package

- Help file: `-m pip --help`
- Every installation of Python comes with pre-installed, default modules:
	- sys, random, os
- Additional packages can be found in [Python Package Index aka PyPI ](https://pypi.org)

##### DO NOT USE PIP WITH ANACONDA

#### Installing packages using pip from [[PyPI]]

Use `-m` flag to ensure pip is ran as a module to:
- Avoid Shell PATH issues (if pip is not directly available in PATH)
- Ensures correct python's pip version is used (different versions for different pythons)
`python -m pip install package_name`

#### Uninstalling packages

```
python -m pip uninstall package_name
```

#### Listing installed pip modules

`python -m -pip list`

#### Checking if module is installed

Al advises to use the try block and try to catch an exception

```python
try:
	import NonExistingModule
except ModuleNotFoundError:
	print("Module not found") # this gives user more descriptive error
	sys.exit()
```

You can alternatively use `python -m pip show package_name`

#### Updating packages

`-m pip install -U package_name`
- U stands for update
- You can also specify a package version by adding `package==version`

#### Built-in variables

Several built-in variables can give your Python program useful info about itself:
- the OS it's on
- Python interpreter version
- `__file__` variable, which contains .py file's path as a str
	- can be used to find out where the program is running from by using:
	- `Path(__file__)` will return Path object of this file
- `sys.executable` will return full path to Python interpreter program itself
- `sys.version` will return Python interpreter version
- `sys.versioninfo.major` and `sys.versioninfo.minor` will return major and minor versions of Python interpreter (eg. 3.13.1 -> major = 3, minor = 13)
- `os.name` Will return `nt` for Windows or `posix` for macOS and Linux
- `sys.platform` will return `win32` for Windows or `darwin` for macOS or `linux` for Linux

#### Installing the "Automate the boring stuff" package

- Windows:
`python -m pip install AutomateTheBoringStuff3`
- macOS and Linux:
`python3 -m pip install AutomateTheBoringStuff3`

### Text-Based program design ([[TUI]])

In this book we are focusing on building small programs not using GUI, however we can still provide something similar using TUI (Text User Interface)

They are quite simple to make

#### Short command names

- TUI is usually run by text commands
- These commands are usually short and easy to remember like `ls` or `cd` and are usually shortened versions of longer commands like `list` or `change directory`

#### Command-line Arguments

To run a program from CLI simply enter it's name (like `python` on windows) and then the filename like `project.py`
After the command you supply arguments
- `ls` - lists contents of current directory but can also specify a specific folder to list contents of
- `sys.argv` list contains all arguments passed to the program and Python scripts can access that list
	- for example: if you enter `python script.py hello world` the sys.argv list will contain `['script.py', 'hello', 'world']`
	- This can be used to specify a wide range of configurations before the program even runs
	- You can also use `argparse module` in complicated situations when using many arguments 
- passing following after the command: `\?` on Windows and `--help` on Linux and macOS will print help text for the program
- a lot of programs accept `-v` or `--verbose` for verbose mode (more text output)
- a lot of programs also accept `-q` or `--quiet` for quiet mode (no text output, sound or notifications)

### Clipboard I/O

You don't need to rely on the input() to read text from files or keyboard, you can instead use **pyperclip module** to read text from clipboard

```python
import pyperclip # import the module
text = pyperclip.paste() # obtain the input text from the clipboard
# do some operations on the text here
pyperclip.copy(text) # copy the input text back to the clipboard
```

More info in the [pyperclip documentation](https://pypi.org/project/pyperclip/)
Project in MOD 8 was using pyperclip 

### Colorful text using Bext

- Needs to be installed first
- Only works on programs run from Terminal
- use fg() for foreground and bg() for background to change colors
	- they take RGB and string arguments such as: `fg(255, 0, 0)` for red or 'yellow', 'blue' etc
- use clear() to clear the screen

Bext also has some TUI-like features:
- bext.clear() - clears the screen
- bext.width() and bext.height() - get the width and height of the terminal
- bext.hide() and bext.show() - hide and show the cursor
- bext.title() - set the title of the terminal window
- bext.goto(x, y) - move the cursor to the specified position
- bext.get_key() - get a key press from the user and then return a string representation of the key
	- examples of keys returned include 'a', 'z' and 5' but also 'left' 'f1' and 
	- 'esc' TAB and Enter return '\t' and '\n' respectively

Example of ASCII fish-tank program by Al featured in his other book "book of small python projects" - https://inventwithpython.com/projects/fishtank.py

### Clearing the Terminal

bext.clear() is useful if you want to remove any text from before it ran

```python
import bext
bext.clear()
```

You can also use non-bext "one-liner" script:

```python
import os
def clear():
	os.system('cls' if os.name == 'nt' else 'clear')
```

This only works in terminal (not code editors)
`cls` is a clear program on Windows and `clear` is a clear program on Linux

##### one-liners are usually avoided because they are difficult to read and debug

### Sound and text notifications

- Easy to overuse just like colorful text

#### Playsound3

- can be used to play single audio files using playsound() function and passing it path to a file
- accepts .mp3 and .wav

Example:

- Download hello.mp3 from [here](https://autbor.com/hellp.mp3) and run the following:

```python
import playsound3
playsound3.playsound('hello.mp3')
```

- `Playsound()` function won't return until the audio file stops playing - blocks until it finished
- If it raises an exception it may be caused by odd character in file name, to avoid this pass it a `Path object`
- if program is running in quiet mode you can use `--beep` or `-b` to play a sound or alert beeps

### PyMsgBox

- Instead of using full GUI toolkit like **Tkinter, wxPython, PyQt or PySimpleGUI** you can use `PyMsgBox` module to display a message box
- if you only require occasional notifications or input it can be a suitable replacement for print() and input()
- Needs to be installed with pip
	- On macOS and Linux you first need to install it on OS by running `sudo apt install python3-tk`

- PyMsgBox functions mirror JS message box functions
	- pymsgbox.alert(text) - displays a message box with OK button, pressing it returns a str of value 'ok'
	- pymsgbox.confirm(text) - displays a message box with OK and Cancel buttons and returns a str of value 'ok' or 'cancel'
	- pymsgbox.prompt(text) - displays a message along with a field text. returns text user entered as str or None if they cancelled
	- pymsgbox.password(text) - same as prompt but text user enters is masked with asterisks

### Deploying Python Programs

- First make sure your [[PATH]] environment variable is set correctly with `Scripts` folder
- You will also need to create a virtual environment with [[venv]]

#### Windows

1. Place the program.py into `Scripts` folder
2. Create a program.bat file in `Scripts` folder to run the Python script with the following content:
	```bat
	@call %HOMEDRIVE%%HOMEPATH%\Scripts\.venv\Scripts\activate.bat REM activate venv
	@python %HOMEDRIVE%%HOMEPATH%%\Scripts\program.py %* REM run python.exe which then runs the program. %* is added to forward any additional arguments
	@pause REM wait for user to press enter, prevents window from closing prematurely
	@deactivate REM deactivates venv in case windo remained open after running the program
	```
3. Press `Win+R` key will bring up the Run dialog window
4. Type `program` and press enter
	- you can optionally add any additional arguments to run the program with

#### macOS

1. Place the program.py into `Scripts` folder
2. create a text file named `program.command` to run the Python script.
	```bash
	source ~/Scripts/.venv/bin/activate # activate venv
	python3 ~/Scripts/program.py # run python.exe which then runs the program
	deactivate # deactivates venv
	```
3. Run `chmod u_x program.command` to add execute permissions to the file
4. press COMMAND + spacebar -> spotlight -> enter name of the program to run

##### macOs Spotlight has no way of passing arguments to the program. They need to be defined in a .command file

#### Linux

Ubuntu linux Dash search can be brought up by pressing windows key and entering the name of the program you want to run 

1. Place the program.py into `Scripts` folder
2. create a text file named `program.sh` to run the Python script.
	```bash
	source ~/Scripts/.venv/bin/activate # activate venv
	python3 ~/Scripts/program.py # run python.exe which then runs the program
	read -p "press any key to continue...." # wait for user to press enter, prevents window from closing prematurely
	deactivate # deactivates venv
	```
3. Run `chmod u+x program.sh` to add execute permissions to the file
4. create `program.desktop` file in `~/.local/share/applications` folder to add the program to the menu
	```bash
	[Desktop Entry]
	Name=Program 
	Exec=gnome-terminal -- /home/al/Scripts/program.py # the path need to be full path
	Type=Application 
	```

