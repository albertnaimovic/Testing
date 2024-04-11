import requests


def get_stock_price(stock_name: str) -> float:
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock_name}&apikey=DHVVHGCAT5GZALII"
    r = requests.get(url)
    data = r.json()
    return data["Global Quote"]["02. open"]


print(get_stock_price("IBM"))

# url = "https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey=DHVVHGCAT5GZALII"
# r = requests.get(url)
# data = r.json()

# print("Top gainers:")
# for stock in data["top_gainers"]:
#     print(f"Stock: {stock['ticker']}, price: {stock['price']}")

# print("\nTop losers:")

# for stock in data["top_losers"]:
#     print(f"Stock: {stock['ticker']}, price: {stock['price']}")
