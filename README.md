# web application password Brute Forcing Tool

## Overview

This repository contains a solution for brute-forcing the magic number used in a server verification process. 
The objective is to send POST requests with all possible combinations of a 3-digit magic number and find the correct one that is accepted by the server.

## Solution Process

### Step 1: Problem Understanding

I was tasked with developing a tool that can help brute-force the correct "magic number" needed for server verification. 
The server verifies the magic number by accepting valid combinations and rejecting invalid ones with an error message. 
my goal was to identify the correct magic number by sending all possible combinations, from `000` to `999`.

### Step 2: Initial Approach

The initial approach was to use wireshark capturing the manual entering of pin in a browser 
and trying to send a POST request in postman for checking if the server has a reply
then basing it for our python script format request:
1. Create a POST request with a 3-digit number as the magic number.
2. Send this request to the server.
3. Check the server's response to determine whether the number was correct.

The response from the server would indicate whether the magic number was valid or not. 
If the response contained the message "Incorrect number," the script would try the next combination. 
If the response did not contain this message, the correct magic number was found.

### Step 3: Code Implementation

I implemented a basic script using the `socket` library to send raw HTTP POST requests to the server. 
The code iterated through all 1000 possible combinations (`000` to `999`) of 3-digit numbers and sent each one to the server. 

### Step 4: Improvements and Enhancements
# 4.1 Displaying Success or Failure
We improved the user experience by displaying clear messages when a combination succeeds or fails:

# 4.2 Adding Delay for Avoiding Server Overload
To prevent overwhelming the server with too many requests in a short period, we introduced a delay (sleep) between requests:
import time

### Step 5: Snoop Server Script
I developed an additional tool for cases where the user doesn't know the server address and port.
Note: if the user has access to turn on or off the server they can track it if a new port opens and is LISTENING running 
"netstat -ano | findstr LISTENING" in terminal before and after the server is run.
The tool processes netstat output to automatically detect open ports on the system (if the user doent want to type all the ports manually).
It then attempts to connect to each address and port, opening successful ones in a web browser automatically.

