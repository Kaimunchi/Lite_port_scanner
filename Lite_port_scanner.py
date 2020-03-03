import socket
import sys
from datetime import datetime
remoteserver = input("enter the remote host to scan:")
remoteserverip = socket.gethostbyname(remoteserver)
print("-"*60)
print("pls wait sir,scanning remote host",remoteserverip)
print("-"*60)
t1=datetime.now()
#print(t1)
try:
    for port in range(1,1025):
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result=sock.connect_ex((remoteserverip,port))
        if result == 0:
            print("port{}: open".format(port))
        sock.close()
except KeyboardInterrupt:
    print("you pressed ctrl+c")
    sys.exit()

except socket.gaierror:
    print("hostname could not be resoved .Exiting")
    sys.exit()
except socket.error:
    print("cant connect to server")
    sys.exit()
t2=datetime.now()
total=t2-t1
print("scanning completed in",total)

