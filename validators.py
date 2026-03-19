from pydantic import BaseModel, Field, validator
from typing import Literal, Optional
from dotenv import load_dotenv
import os

load_dotenv()

class OrderRequest(BaseModel):
    symbol: str = Field(..., description="Trading pair e.g. BTCUSDT")
    side: Literal['BUY', 'SELL'] = Field(..., description="Order side")
    type: Literal['MARKET', 'LIMIT'] = Field(..., description="Order type")
    quantity: float = Field(..., gt=0, description="Order quantity")
    price: Optional[float] = Field(None, gt=0, description="Limit price")

    @validator('symbol')
    def uppercase_symbol(cls, v):
        return v.upper()

    @validator('price')
    def validate_price(cls, v, values):
        order_type = values.get('type')
        if order_type == 'MARKET' and v is not None:
            raise ValueError('Price should not be provided for MARKET orders')
        if order_type == 'LIMIT' and v is None:
            raise ValueError('Price is required for LIMIT orders')
        return v

def get_api_credentials(api_key: Optional[str] = None, api_secret: Optional[str] = None) -> tuple[str, str]:
    key = api_key or os.getenv('API_KEY')
    secret = api_secret or os.getenv('API_SECRET')
    if not key or not secret:
        raise ValueError('Provide API_KEY and API_SECRET via --api_key/--api_secret or .env file')
    return key, secret

