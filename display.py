from rich import print

print("[green]success[/green]")
print("[red]error[/red]")
print("[yellow]warning[/yellow]")

from rich.panel import Panel
from rich.console import Console

console = Console()

console.print(
        Panel(
             "Reads csv files and generates insights",
             title= "Data pipeline cli tool",
             subtitle= "V1"

              
              
        )


)
   

from rich.console import Console
from rich.table import Table

def show_report(cleaned_df , title):
 console = Console()

 table = Table(title= title)

 table.add_column("metric")
 table.add_column("value")
 

 table.add_row("Rows", str(len(cleaned_df)))
 table.add_row("Columns", str(len(cleaned_df.columns)))
 table.add_row("Duplicates", str(cleaned_df.duplicated().sum()))
 table.add_row("Missing values", str(cleaned_df.isnull().sum().sum()))

 console.print(table)

