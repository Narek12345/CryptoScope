from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config import settings
from src.http_client import CMCHTTPClient


app = FastAPI()

cmc_client = CMCHTTPClient(
	base_url="https://pro-api.coinmarketcap.com",
	api_key=settings.CMC_API_KEY,
)


@app.get("/cryptocurrencies")
async def get_cryptocurrencies():
	return await cmc_client.get_listings()


@app.get("/cryptocurrencies/{currency_id}")
async def get_cryptocurrency(currency_id: int):
	return await cmc_client.get_currency(currency_id)


origins = [
	'http://localhost:5175',
	'http://127.0.0.1:5175',
]

app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=['*'],
)
