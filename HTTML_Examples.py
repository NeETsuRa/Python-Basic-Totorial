import socket

#Working with sockets
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)
server = 'pythonprogramming.net'
port = 80
# Get info from an server
server_ip = socket.gethostbyname(server)
print(server_ip)

request = "GET / HTTP/1.1\nHost: "+server+"\n\n"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("pythonprogramming.net", 80))
# http request to an server
s.send(request.encode())
result = s.recv(4096)

#print(result)
while (len(result) > 0):
    print(result)
    result = s.recv(4096)

# Port scaner of an web site
#target = input('What website to scan?: ')
target = 'https://www.hackthissite.org/'
def pscan(port):
    try:
        con = s.connect((target,port))
        return True
    except:
        return False


for x in range(25):
    if pscan(x):
        print('Port',x,'is open')	

# How to execute code provided as Text.
exec("def test(): print('oooo snap!!!')")
test()