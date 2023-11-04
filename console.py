from rich.console import Console # Import rich console 

console = Console() # Create one console for everything

from rich.table import Table # Import rich table

def getTable():
    """Give a empty clean table to use"""
    return Table()
