# Stock Portfolio Tracker
stock_prices = {
    "TCS": 3500,
    "INFY": 1800,
    "RELIANCE": 2900,
    "HDFC": 1700,
    "WIPRO": 550
}

print("================================")
print("      STOCK PORTFOLIO TRACKER")
print("================================")

print("\nAvailable Stocks:")

for stock in stock_prices:
    print(stock, "Rs.", stock_prices[stock])

total = 0

while True:

    stock = input("\nEnter stock name: ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:

        quantity = int(input("Enter quantity: "))

        price = stock_prices[stock]

        amount = quantity * price

        print("Stock:", stock)
        print("Quantity:", quantity)
        print("Price: Rs.", price)
        print("Investment: Rs.", amount)

        total = total + amount

    else:
        print("Sorry, this stock is not available.")

print("\n================================")
print("       PORTFOLIO SUMMARY")
print("================================")

print("Total Investment: Rs.", total)

print("\nThank you for using the Stock Portfolio Tracker!")