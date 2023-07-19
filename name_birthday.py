import tkinter as tk
from datetime import datetime

class ErrorDialog(tk.Toplevel):
    """
    A custom error handler.
    """
    def __init__(self, parent, title, message):

        """
        Initialisation of the error dialog.

        Parameters:
            parent (tkinter widget): The parent widget.
            title (str): The title of the dialog.
            message (str): The error message.
        """
        tk.Toplevel.__init__(self, parent)
        self.title(title)
        self.geometry("200x100")
        
        tk.Label(self, text=message, bg='white', fg='red').pack()
        tk.Button(self, text="OK", command=self.destroy).pack()

class NameErrorDialog(ErrorDialog):
    def __init__(self, parent):
        super().__init__(parent, "Name Error", "Name can only contain letters.")

class DateErrorDialog(ErrorDialog):
    def __init__(self, parent):
        super().__init__(parent, "Date Error", "Invalid date.")

class FutureDateErrorDialog(ErrorDialog):
    def __init__(self, parent):
        super().__init__(parent, "Future Date Error", "Date cannot be in the future.")

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        # Create widgets
        self.name_label = tk.Label(self, text="Name")
        self.name_label.pack()

        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        self.date_label = tk.Label(self, text="Birthday")
        self.date_label.pack()

        self.year_label = tk.Label(self, text="Year")
        self.year_label.pack()
        self.year_var = tk.StringVar(self)
        self.year_var.set('Year')
        self.year_option = tk.OptionMenu(self, self.year_var, *[str(year) for year in range(1980, datetime.now().year+1)])
        self.year_option.pack()

        self.month_label = tk.Label(self, text="Month")
        self.month_label.pack()
        self.month_var = tk.StringVar(self)
        self.month_var.set('Month')
        self.month_option = tk.OptionMenu(self, self.month_var, *[str(month).zfill(2) for month in range(1, 13)])
        self.month_option.pack()

        self.day_label = tk.Label(self, text="Day")
        self.day_label.pack()
        self.day_var = tk.StringVar(self)
        self.day_var.set('Day')
        self.day_option = tk.OptionMenu(self, self.day_var, *[str(day).zfill(2) for day in range(1, 32)])
        self.day_option.pack()

        self.submit_button = tk.Button(self)
        self.submit_button["text"] = "Submit"
        self.submit_button["command"] = self.validate_inputs
        self.submit_button.pack()

    def validate_inputs(self):
        name = self.name_entry.get()
        if not name.isalpha():
            NameErrorDialog(self.master)
            return

        try:
            date = datetime.strptime(f"{self.year_var.get()}-{self.month_var.get()}-{self.day_var.get()}", '%Y-%m-%d').date()
        except ValueError:
            DateErrorDialog(self.master)
            return

        if date > datetime.now().date():
            FutureDateErrorDialog(self.master)
            return

        print(f"Name: {name}, Birthday: {date}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


