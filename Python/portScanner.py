import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target = input('What website to scan: ')
openPorts = []
def pscan(port):
    try:
        con = s.connect((target, port))
        return True
    except:
        return False

for x in range(25):
    if pscan(x):
        openPorts.append(x)

print(openPorts)
