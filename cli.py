import typer
import json
import sys
from dotenv import load_dotenv
from logging_config import setup_logger
from bot.orders import place_order
from validators import get_api_credentials

load_dotenv()
app = typer.Typer()
logger = setup_logger()

@app.command()
def market(
    symbol: str,
    side: str,
    quantity: float,
    api_key: str = typer.Option(None, "--api_key"),
    api_secret: str = typer.Option(None, "--api_secret")
):
    
    try:
        key, secret = get_api_credentials(api_key, api_secret)
        order = place_order(key, secret, symbol, side, 'MARKET', quantity)
        print("Order Request Summary:")
        print(f"  Symbol: {symbol}")
        print(f"  Side: {side}")
        print(f"  Type: MARKET")
        print(f"  Quantity: {quantity}")
        print("\nOrder Response:")
        print(json.dumps(order, indent=2))
        print("\nSUCCESS: Market order placed!")
        logger.info('CLI market command completed successfully')
    except Exception as e:
        error_msg = f"MARKET order failed: {str(e)}"
        print(f"ERROR: {error_msg}", file=sys.stderr)
        logger.error(error_msg)
        raise typer.Exit(code=1)

@app.command()
def limit(
    symbol: str,
    side: str,
    quantity: float,
    price: float,
    api_key: str = typer.Option(None, "--api_key"),
    api_secret: str = typer.Option(None, "--api_secret")
):
    
    try:
        key, secret = get_api_credentials(api_key, api_secret)
        order = place_order(key, secret, symbol, side, 'LIMIT', quantity, price)
        print("Order Request Summary:")
        print(f"  Symbol: {symbol}")
        print(f"  Side: {side}")
        print(f"  Type: LIMIT")
        print(f"  Quantity: {quantity}")
        print(f"  Price: {price}")
        print("\nOrder Response:")
        print(json.dumps(order, indent=2))
        print("\nSUCCESS: Limit order placed!")
        logger.info('CLI limit command completed successfully')
    except Exception as e:
        error_msg = f"LIMIT order failed: {str(e)}"
        print(f"ERROR: {error_msg}", file=sys.stderr)
        logger.error(error_msg)
        raise typer.Exit(code=1)

if __name__ == "__main__":
    logger.info('Trading Bot CLI started')
    app()

