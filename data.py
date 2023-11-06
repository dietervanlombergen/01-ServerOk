# Imports
import json
import os
from console import console
from console import getTable
import datetime # To get the current time
import pytz
import logger
# Const
TIMEZONE = "Europe/Brussels"

# Where the json files are stored
LOGS = {"server": "json_data/server.log",
        "serverjson": "json_data/server.json",
"ping": "log/ping_checks.json"} 

# JSON data files paths
DATA = {"server": "json_data/servers.json"}




# Server functions
def add_server(name, ip):
    """Add server to local JSON file"""
    try:
        if not os.path.exists(DATA["server"]) or os.path.getsize(DATA["server"]) == 0:
            data = []
            index = 1
        else:
            # Read current servers
            with open(DATA["server"], "r") as s:
                data = json.load(s)
            index = int(data[-1]["id"]) + 1

        # Add server to list
        server = {"id": index ,"name": name, "ip": ip}
        data.append(server)

        # Write data to file
        with open(DATA["server"], "w") as s:
            json.dump(data, s, indent=4)

        console.log(data)
    except Exception as e: 
        console.log(f"{e}", style="red")

    # Log the add server
    
    logger.logger.info(f"A server with name {name} and ip {ip} is added")
    
def delete_allservers():
    """Clear the local JSON file"""   
    with open(DATA["server"], "w") as s:
        s.truncate()
    console.log("The file is cleared")

def delete_server(name):
    """Delete a server from local JSON file"""
    # Read current servers
    with open(DATA["server"], "r") as s:
        server_data = json.load(s)

    # Remove server from list
    for server in server_data:
        if server["name"] == name:
            server_data.remove(server)
            console.log(f"{name} server data is removed")
    
    # Write data to file
    with open(DATA["server"], "w") as s:
        json.dump(server_data, s, indent=4)

    logger.logger.warning(f"{name} server is removed")

def show_servers():
    """Show all servers"""

    # Check if
    try:
        # Read current servers
        with open(DATA["server"], "r") as s:
            server_data = json.load(s)

        # Tables
        table = getTable()
        table.title = "Server list"
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
    with open(DATA["server"], "r") as s:
        server_data = json.load(s)

    return server_data

# Logs
# General log functions
def clear_log(log_file):
    """Clear the log file"""   
    with open(log_file, "w") as log:
        log.truncate()

    console.log("The log is cleared")

def add_log_entry(server , result, type):
    """Add log for a type of check"""
    timestamp = datetime.datetime.now(pytz.timezone(TIMEZONE)).strftime("%Y-%m-%d %H:%M:%S")

    try:
        if not os.path.exists(LOGS[type]) or os.path.getsize(LOGS[type]) == 0:
            data = []
        else:
            # Read current pings
            with open(LOGS[type], "r") as p:
                data = json.load(p)

        # Add ping entry to list
        entry = {"date": timestamp, "type": type ,"name": server["name"], "ip": server["ip"], "result": result}
        data.append(entry)

        # Write data to file
        with open(LOGS[type], "w") as p:
            json.dump(data, p, indent=4)
    except Exception as e: 
        console.log(f"{e}", style="red")

def get_log(type):
    """Get the latest log info"""
    try:
        if not os.path.exists(LOGS[type]) or os.path.getsize(LOGS[type]) == 0:
            return []
        else:
            # Read current pings
            with open(LOGS[type], "r") as p:
                data = json.load(p)


        # Count the servers for latest information
        number_servers = len(get_servers())
        
        return data[-number_servers:]

    except Exception as e: 
        console.log(f"{e}", style="red")
    

