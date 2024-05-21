
import requests
import json

products_response = requests.get("https://api.pro.coinbase.com/products")
with open("products.json", "w") as file:
    json.dump(products_response.json(), file, indent=4)

stats_response = requests.get("https://api.pro.coinbase.com/products/BTC-USD/stats")
with open("stats.json", "w") as file:
    json.dump(stats_response.json(), file, indent=4)

historical_data_response = requests.get("https://api.pro.coinbase.com/products/BTC-USD/candles?start=2024-01-01&end=2024-01-02&granularity=3600")
with open("historical_data.json", "w") as file:
    json.dump(historical_data_response.json(), file, indent=4)
