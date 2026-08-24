class Expense:
    def __init__(self, name, catogry, amount):

        if amount <= 0:
                    raise ValueError("Value must be greater than zero")
                
        self.name = name 
        self.catogry = catogry
        self.amount = amount
    def __str__(self):
        return f"{self.name}: {self.catogry} - $ {self.amount}"

class ExpenseTracker:
    def __init__(self):
            self.expenses = []

    def add_expense(self, expense):
            self.expenses.append(expense)

    def get_expenses(self):
            for expense in self.expenses:
                print(expense)
    def calculatee_total(self):
          total = 0
          for expense in self.expenses:
                total += expense.amount
          return total

    def filter_expenses(self, catogry):
        res = []
        for expense in self.expenses:
            if expense.catogry == catogry:
                res.append(expense)
        return res

    def remove_expense(self, expense):
          if expense in self.expenses:
                self.expenses.remove(expense)


            
