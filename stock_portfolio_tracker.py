print("======================================")
print("      STOCK PORTFOLIO TRACKER")
print("======================================\n")

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 130,
    "MSFT": 300,
    "AMZN": 100
}

portfolio = {}
total_investment = 0

# Display available stocks
print("Available Stocks and Prices:\n")

for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

print()

# Number of stocks user wants to add
num_stocks = int(input("Enter number of stocks in your portfolio: "))

# Input stock details
for i in range(num_stocks):

    print(f"\nStock #{i+1}")

    stock = input("Enter stock symbol: ").upper()

    # Check if stock exists
    if stock not in stock_prices:
        print(" Stock not available!")
        continue

    quantity = int(input(f"Enter quantity of {stock}: "))

    # Store in portfolio
    portfolio[stock] = quantity

    # Calculate investment
    investment = stock_prices[stock] * quantity
    total_investment += investment

    print(f" Added {quantity} shares of {stock}")

# Portfolio Summary
print("\n======================================")
print("         PORTFOLIO SUMMARY")
print("======================================")

for stock, qty in portfolio.items():

    price = stock_prices[stock]
    value = qty * price

    print(f"\nStock Name     : {stock}")
    print(f"Stock Price    : ${price}")
    print(f"Quantity       : {qty}")
    print(f"Total Value    : ${value}")

# Final Investment
print("\n======================================")
print(f" TOTAL INVESTMENT VALUE: ${total_investment}")
print("======================================")

# Investment Advice
print("\n Investment Suggestion:")

if total_investment < 1000:
    print(" Small portfolio. Consider diversifying investments.")

elif total_investment < 5000:
    print(" Good start! Maintain balanced investments.")

else:
    print(" Strong portfolio! Keep monitoring market trends.")

# Save to file
save = input("\nDo you want to save portfolio summary to file? (y/n): ").lower()

if save == 'y':

    with open("portfolio_summary.txt", "w") as file:

        file.write("======================================\n")
        file.write("      STOCK PORTFOLIO SUMMARY\n")
        file.write("======================================\n\n")

        for stock, qty in portfolio.items():

            price = stock_prices[stock]
            value = qty * price

            file.write(f"Stock Name  : {stock}\n")
            file.write(f"Price       : ${price}\n")
            file.write(f"Quantity    : {qty}\n")
            file.write(f"Total Value : ${value}\n\n")

        file.write("======================================\n")
        file.write(f"TOTAL INVESTMENT VALUE: ${total_investment}\n")
        file.write("======================================\n")

    print("\n Portfolio summary saved successfully!")

else:
    print("\n Portfolio summary was not saved.")

print("\n Thank you for using Stock Portfolio Tracker!")