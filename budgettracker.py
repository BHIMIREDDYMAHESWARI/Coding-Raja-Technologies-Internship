import tkinter as tk
from tkinter import messagebox

class BudgetTrackerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Budget Tracker")

        self.balance = 0
        self.transactions = []

        self.balance_label = tk.Label(master, text="Balance: rs 0")
        self.balance_label.pack()

        self.add_income_button = tk.Button(master, text="Add Income", command=self.add_income)
        self.add_income_button.pack()

        self.add_expense_button = tk.Button(master, text="Add Expense", command=self.add_expense)
        self.add_expense_button.pack()

        self.view_transactions_button = tk.Button(master, text="View Transactions", command=self.view_transactions)
        self.view_transactions_button.pack()

    def add_income(self):
        amount = tk.simpledialog.askfloat("Add Income", "Enter the income amount:")
        if amount is not None:
            description = tk.simpledialog.askstring("Add Income", "Enter a description:")
            if description:
                self.balance += amount
                self.transactions.append((amount, description, 'Income'))
                self.update_balance_label()

    def add_expense(self):
        amount = tk.simpledialog.askfloat("Add Expense", "Enter the expense amount:")
        if amount is not None:
            description = tk.simpledialog.askstring("Add Expense", "Enter a description:")
            if description:
                self.balance -= amount
                self.transactions.append((amount, description, 'Expense'))
                self.update_balance_label()

    def view_transactions(self):
        if not self.transactions:
            messagebox.showinfo("View Transactions", "No transactions recorded yet.")
            return

        transactions_str = "Transactions:\n"
        for transaction in self.transactions:
            transactions_str += "- Amount: rs{}, Description: {}, Type: {}\n".format(transaction[0], transaction[1], transaction[2])

        messagebox.showinfo("View Transactions", transactions_str)

    def update_balance_label(self):
        self.balance_label.config(text="Balance: rs{:.2f}".format(self.balance))


def main():
    root = tk.Tk()
    app = BudgetTrackerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

