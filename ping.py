# Imports
from ping3 import ping, verbose_ping
#import ping3
#ping3.DEBUG = True
from console import console
from data import log_pingcheck

def startping_servers(servers):
    """Start the ping for all the servers in the list"""
    with console.status("[bold green]Working on server checks...") as status:

        for server in servers:
            if startping(server) == True:
                console.print("Server:", server["name"],"with ip:", server["ip"],"is online", ":white_heavy_check_mark:")
            else:
                console.print("Server:", server["name"],"with ip:", server["ip"],"is offline", ":x:")

def startping(server):
    """Try the ping test for 1 host"""
    res = ping(server["ip"])

    # timeout = res["timeout"]
    # is_alive = res["is_alive"]
    # rtt = res["rtt"]

    #info = {"timeout": timeout, "is_alive": is_alive, "rtt": rtt}

    log_pingcheck(server, bool(res))

    if res == False:
        return False
    else:
        return True
    
