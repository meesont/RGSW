import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# target = input('What website to scan: ')

target = 'https://www.hackthissite.org/'
openPorts = []
def pscan(port):
    try:
        con = s.connect((target, port))
        return True
        con.close()
    except:
        return False

for x in range(25):
    if pscan(x):
        print(x);

print(openPorts)
