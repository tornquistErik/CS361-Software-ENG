import requests
import json
import socket

INTERFACE, SPORT = 'localhost', 8090
CHUNK = 100

def find_card(jsonFile, id):
    intid = int(id)
    for i in range(0, len(jsonFile)):
        if (jsonFile[i]["id"] == intid):
            return json.dumps(jsonFile[i], indent=2)
    return "NO CARD FOUND"
    
    

def receive_long_message(conn):
    data_length_hex = conn.recv(8, socket.MSG_WAITALL)

    data_length = int(data_length_hex, 16)

    data = b""
    full_data = b""
    bytes_received = 0

    while (bytes_received < data_length):
        data = conn.recv(CHUNK)
        full_data += data
        bytes_received += CHUNK

    return full_data.decode()

def main():
    f = open("save.json", "r+")

    jsonFile = json.loads(f.read())
    f.close()
    # Configure a socket object to use IPv4 and TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Set interface and port
        server_socket.bind((INTERFACE, int(SPORT)))

        # Start listening for client connections (allow up to 5 connections to queue up)
        server_socket.listen(5)
        while True:

            # Accept a connection from a client
            conn, (client_host, client_port) = server_socket.accept()
            print("Connection received from:", client_host, "on port", client_port)

            message = receive_long_message(conn)
        
            return_message = find_card(jsonFile, message)
            conn.sendall(return_message.encode())
            break

    conn.close()


# Run the `main()` function
if __name__ == "__main__":
    main()
