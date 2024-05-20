import requests
import socket
import sys
from threading import Thread

INTERFACE, SPORT = 'localhost', 8095
CHUNK = 100

def readFromFile(fileName):
    f = open(fileName, "r+")
    return f.read()

# Helper function that converts an integer into a string of 8 hexadecimal digits
# Assumption: integer fits in 8 hexadecimal digits
def to_hex(number):
    # Verify our assumption: error is printed and program exists if assumption is violated
    assert number <= 0xffffffff, "Number too large"
    return "{:08x}".format(number)

def send_long_message(conn, message):
    strlen = to_hex(len(message)).encode()
    conn.sendall(strlen)

    conn.sendall(message.encode())

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

def accept_connection(conn):
    message = receive_long_message(conn)
    print(message)
    
    return_message = readFromFile(message)

    send_long_message(conn, return_message) 

def main():
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
            thread = Thread(target=accept_connection, args=[conn])
            thread.start()

    conn.close()


# Run the `main()` function
if __name__ == "__main__":
    if len(sys.argv) < 2:
        SPORT = sys.argv[1]
    main()
