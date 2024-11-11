# Expense Tracker Python

A simple Python application to track daily expenses, view expense history, and generate spending reports.

## Features

- Add new expenses with date, category, amount, and description.
- View all recorded expenses.
- Generate a bar chart report of expenses by category.

## Requirements

- Python 3.x
- `pandas` library
- `matplotlib` library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/muhammadumermemon/expense_tracker.py.git
    ```
2. Navigate to the project directory:
    ```bash
    cd expense-tracker-python
    ```
3. Install the required libraries:
    ```bash
    pip install pandas matplotlib
    ```

## Usage

1. Run the script:
    ```bash
    python expense_tracker.py
    ```
2. Use the functions `add_expense`, `view_expenses`, and `generate_report` to manage and analyze your expenses.

## Example

```bash
add_expense('2024-11-07', 'Food', 15.50, 'Lunch')
add_expense('2024-11-07', 'Transport', 5.00, 'Bus fare')
view_expenses()
generate_report()
