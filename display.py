
from rich.panel import Panel
from rich.console import Console
from rich.align import Align
from rich.text import Text
from rich.table import Table

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




def show_shape(shape , title):
 console = Console()

 table = Table(title= title)
 table.add_column("Metrics")
 table.add_column("Value")

 table.add_row("Rows" , str(shape[0]))
 table.add_row("Columns" , str(shape[1]))

 console.print(table)

 
def show_columns(columns):
  console = Console()

  table = Table()
  table.add_column("COLUMN NAMES")

  for column in columns:
   table.add_row(column)
  console.print(table)


def show_report(df , title):
 console = Console()

 table = Table(title= title)

 table.add_column("Metrics")
 table.add_column("Value")
 

 table.add_row("Rows", str(len(df)))
 table.add_row("Columns", str(len(df.columns)))
 table.add_row("Duplicates", str(df.duplicated().sum()))
 table.add_row("Missing values", str(df.isnull().sum().sum()))

 console.print(table)

from rich.console import Console
from rich.table import Table


def show_large_dataset_info(file_name, file_size):

    console = Console()

    table = Table(title="LARGE DATASET INFORMATION")

    table.add_column("Metric")
    table.add_column("Value")

    table.add_row("File Name", file_name)
    table.add_row("File Size", f"{file_size:.2f} MB")

    console.print(table)