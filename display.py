

from rich.panel import Panel
from rich.console import Console

console = Console()

console.print(
        Panel(
             "Reads CSV and JSON files and generates insights",
             title= "Data pipeline cli tool",
             subtitle= "V2"

              
              
        )


)


from rich.console import Console
from rich.table import Table

def show_report(df , title):
 console = Console()

 table = Table(title= title)

 table.add_column("metrics")
 table.add_column("value")
 

 table.add_row("Rows", str(len(df)))
 table.add_row("Columns", str(len(df.columns)))
 table.add_row("Duplicates", str(df.duplicated().sum()))
 table.add_row("Missing values", str(df.isnull().sum().sum()))

 console.print(table)

