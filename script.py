import socket

# Define the server address and port
HOST = '127.0.0.1'  
PORT = 8888         

# Function to send a single POST request with a static pin
def send_single_request():
    pin = "123"  # Hardcoded pin for now

    # Create a very basic POST request
    request = (
        "POST /verify HTTP/1.1\r\n"
        f"Host: {HOST}:{PORT}\r\n"
        "Content-Type: application/x-www-form-urlencoded\r\n"
        f"Content-Length: {len('magicNumber=' + pin)}\r\n"
        "\r\n"
        f"magicNumber={pin}\r\n"
    )

    # Create socket connection
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(request.encode())
        response = s.recv(4096).decode()
        print(response)

# Run the single request
send_single_request()
