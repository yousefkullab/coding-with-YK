class Order():
    VALID_ORDER_TYPES = {"BUY", "SELL"}
    def __init__(self, order_id, symbol, quantity, price, order_type):

        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")

        if price <= 0:
            raise ValueError("Price must be greater than 0")

        if order_type not in self.VALID_ORDER_TYPES:
            raise ValueError("Invalid order type")

        self.order_id = order_id
        self.symbol = symbol
        self.quantity = quantity
        self.price = price 
        self.order_type = order_type
        self.status = "PENDING"

    def calculate_value(self):
        return self.quantity * self.price
    
    def execute(self):
        if self.status == "EXECUTED":
            raise ValueError("Order is already executed")
        if self.status == "CANCELLED":
            raise ValueError("Cannot execute a cancelled order")

        self.status = "EXECUTED"

    def cancel(self):
        if self.status == "EXECUTED":
            raise ValueError("Cannot cancel an executed order")

        if self.status == "CANCELLED":
            raise ValueError("Order is already cancelled")

        self.status = "CANCELLED"

    def __str__(self):
           return (
            f"Order(id={self.order_id}, "
            f"symbol={self.symbol}, "
            f"quantity={self.quantity}, "
            f"price={self.price}, "
            f"type={self.order_type}, "
            f"status={self.status})"
        )


class Protfolio:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        if not isinstance(order, Order):
                raise TypeError("order must be an Order instance")

        self.orders.append(order)

    def remove_order(self, order_id):
        for order in self.orders:
                if order.order_id == order_id:
                    self.orders.remove(order)
                    return
        raise ValueError(f"Order {order_id} not found")
    
    def get_orders(self):
        return self.orders.copy()

    def calculate_total_order_value(self):
        return sum(order.calculate_value() for order in self.orders)
    
    def execute_order(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                order.execute()
                return

        raise ValueError(f"Order {order_id} not found")


class Trader:
    def __init__(self, name, balance):

        if balance < 0:
            raise ValueError("Balance can not be negative")
        
        self.name = name 
        self.balance = balance
        self.portfolio = Protfolio()

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError("Cannot withdraw more than balance")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        self.balance -= amount
        
    def place_order(self, order):
        self.portfolio.add_order(order)

