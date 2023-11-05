# Imports
from ping3 import ping # Ping functions
from console import console # Console to use
from console import getTable
from rich.live import Live
from data import log_entry # To add log entry





def startping_servers(servers):
    """Start the ping for all the servers in the list"""
    with console.status("[bold green]Working on server checks...") as status:

        # for server in servers:
        #     if startping(server) == True:
        #         console.print("Server:", server["name"],"with ip:", server["ip"],"is online", ":white_heavy_check_mark:")
        #     else:
        #         console.print("Server:", server["name"],"with ip:", server["ip"],"is offline", ":x:")

        # TRY TABLES
        ping_table = getTable()
        ping_table.title = "Ping results"
        ping_table.add_column("Server")
        ping_table.add_column("Ip")
        ping_table.add_column("Status")

        with Live(ping_table, refresh_per_second=4) as live:
            for server in servers:
                if startping(server) == True:
                    ping_table.add_row(server["name"], server["ip"], "[green]Online")
                else:
                    ping_table.add_row(server["name"], server["ip"], "[red]Offline")

        console.print("[green]All servers are tested", ":tada:")

                

def startping(server):
    """Try the ping test for 1 host"""
    res = ping(server["ip"])

    # timeout = res["timeout"]
    # is_alive = res["is_alive"]
    # rtt = res["rtt"]

    #info = {"timeout": timeout, "is_alive": is_alive, "rtt": rtt}

    log_entry(server, bool(res), "ping")

    if res == False:
        return False
    else:
        return True
    
