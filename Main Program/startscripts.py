import os 
import subprocess

subprocess.Popen(['python','apiTest.py'])
print("API SERVER OPENED")
subprocess.Popen(['python','readCard.py'])
print("CARD SERVER OPENED")
subprocess.Popen(['WinformsApp1.exe'])
print("WINFORMS OPENED")