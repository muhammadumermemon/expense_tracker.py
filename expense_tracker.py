import pandas as pd
import matplotlib.pyplot as plt

# Initialize an empty DataFrame to store expenses
expenses = pd.DataFrame(columns=['Date', 'Category', 'Amount', 'Description'])

def add_expense(date, category, amount, description):
    global expenses
    new_expense = pd.DataFrame([[date, category, amount, description]], columns=expenses.columns)
    expenses = pd.concat([expenses, new_expense], ignore_index=True)

def view_expenses():
    print(expenses)

def generate_report():
    report = expenses.groupby('Category')['Amount'].sum()
    report.plot(kind='bar')
    plt.show()

# Example usage
add_expense('2024-11-07', 'Food', 15.50, 'Lunch')
add_expense('2024-11-07', 'Transport', 5.00, 'Bus fare')
view_expenses()
generate_report()
