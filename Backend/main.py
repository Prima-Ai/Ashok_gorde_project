from fastapi import HTTPException,FastAPI
from fastapi.middleware.cors import CORSMiddleware
from manager import SmartOne

app = FastAPI(title="AlgoAPI to buy and sell")

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.post("/Place_order")
async def place_order(symbol:str,transactiontype:str,price:str,quantity:int):
    try:
        smartone = SmartOne()
        order = smartone.place_order(symbol,transactiontype,price,quantity)
        if order:
            return order
    except HTTPException as e:
        raise e