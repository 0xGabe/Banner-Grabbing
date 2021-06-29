import sys,socket

def prPink(skk): print("\033[95m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m{}\033[00m" .format(skk))

prPink("""                                                         
 _______  _______  __    _  __    _  _______  ______          _______  __   __ 
|  _    ||   _   ||  |  | ||  |  | ||       ||    _ |        |       ||  | |  |
| |_|   ||  |_|  ||   |_| ||   |_| ||    ___||   | ||        |    _  ||  |_|  |
|       ||       ||       ||       ||   |___ |   |_||_       |   |_| ||       |
|  _   | |       ||  _    ||  _    ||    ___||    __  | ___  |    ___||_     _|
| |_|   ||   _   || | |   || | |   ||   |___ |   |  | ||   | |   |      |   |  
|_______||__| |__||_|  |__||_|  |__||_______||___|  |_||___| |___|      |___|            
""")

if len(sys.argv) != 3:
    prRed("[-] How to use -> python3 10.0.0.10 22")
else:
    ip = sys.argv[1]
    port = sys.argv[2]

    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.connect((ip,int(port)))
    banner = mysocket.recv(1024)

    prPurple("[i] Server Banner")
    print(banner)
