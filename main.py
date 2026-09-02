from trading import Trader, Order

T1 = Trader("Yousef", 29000)
order1 = Order(1, "AAPL", 10, 200, "BUY")
order2 = Order(2, "TSLA", 5, 300, "SELL")

T1.place_order(order1)
T1.place_order(order2)

print(T1.name)
print(T1.balance)

print(T1.portfolio.get_orders())
print(T1.portfolio.calculate_total_order_value())

T1.deposit(1000)
print(T1.balance)

T1.withdraw(3000)
print(T1.balance)

T1.portfolio.execute_order(order1.order_id)
print(order1)

