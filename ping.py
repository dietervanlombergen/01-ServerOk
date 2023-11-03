# Imports
from ping3 import ping

def startping(host):
    
    res = ping(host)

    if res == False:
        return False
    else:
        return True
    
