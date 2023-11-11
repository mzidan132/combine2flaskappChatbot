import subprocess

# Create and start the processes
proc1 = subprocess.Popen(['python', 'apps.py'])
proc2 = subprocess.Popen(['python', 'app.py'])


# Wait for the processes to finish
proc1.wait()
proc2.wait()

