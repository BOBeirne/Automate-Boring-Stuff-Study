import subprocess
import time

print("--- Starting Notepad Test ---")

try:
# Let's try launching without the full path.
# Windows should find notepad.exe in its system PATH.
	print("Launching 'notepad'...")
	proc = subprocess.Popen(['notepad'])

	print(f"Subprocess object created: {proc}")
	print(f"Process ID (PID): {proc.pid}")

	# Let's wait a generous 5 seconds.
	# During this time, you should see a Notepad window appear and stay open.
	print("Waiting for 5 seconds...")
	time.sleep(5)

	# Now, let's check the status.
	poll_result = proc.poll()
	print(f"Result of proc.poll() after 5 seconds: {poll_result}")

	if poll_result is None:
		print("\nSUCCESS: poll() returned None, which means the process is still running.")
		print("This is the correct and expected behavior.")
		print("Terminating the process now...")
		proc.terminate()
	else:
		print(f"\nFAILURE: poll() returned an exit code ({poll_result}).")
		print("This means the process terminated almost immediately after launching.")

except FileNotFoundError:
	print("\nERROR: Could not find 'notepad'. This indicates a problem with your system's PATH environment variable.")
except Exception as e:
	print(f"\nAn unexpected error occurred: {e}")

print("--- Test Finished ---")