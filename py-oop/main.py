from abc import ABC, abstractmethod

class User: # class
    platfrom = 'Tradeep' # Class Attribute

    def __init__(self, username, email): # Initializer
        self.username = username  # Instance Attribute
        self._email = email # Internal Attribute

    def login(self): # Instance Method
        return f"{self.username} logged in"

    def get_dashboard(self):
        return "Basic dashboard"

    @property  # Property
    def email(self):
        return self._email

    @email.setter # Encapsulation
    def email(self, new_email): 
        if "@" not in new_email:
            raise ValueError("Invalid Email")
        self._email = new_email

    def __str__(self): # Dunder Method
        return f"User({self.username})"

class Trader(User): # Inheritance 'is a'
    def __init__(self, username, email, balance):
        super().__init__(username, email)
        self.balance = balance
        self.portfolio = Portfolio()

    def place_trade(self):
        return f"{self.username} placed a trade"

    def get_dashboard(self):
        return "Trading dashboard"

    @classmethod
    def from_string(cls, data): # Class Method

        username, email, balance = data.split(",")

        return cls(
            username,
            email,
            float(balance)
        )

class Trade:
    @staticmethod
    def is_valid_quantity(quantity): # Static Method
        return quantity > 0
    
class Admin(User):

    def get_dashboard(self): # Polymorphism
        return "Admin dashboard"


class Payment(ABC): # Abstraction

    @abstractmethod
    def pay(self, amount):
        pass

class StripePayment(Payment):

    def pay(self, amount):
        return f"Paid {amount} using Stripe"

class PayPalPayment(Payment):

    def pay(self, amount):
        return f"Paid {amount} using PayPal"


class Portfolio: # Composion 'has a'
    
    def __init__(self):
        self.trades = []

    def add_trade(self, trade):
        self.trades.append(trade)

    def get_trade_count(self):
        return len(self.trades)
    
if __name__ == "__main__":
    
    # Create Trader object
    trader = Trader(
        "Yousef",
        "yousef@gmail.com",
        1000
    )

    print(trader)
    print(trader.login())
    print(trader.get_dashboard())

    # Test property
    print(trader.email)

    trader.email = "new@gmail.com"
    print(trader.email)

    # Test Class Method
    trader2 = Trader.from_string(
        "Ali,ali@gmail.com,5000"
    )

    print(trader2)
    print(trader2.balance)

    # Test Composition
    print(trader.portfolio.get_trade_count())

    # Test Static Method
    print(Trade.is_valid_quantity(10))
    print(Trade.is_valid_quantity(-5))

    # Test Polymorphism
    users = [
        User("User1", "user@gmail.com"),
        Trader("Trader1", "trader@gmail.com", 1000),
        Admin("Admin1", "admin@gmail.com")
    ]

    for user in users:
        print(user.get_dashboard())

    # Test Abstraction + Polymorphism
    payments = [
        StripePayment(),
        PayPalPayment()
    ]

    for payment in payments:
        print(payment.pay(100))


