import tkinter as tk
from project import connect_to_database, add_expense, view_expenses, calculate_totals

# Function to add an expense when the "Add Expense" button is clicked
def add_expense_button_clicked():
    date = date_entry.get()
    category = category_entry.get()
    description = description_entry.get()
    amount = float(amount_entry.get())
    connection = connect_to_database()
    add_expense(connection, date, category, description, amount)
    clear_entry_fields()

# Function to view all expenses when the "View Expenses" button is clicked
def view_expenses_button_clicked():
    connection = connect_to_database()
    expenses = view_expenses(connection)
    display_expenses(expenses)

# Function to calculate daily, monthly, and yearly totals when the "Calculate Totals" button is clicked
def calculate_totals_button_clicked():
    connection = connect_to_database()
    calculate_totals(connection)

# Function to clear all entry fields
def clear_entry_fields():
    date_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

# Function to display the expenses in the GUI
def display_expenses(expenses):
    expense_listbox.delete(0, tk.END)
    for expense in expenses:
        expense_listbox.insert(tk.END, expense)

# Create the main window
root = tk.Tk()
root.title("Expense Tracker")

# Create a label and entry field for the date
date_label = tk.Label(root, text="Date:")
date_label.grid(row=0, column=0)
date_entry = tk.Entry(root)
date_entry.grid(row=0, column=1)

# Create a label and entry field for the category
category_label = tk.Label(root, text="Category:")
category_label.grid(row=1, column=0)
category_entry = tk.Entry(root)
category_entry.grid(row=1, column=1)

# Create a label and entry field for the description
description_label = tk.Label(root, text="Description:")
description_label.grid(row=2, column=0)
description_entry = tk.Entry(root)
description_entry.grid(row=2, column=1)

# Create a label and entry field for the amount
amount_label = tk.Label(root, text="Amount:")
amount_label.grid(row=3, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=3, column=1)

# Create a button to add an expense
add_button = tk.Button(root, text="Add Expense", command=add_expense_button_clicked)
add_button.grid(row=4, column=0)

# Create a button to view all expenses
view_button = tk.Button(root, text="View Expenses", command=view_expenses_button_clicked)
view_button.grid(row=4, column=1)

# Create a button to calculate totals
total_button = tk.Button(root, text="Calculate Totals", command=calculate_totals_button_clicked)
total_button.grid(row=5, column=0)

# Create a listbox to display the expenses
expense_listbox = tk.Listbox(root)
expense_listbox.grid(row=6, column=0, rowspan=2, columnspan=2)

# Establish a connection to the PostgreSQL database
connection = connect_to_database()

# Start the main loop
root.mainloop()