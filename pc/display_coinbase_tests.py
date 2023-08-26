from coinbaseadvanced.client import CoinbaseAdvancedTradeAPIClient, Granularity
import os

# Add your key and secret as an environment variable with these names.
api_key = os.environ.get('COIN_API_KEY')
api_secret = os.environ.get('COIN_API_SEC')

client = CoinbaseAdvancedTradeAPIClient(api_key=api_key, secret_key=api_secret)

def get_price(product):
    product = client.get_product(product)
    trades = client.get_market_trades(product.product_id, 1)
    current_price = round(float(float(trades.best_ask) + float(trades.best_bid)) / 2, 8)
    #print(current_price)
    return current_price