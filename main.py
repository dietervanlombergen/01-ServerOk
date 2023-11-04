# Imports
import sys # Sys arguments
from console import console # Rich text output
from rich.prompt import IntPrompt
import ping # Ping functions
import data # Data functions
#from console import optionstable # To show the options
#from console import table # Test table
from console import getTable # Reset the table

# Constants
TITLE = "Server OK?"
# List for the management options
MANAGEMENT_OPTIONS = (
    "Add servers",
    "Delete servers",
    "Show servers",
    "Stop program"
)

# List for the options in check mode
CHECKMODE_OPTIONS = (
    "Ping"
)



# Start of code

def main():
    """Start of the application"""

    #CHECK IF THERE ARE ARGUMENTS
    if len(sys.argv) <= 1:
        console.print(":rotating_light:","Not possible to start with no mode selected", style="red")
        sys.exit()
    else:
        # 1 = mode
        if sys.argv[1] == "management":
            management_mode()
        elif sys.argv[1] == "check":
            check_mode()
        else:
            console.print(":rotating_light:","Not possible to start in this mode", style="red")
            sys.exit()


    # # Ask the option
    # option = IntPrompt.ask("Choose an option")

    # # Check the option
    # match option:
    #     case 0:
    #         console.print("Add servers")
    #         name = input("Whats the name of the server you want to add: ")
    #         ip = input("Whats the ip of the server you want to add: ")
    #         data.add_server(name, ip)
    #     case 1:
    #         console.print("Delete servers")
    #         name = input("Whats the name of the server you want to delete: ")
    #         data.delete_server(name)
    #     case 2: 
    #         console.print("Show servers")
    #         data.show_servers()
    #     case 3:
    #         console.print("Check servers")
    #         check_servers()
    #     case 4:
    #         console.print("Exit program")
    #         sys.exit()
    #     case default:
    #         print("No option is choosen, try again")

def check_mode():
    """Running the program in check mode"""
    console.print("Check mode")

def management_mode():
    """Running the program in management mode"""

    # Show title in console
    console.rule(f"[bold red]{TITLE} - Management mode :toolbox:")

    # Show the possible options
    # table.title= "Options" # Set title
    optionsTable = getTable()
    optionsTable.add_column("Select", style="cyan") # Add select column
    optionsTable.add_column("Option", style="yellow") # Add option column

    for i in range(len(MANAGEMENT_OPTIONS)):
        optionsTable.add_row(str(i), MANAGEMENT_OPTIONS[i]) # Create a row for every possible option

    console.print(optionsTable) # print the options table





if __name__ == "__main__":
    main()