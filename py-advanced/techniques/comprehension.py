# List comprehension 
# [expression for item in iterable if condition]
prices = [10,42,5,55,76]

fees = [int(price * 0.1) for price in prices]

print(fees)

# Dictionary Comprehension
# { key:value for key, value in iterable if condition}

prices = {"BTC": 100, "ETH": 50, "SOL": 20}

updated_prices = {
    coin: int(value * 1.1) 
    for coin, value in prices.items()
}

print(updated_prices)

