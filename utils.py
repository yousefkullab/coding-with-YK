def add_expense(expense ,expenses):
    expenses.append(expense)
    print(f"{expense} was added")


def calculate_total(expenses):
    total = 0
    for i in range(len(expenses)):
        total += expenses[i]["amount"]
    return total

def get_highest_expense(expenses):
    max_amout = expenses[0]["amount"]
    for i in range(len(expenses)):
        if max_amout > expenses[i]["amount"]:
            continue
        else:
            max_amout = expenses[i]["amount"]
    return max_amout
                

def get_avg_expense(expenses):
    total = 0
    for i in range(len(expenses)):
        total += expenses[i]["amount"]
    return total/len(expenses)

def display_expenses(expenses):
    for i in range(len(expenses)):
        print(f'{expenses[i]["name"]}: {expenses[i]["amount"]}')