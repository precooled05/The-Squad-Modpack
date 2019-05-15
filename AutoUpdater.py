import subprocess

DEBUG = True
<<<<<<< HEAD
=======

>>>>>>> cd20e77575eba2c1c353a6b583b27ab06b770ebe
try:
	subprocess.call("git pull", shell=True)
	if DEBUG:
		input()
	else:
		exit(0)

except Exception as e:
	print(f"ERROR (Fatal): {e}")
	input("Press any button to exit...")

