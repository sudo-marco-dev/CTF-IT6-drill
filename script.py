import socket

# Define server address and port
HOST = '127.0.0.1'
PORT = 8888

# Function to send POST request with given pin
def send_request(pin):
    request = (
        f"POST /verify HTTP/1.1\r\n"
        f"Host: {HOST}:{PORT}\r\n"
        f"Connection: close\r\n"
        f"Content-Length: {len('magicNumber=' + pin)}\r\n"
        f"Content-Type: application/x-www-form-urlencoded\r\n"
        f"\r\n"
        f"magicNumber={pin}\r\n"
    )

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(request.encode())
        response = s.recv(4096).decode()
        
    return response

# Send a single PIN and print clear result
def try_pin(pin):
    response = send_request(pin)
    if "Incorrect number" in response:
        print(f"PIN {pin}: ❌ Incorrect")
    else:
        print(f"PIN {pin}: ✅ Success!")

# Example usage
try_pin("123")
