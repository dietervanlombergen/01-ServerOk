# Imports
import json
import os
from console import console
from console import getTable
import datetime # To get the current time

# Const

# Where the json files are stored
SERVERDATA = "json_data/servers.json"
PINGCHECKDATA = "json_data/ping_checks.json"


# Server functions
def add_server(name, ip):
    """Add server to local JSON file"""
    try:
        if not os.path.exists(SERVERDATA) or os.path.getsize(SERVERDATA) == 0:
            data = []
            index = 1
        else:
            # Read current servers
            with open(SERVERDATA, "r") as s:
                data = json.load(s)
            index = int(data[-1]["id"]) + 1

        # Add server to list
        server = {"id": index ,"name": name, "ip": ip}
        data.append(server)

        # Write data to file
        with open(SERVERDATA, "w") as s:
            json.dump(data, s, indent=4)

        console.log(data)
    except Exception as e: 
        console.log(f"{e}", style="red")
    
def delete_allservers():
    """Clear the local JSON file"""   
    with open(SERVERDATA, "w") as s:
        s.truncate()
    console.log("The file is cleared")

def delete_server(name):
    """Delete a server from local JSON file"""
    # Read current servers
    with open(SERVERDATA, "r") as s:
        server_data = json.load(s)

    console.log(server_data)

    # Remove server from list
    for server in server_data:
        if server["name"] == name:
            server_data.remove(server)
            console.log(f"{name} server data is removed")
    
    # Write data to file
    with open(SERVERDATA, "w") as s:
        json.dump(server_data, s, indent=4)

    console.log(server_data)

def show_servers():
    """Show all servers"""

    # Check if
    try:
        # Read current servers
        with open(SERVERDATA, "r") as s:
            server_data = json.load(s)

        console.log(server_data)

        # Tables
        table = getTable()
        table.add_column("ID")
        table.add_column("Server name")
        table.add_column("IP")
        for server in server_data:
            table.add_row(str(server["id"]), server["name"], server["ip"])
        console.print(table)

    except:
        console.log("The list is empty or does not exist", style="red")



def get_servers():
    """Get the servers as object"""
    with open(SERVERDATA, "r") as s:
        server_data = json.load(s)

    return server_data

# Logs
# General log functions
def clear_log(log_file):
    """Clear the log file"""   
    with open(log_file, "w") as log:
        log.truncate()

    console.log("The log is cleared")


# Log Ping checks

def log_pingcheck(server , result):
    """Add log for ping check"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        if not os.path.exists(PINGCHECKDATA) or os.path.getsize(PINGCHECKDATA) == 0:
            data = []
        else:
            # Read current pings
            with open(PINGCHECKDATA, "r") as p:
                data = json.load(p)

        # Add ping entry to list
        entry = {"date": timestamp, "name": server["name"], "ip": server["ip"], "result": result}
        data.append(entry)

        # Write data to file
        with open(PINGCHECKDATA, "w") as p:
            json.dump(data, p, indent=4)
    except Exception as e: 
        console.log(f"{e}", style="red")

