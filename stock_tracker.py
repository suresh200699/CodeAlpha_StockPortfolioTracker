stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

total_value = 0

print("=== Stock Portfolio Tracker ===")

while True:
    stock_name = input("Enter Stock Name (or 'done'): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stocks:
        quantity = int(input("Enter Quantity: "))
        investment = stocks[stock_name] * quantity
        total_value += investment

        print(f"{stock_name} Value = ${investment}")
    else:
        print("Stock not found!")

print("\nTotal Portfolio Value = $", total_value)

with open("portfolio.txt", "w") as file:
    file.write(f"Total Portfolio Value: ${total_value}")

print("Portfolio saved to portfolio.txt")
