import socket
import sys

IP, DPORT = 'localhost', 8095
CHUNK = 100

# Helper function that converts an integer into a string of 8 hexadecimal digits
# Assumption: integer fits in 8 hexadecimal digits
def to_hex(number):
    # Verify our assumption: error is printed and program exists if assumption is violated
    assert number <= 0xffffffff, "Number too large"
    return "{:08x}".format(number)

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


def send_long_message(conn, message):

    strlen = to_hex(len(message)).encode()
    conn.sendall(strlen)

    conn.sendall(message.encode())

def main():

    # Configure a socket object to use IPv4 and TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:

        # Connect to the server
        conn.connect((IP, int(DPORT)))

        long_msg = input("Please enter a message to send to the server: ")

        send_long_message(conn, long_msg)

        m = receive_long_message(conn)
        print("SERVER REPLIED: " + m)


    return 0

# Run the `main()` function
if __name__ == "__main__":
    if len(sys.argv) < 2:
        DPORT = sys.argv[1]
    main()
