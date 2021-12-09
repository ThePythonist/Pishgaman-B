import os
command = input("Command : ")
os.system(f"start /B start cmd.exe @cmd /k {command}")
