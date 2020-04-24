# pythonWebserver.py

import http.server
import socketserver
import subprocess

def getWindowsIP():
    responseBytes = subprocess.check_output(['ipconfig'])
    responseArray = responseBytes.decode().split('\n')

    ethernet = False
    for line in responseArray:
        line = line.strip()
        if len(line) > 0:
            print(line)
            if 'Ethernet adapter' in line:
                ethernet = True
            if 'VirtualBox' in line:
                ethernet = False
            if 'IPv4' in line and ethernet == True:
                parts = line.split(':')
                return parts[1].strip()
            
    print("******* Could not find your local IP Address")
    return 'Unknown'

ipAddress = getWindowsIP()
PORT = 8081 
print('Browse: ' + ipAddress + ':' + str(PORT))

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
