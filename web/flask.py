from flask import Flask, render_template, jsonify
from coinbase_tests import get_price

app = Flask(__name__)

@app.route('/')
def index():
    product = "BTC-USD"
    current_price = get_price(product)
    return render_template('index.html', product=product, current_price=current_price)

if __name__ == '__main__':
    app.run(debug=True)