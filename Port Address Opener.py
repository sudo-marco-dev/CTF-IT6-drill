import webbrowser
import socket

# Main function to process the user input and try connecting
def open_server():
    # Ask the user to paste the command output from netstat (addresses and ports)
    print("Please paste the netstat output with the LISTENING ports (press Enter twice to end the input):")

    cmd_output = []
    try:
        while True:
            line = input()  # Read input line by line
            if line == '':  # Stop when the user presses Enter without typing anything
                break
            cmd_output.append(line)
    except KeyboardInterrupt:
        print("\nInput reading stopped by user.")
    
    # Process the multi-line input
    for line in cmd_output:
        try:
            # Ignore lines that don't have a valid address:port format
            parts = line.split()

            if len(parts) < 2:  # Ensure that there's at least address and port
                continue

            # Extract address and port from the part that contains the address:port format
            address_and_port = parts[1]  # The second part is usually address:port

            if ":" not in address_and_port:  # Skip if there's no port in the address
                continue

            address = address_and_port.split(":")[0]  # Get the address before the ":"
            port = int(address_and_port.split(":")[1])  # Get the port number after the ":"

            # Try connecting and open the address in a browser
            if address in ["0.0.0.0", "[::]"]:
                address = "127.0.0.1"  # Replace with localhost if address is 0.0.0.0 or [::]
            
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(3)  # Set a timeout for the connection
                s.connect((address, port))  # Try connecting
                print(f"✔️ Successfully connected to {address}:{port}")
                webbrowser.open(f"http://{address}:{port}")  # Open in the browser

        except Exception as e:
            print(f"❌ Error processing line: '{line}' - {e}")
            continue  # Skip the problematic line and move to the next one

if __name__ == "__main__":
    open_server()
