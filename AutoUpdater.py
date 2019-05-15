import subprocess

DEBUG = True

try:
	subprocess.call("git pull", shell=True)
	if DEBUG:
		input()
	else:
		exit(0)

except Exception as e:
	print(f"ERROR (Fatal): {e}")
	input("Press any button to exit...")

