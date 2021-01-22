# MiniSpy
Introduction:
An alternate Python payload for Rapid 7's Metasploit Python Payload (https://www.rapid7.com/).
It is combined with the custom listener for controlling this payload.
For a simple introduction about what a payload and listener is go to
https://us.norton.com/internetsecurity-malware-what-is-a-trojan.html
This is based off of Remote Access Trojan & Backdoor Trojan.
The purpose of this project is to understand and create effective trojans.
This will not be a 100% FUD (Fully UnDetectable) by any means.
This is just supposed to provide an alternative for Pen Testers
(https://www.cyberdegrees.org/jobs/penetration-tester/). The way this program works is
the payload will try to bind to the listener. Then backdoor access will provide access to the
CMD (Command Prompt) or the Terminal based on the operating system. The installer will
put the payload onto the startup file of windows (Linux not supported) so after reboot
the program will provide a persistent backdoor. All of the programs (except MiniSpy_Listener.py)
will be turned into an EXE with Pyinstaller (https://www.pyinstaller.org/) for easy exploitation.
