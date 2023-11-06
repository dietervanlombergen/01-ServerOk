from rich.console import Console # Import rich console 

console = Console() # Create one console for everything

from rich.table import Table # Import rich table

def getTable():
    """Give a empty clean table to use"""
    return Table()


def show_options(options, title=""):
    # Show the possible options
    optionsTable = getTable()
    optionsTable.title= title # Set title
    optionsTable.add_column("Select", style="cyan") # Add select column
    optionsTable.add_column("Option", style="yellow") # Add option column

    for i in range(len(options)):
        optionsTable.add_row(str(i), options[i]) # Create a row for every possible option

    console.print(optionsTable) # print the options table

