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

## CLI - Command Line Interface

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

### PATH Environment Variable

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

#### Creating Virtual Environment

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

### pip - pip installs package

- Help file: `-m pip --help`
- Every installation of Python comes with pre-installed, default modules:
	- sys, random, os
- Additional packages can be found in [Python Package Index aka PyPI ](https://pypi.org)
##### DO NOT USE PIP WITH ANACONDA

#### Installing packages using PyPI

Use `-m` flag to ensure pip is ran as a module to:
- Avoid Shell PATH issues (if pip is not directly available in PATH)
- Ensures correct python's pip version is used (different versions for different pythons)
`python -m pip install package_name`

#### Uninstalling packages

``
#### Listing installed pip modules

`python -m -pip list`

#### Updating packages

`-m pip install -U package_name`

You can also specify a package version by adding `package==version`

