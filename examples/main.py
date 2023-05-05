from rich.text import Text
from textual import on
from textual.app import App
from textual.widgets import Button, Static
from textual_pandas.widgets import DataFrameTable
import pandas as pd

df = pd.DataFrame()
df["Name"] = ["Dan", "Ben", "Don", "John", "Jim", "Harry"]
df["Score"] = [77, 56, 90, 99, 83, 69]
df["Grade"] = ["C", "F", "A", "A", "B", "D"]


class ClassApp(App):
    CSS = """
    Button { margin: 1; } 
    """

    def compose(self):
        yield Static(
            Text("Press buttons to add and remove data.", style="bold orange1"),
            id="instruction_label",
        )
        yield DataFrameTable()
        yield Button("Add Teachers", variant="success", id="add-btn")
        yield Button("Delete Teachers", variant="error", id="delete-btn")

    def on_mount(self):
        table = self.query_one(DataFrameTable)
        # Initially add DataFrame to DataFrameTable
        table.add_df(df)

    @on(Button.Pressed, "#add-btn")
    def add_to_df(self):
        """Add new column with data to DataFrameTable."""
        col_name = "Teacher"
        try:
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
            # Update existing DataFrameTable with new DataFrame data
            table.update_df(df)
        except ValueError:
            self.query_one("#instruction_label", Static).update(
                Text(f"{col_name} column already exists!", style="bold red1")
            )

    @on(Button.Pressed, "#delete-btn")
    def remove_df_col(self):
        """Delete column from DataFrameTable."""
        try:
            col_name = "Teacher"
            df.drop(col_name, axis=1, inplace=True)
            table = self.query_one(DataFrameTable)
            # Update existing DataFrameTable with new DataFrame
            table.update_df(df)
        except KeyError:
            self.query_one("#instruction_label", Static).update(
                Text(f"{col_name} column does not exists!", style="bold red1")
            )


if __name__ == "__main__":
    app = ClassApp()
    app.run()
