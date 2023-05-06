# textual-pandas

A module to display Pandas DataFrames in Textual's DataTable widget.

## Background

Pandas is a popular Python library for data analysis. One of the core components of Pandas is the DataFrame object. A DataFrame is a two-dimensional data structure that represents data in rows and columns.

Given Pandas DataFrames are tabular in nature, it makes sense to be able to render them in Textual using the DataTable widget. Enter the DataFrameTable widget...

## Installation

Install `textual-pandas` via pip:

```
pip install textual-pandas
```

## Getting Started

`textual-pandas` introduces a new widget called `DataFrameTable`, which uses Textual's DataTable widget as a base.

First, you'll need to import the `DataFrameTable` widget.

```python
from textual_pandas.widgets import DataFrameTable
```

After importing the widget, you'll need to yield the `DataFrameTable` widget in your Textual app's `compose()` method (like you would with the DataTable widget). Once you're ready to draw the table with your DataFrame data (most likely `on_mount()`), you'll simply call the `add_df()` method and pass in a Pandas DataFrame.

```python
from textual.app import App
from textual_pandas.widgets import DataFrameTable
import pandas as pd

# Pandas DataFrame
df = pd.DataFrame()
df["Name"] = ["Dan", "Ben", "Don", "John", "Jim", "Harry"]
df["Score"] = [77, 56, 90, 99, 83, 69]
df["Grade"] = ["C", "F", "A", "A", "B", "D"]

class ClassApp(App):
    def compose(self):
        yield DataFrameTable()

    def on_mount(self):
        table = self.query_one(DataFrameTable)
        table.add_df(df)
```

That's it! Now your DataFrame will display within a DataTable widget!

### Updating the DataFrame

If you update your DataFrame, and would like to see the updates in your app, then you'll need to use the `update_df()` method and pass in your updated DataFrame object.

If you only want to update the rendered DataFrameTable (without the need to change the DataFrame), you may also use the `update_cell()` and `update_cell_at()` methods that are provided by the DataTable widget.

```python
df.insert(
    1,
    "Teacher",
    [
        "Mr. Smith",
        "Mr. Smith",
        "Mr. Smith",
        "Mr. Smith",
        "Mr. Smith",
        "Mr. Smith",
    ],
)
table = self.query_one(DataFrameTable)
# Provide new DataFrame to update DataFrameTable widget
table.update_df(df)
```

## Contributing

I built this module for the sole purpose of displaying a Pandas DataFrame in a DataTable widget. I'm sure there's additional functionality with the Pandas library that others would like to see!

If you have any ideas, questions, or issues, please feel free to open an issue or PR!