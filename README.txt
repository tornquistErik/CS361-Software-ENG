Includes 2 local server scripts written in python, the winforms application, and a simple file reading microservice
To run the main program, open powershell and cd into the "Main Program" directory with the project files. Run "python startscripts.py"
Will need .net framework installed

To run the file reading microservice, download the script "readFileData.py". Run "python readFileData.py [port]". If no port is specified the default port of 8095 will be used.

To use the microservice, open a socket connection to localhost at port 8095. Send an eight character hexadecimal message indicating the length of the main message. Then send the main message.
The server will respond with an 8 digit hexadecimal message, then the main data that was requested. See the implementation in "readFileDataTest.py" for more information

/uml.drawio.png
