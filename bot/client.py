from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException
import logging

logger = logging.getLogger('trading_bot.client')

class BinanceFuturesClient:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret, testnet=True)
        logger.info('Binance Futures Testnet client initialized successfully')

    def create_market_order(self, symbol, side, quantity):
        try:
            logger.info(f'Creating MARKET {side} order: symbol={symbol}, quantity={quantity}')
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='MARKET',
                quantity=quantity
            )
            logger.info(f'Market order successful: orderId={order["orderId"]}')
            return order
        except (BinanceAPIException, BinanceOrderException) as e:
            logger.error(f'Failed to create market order: {e}')
            raise

    def create_limit_order(self, symbol, side, quantity, price):
        try:
            logger.info(f'Creating LIMIT {side} order: symbol={symbol}, quantity={quantity}, price={price}')
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='LIMIT',
                timeInForce='GTC',
                quantity=quantity,
                price=price
            )
            logger.info(f'Limit order successful: orderId={order["orderId"]}')
            return order
        except (BinanceAPIException, BinanceOrderException) as e:
            logger.error(f'Failed to create limit order: {e}')
            raise

