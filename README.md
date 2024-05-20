Includes 2 local server scripts written in python, the winforms application, and a simple file reading microservice
To run the main program, open powershell and cd into the "Main Program" directory with the project files. Run "python startscripts.py"
Will need .net framework installed

To run the file reading microservice, download the script "readFileData.py". Run "python readFileData.py [port]". If no port is specified the default port of 8095 will be used.

To use the microservice, open a socket connection to localhost at port 8095. Send an eight character hexadecimal message indicating the length of the main message. Then send the main message.
The server will respond with an 8 digit hexadecimal message, then the main data that was requested. See the implementation in "readFileDataTest.py" for more information

Example call: 

    def to_hex(number):
        # Verify our assumption: error is printed and program exists if assumption is violated
        assert number <= 0xffffffff, "Number too large"
        return "{:08x}".format(number)
        
     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
        # Connect to the server
        conn.connect((IP, int(DPORT)))
       
        message = !!!!MESSAGE HERE!!!!
        strlen = to_hex(len(message)).encode()
        conn.sendall(strlen)
      
        conn.sendall(message.encode())

        data_length_hex = conn.recv(8, socket.MSG_WAITALL)
        
        data_length = int(data_length_hex, 16)
        
        data = b""
        full_data = b""
        bytes_received = 0
        
        while (bytes_received < data_length):
            data = conn.recv(CHUNK)
            full_data += data
            bytes_received += CHUNK
        
        returnedData = full_data.decode()

![Microservice UML diagram](https://github.com/tornquistErik/CS361-Software-ENG/blob/main/UML.drawio.png?raw=true)
