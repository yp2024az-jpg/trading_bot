# Binance Futures Testnet Trading Bot

## Setup Steps
1. Create a Binance Futures Testnet account at https://testnet.binancefuture.com
2. Generate API Key and Secret with Futures Trading permissions.
3. Clone/download this repo or unzip to a folder.
4. Install dependencies:
   ```
   cd trading_bot
   pip install -r requirements.txt
   ```
5. (Optional) Create `.env` file with:
   ```
   API_KEY=your_testnet_api_key
   API_SECRET=your_testnet_api_secret
   ```

## How to Run
Run from `trading_bot/` dir. Pass API credentials via args or `.env`.

### Examples
**Market BUY:**
```
python cli.py market BTCUSDT BUY 0.001 --api_key YOUR_KEY --api_secret YOUR_SECRET
```

**Limit SELL:**
```
python cli.py limit BTCUSDT SELL 0.001 60000 --api_key YOUR_KEY --api_secret YOUR_SECRET
```

**With .env (loads automatically if present):**
```
python cli.py market BTCUSDT BUY 0.001
```

- Logs saved to `logs/bot.log`.
- Check order status in testnet dashboard.

## Assumptions
- Testnet only (no real funds).
- Basic validation (positive qty/price, valid side/type/symbol uppercase).
- No advanced precision checks (use testnet symbols like BTCUSDT).
- Typer CLI for enhanced UX.
- Errors logged and printed.

## Project Structure
```
trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   └── validators.py  (wait, validators.py is top level)
├── cli.py
├── logging_config.py
├── requirements.txt
├── README.md
```

