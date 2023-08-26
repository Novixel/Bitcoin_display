from flask import Flask, render_template, jsonify
from web_coinbase_tests import get_price
import asyncio
import threading

app = Flask(__name__)

product = "BTC-USD"
current_price = "Loading..."
old_price = 0

async def update_price():
    global current_price
    global old_price
    while True:
        price = get_price(product)
        current_price = price
        await asyncio.sleep(1)

async_thread = threading.Thread(target=asyncio.run, args=(update_price(),), daemon=True)
async_thread.start()

@app.route('/')
def index():
    return render_template('index.html', product=product, current_price=current_price)

@app.route('/get_price')
def get_updated_price():
    global current_price
    global old_price
    price = get_price(product)
    
    if old_price > price:
        color = "red"
    else:
        color = "green"
    
    old_price = price
    current_price = price
    
    return jsonify(product=product, current_price=current_price, color=color)

if __name__ == '__main__':
    app.run(debug=True)