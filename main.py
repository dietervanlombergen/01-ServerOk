# Imports
import sys  # Sys arguments
import os  # To list a dir
from console import console  # Rich text output
from rich.prompt import IntPrompt
from rich.prompt import Prompt
from rich.prompt import Confirm

from app import app # Flask web application

import ping  # Ping functions
import data  # Data functions

from console import getTable  # Reset the table
from console import show_options


# Constants
TITLE = "Server OK?"
# List for the management options
# For use with only commands use "Add", "Delete", "Show", "Clear"
MANAGEMENT_OPTIONS = (
    "Add servers",
    "Delete servers",
    "Show servers",
    "Clear logs",
    "Stop program",
)

# List for the options in check mode
CHECKMODE_OPTIONS = ("Ping",)


# Start of code


def main():
    """Start of the application"""

    # CHECK IF THERE ARE ARGUMENTS
    if len(sys.argv)<= 1:
        console.print(
            ":rotating_light:",
            "Not possible to start with no mode selected",
            style="red",
        )
        sys.exit()
    else:
        # 1 = mode , 2 = command
        if sys.argv[1] == "management":
            management_mode()
        elif sys.argv[1] == "check":
            check_mode()
        else:
            console.print(
                ":rotating_light:", "Not possible to start in this mode", style="red"
            )
            sys.exit()


def check_mode():
    """Running the program in check mode"""
    # Show title in console
    console.rule(f"[bold red]{TITLE} - Check mode :glasses:")

    if len(sys.argv) == 2:
        # Show the check mode options
        show_options(CHECKMODE_OPTIONS, "Check mode options")
        option = IntPrompt.ask("Which option do you select")
    else:
        # Set the type as option
        option = sys.argv[2]

    # Check which function to execute
    match option:
        case "ping" | 0:
            ping.startping_servers(data.get_servers())

        case _:
            console.print(
                ":rotating_light:", "Not possible to start in this mode", style="red"
            )
            sys.exit()

    # Start webserver
    app.run()


def management_mode():
    """Running the program in management mode"""

    # Show title in console
    console.rule(f"[bold red]{TITLE} - Management mode :toolbox:")
    if len(sys.argv) == 2:
        # Show the management options
        show_options(MANAGEMENT_OPTIONS, "Management mode options")
        option = IntPrompt.ask("Which option do you select")
    else:
        # Set the command as option
        option = sys.argv[2]

    match option:
        case "add" | 0:
            if len(sys.argv) > 3:
                data.add_server(sys.argv[3], sys.argv[4])
            else:
                name = Prompt.ask("Enter the server name")
                ip = Prompt.ask("Enter the server ip")
                data.add_server(name, ip)
        case "delete" | 1:
            if len(sys.argv) > 3:
                if sys.argv[3] == "all":
                    confirm = Confirm.ask(":rotating_light: Are you sure you want delete all servers")
                    if confirm == True:
                        data.delete_allservers()
                else:
                    confirm = Confirm.ask(f":rotating_light: Are you sure you want delete {sys.argv[3]} server")
                    if confirm == True:
                        data.delete_server(sys.argv[3])
            else:
                name_list = [server["name"] for server in data.get_servers()]
                name = Prompt.ask("Enter the server name", choices=name_list, show_choices=True)
                confirm = Confirm.ask(f":rotating_light: Are you sure you want delete [red]{name} server")
                if confirm == True:
                    data.delete_server(name)

        case "show" | 2:
            data.show_servers()
        case "clear" | 3:
            if len(sys.argv) == 3:
                data.clear_log(f"log/{sys.argv[3]}")
            else:
                log = Prompt.ask(
                    "Which log do you want to clear?",
                    choices=get_files("log"),
                    show_choices=True,
                )
                data.clear_log(f"log/{log}")

        case _:
            console.print(
                ":rotating_light:", "Not possible to start in this mode", style="red"
            )
            sys.exit()


def get_files(path):
    """Get the files from a dir"""
    res = os.listdir(path)
    return res


if __name__ == "__main__":
    main()
