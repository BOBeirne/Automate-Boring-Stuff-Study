# Subprocess module

## run() function


- `run()` is a built-in function in the `subprocess module` 
- It allows you to run a program in a separate process
- You can also use it to run external programs from Python's script
- `run()` function blocks until the program finishes, it will be run as separate process to the Python's program

**Example using...**
**Windows calculator:**
```python
import subprocess
subprocess.run(['C:\\Windows\\System32\\calc.exe']) # pass it path to the .exe file
# CompletedProcess(args=['C:\\Windows\\System32\\calc.exe'], returncode=0)
```

**Linux calculator**
```python
import subprocess
subprocess.run(['/usr/bin/gnome-calculator'])
# CompletedProcess(args=['/usr/bin/gnome-calculator'], returncode=0)
```

**macOS calculator**
```python
import subprocess
subprocess.run(['open', '/System/Applications/Calculator.app']) # notice you need to pass open as first argument
# CompletedProcess(args=['open', '/System/Applications/Calculator.app'], returncode=0)
```

- You can also run music files:

```python
import subprocess
subprocess.run(['start', 'alarm.wav'], shell=True) # Windows
#subprocess.run(['open', 'alarm.wav'])  # macOS and Linux
```

to see application in more detail see `simpleCountdown.py` in Programs folder


### .Popen()

- Short for "process open"
- It allows you to run a program in a separate process but do not require you to wait for it to close to continue the program
- return value of this function is a `Popen object`
  - you can use this object to control the process
  - It has 2 methods: `poll()` and `wait()`

```python
import subprocess
calc_proc = subprocess.Popen(['C:\\Windows\\System32\\calc.exe'])
```

#### poll()

- It checks if the process is **still running**, and returns `None` if it is
- If the checked program is **closed** it will return the integer `exit code` of the program
  - code 0 means there were no errors
  - code (usually) 1 means there were errors
  - it can also return other error int depending on specific program

#### wait()

- This method will block the program until the process finishes
- The return value of this method is the `exit code` of the process
- If the process is still running, it will return `None`
- Make sure to run following code as `.py` file, as the python console does not show correct information.

```python
import subprocess
calc_process = subprocess.Popen(['c:\\Windows\\System32\\calc.exe'])
calc_process.poll() == None
# True
calc_process.wait() # Doesn't return until Calculator closes
# 0
calc_process.poll()
# 0
```

