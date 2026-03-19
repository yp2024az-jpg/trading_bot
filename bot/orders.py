from .client import BinanceFuturesClient
from validators import OrderRequest
import logging

logger = logging.getLogger('trading_bot.orders')

def place_order(api_key, api_secret, symbol, side, ordertype, quantity, price=None):
    req = OrderRequest(symbol=symbol, side=side, type=ordertype, quantity=quantity, price=price)
    logger.info(f'Validated order request: {req.model_dump_json(indent=2)}')
    client = BinanceFuturesClient(api_key, api_secret)
    if req.type == 'MARKET':
        order = client.create_market_order(req.symbol, req.side, req.quantity)
    elif req.type == 'LIMIT':
        order = client.create_limit_order(req.symbol, req.side, req.quantity, req.price)
    else:
        raise ValueError(f'Unsupported order type: {req.type}')
    logger.info(f'Order placed successfully. Response: {order}')
    return order

