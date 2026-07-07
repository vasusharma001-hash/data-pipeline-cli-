
from rich.panel import Panel
from rich.console import Console
from rich.align import Align
from rich.text import Text


console = Console()

console.print(
        Panel(
                Align.center("Read • Inspect • Clean • Export Datasets "),
             title= " DATA PIPELINE CLI TOOL  v3 ",
             title_align = "center",
             subtitle_align = "center",
             width = 80,
             height = 4,
              
              
        )


)


from rich.console import Console
from rich.table import Table

def show_shape(shape , title):
 console = Console()

 table = Table(title= title)
 table.add_column("metrics")
 table.add_column("value")

 table.add_row("Rows" , str(shape)[1])
 table.add_row("Columns" , str(shape)[4])

 console.print(table)

 
def show_columns(columns , title):
  console = Console()

  table = Table(title = title)
  table.add_column("Columns Name")

  for column in columns:
   table.add_row(column)
  console.print(table)


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

