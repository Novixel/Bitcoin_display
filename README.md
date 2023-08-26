<h1 align="center">Bitcoin Display</h1>

<p align="center">
  <strong>Real-time cryptocurrency price monitoring application</strong>
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#prerequisites">Prerequisites</a> •
  <a href="#getting-started">Getting Started</a> •
  <a href="#customization">Customization</a> •
  <a href="#troubleshooting">Troubleshooting</a> •
  <a href="#license">License</a>
</p>

<p align="center">
  <strong>Bitcoin Display is a simple that fetches the current price of a specified cryptocurrency pair from the Coinbase API and displays it on a webpage. The webpage also dynamically updates the price every second and changes the text color based on whether the price increases or decreases.</strong>
</p>


## Features

- Fetches real-time price data from the Coinbase API.
- Auto-updates the price on the webpage every second.
- Changes text color to green for price increase and red for price decrease.

## Prerequisites

- Python 3.x
- Flask
- Coinbase API Key and Secret (to access Coinbase data)

## Getting Started

1. Clone the repository:

    ```git clone https://github.com/novixel/coinbase-price-monitor.git```
    
    ```cd coinbase-price-monitor```

2. Install the required packages:

    ```pip install -r requirements.txt```

3. Configure your Coinbase API credentials:

    Open `coinbase_tests.py` and replace `'YOUR_API_KEY'` and `'YOUR_API_SECRET'` with your actual Coinbase API credentials.

4. Run the application:
    
    ```python app.py```

5. Open your web browser and navigate to `http://127.0.0.1:5000/` to see the live price updates.

## Customization

You can customize the displayed cryptocurrency pair by modifying the `product` variable in the `app.py` file.

## Troubleshooting

If you encounter any issues or errors, feel free to [open an issue](https://github.com/novixel/coinbase-price-monitor/issues) on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE)