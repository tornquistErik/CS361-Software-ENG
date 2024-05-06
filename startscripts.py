import os 
import subprocess

dir_path = os.path.dirname(os.path.realpath(__file__))

subprocess.Popen(['python','apiTest.py'])
print("API SERVER OPENED")
subprocess.Popen(['python','readCard.py'])
print("CARD SERVER OPENED")
subprocess.Popen(['WinformsApp1.exe'])
print("WINFORMS OPENED")