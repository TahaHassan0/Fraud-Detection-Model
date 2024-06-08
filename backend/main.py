from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    'http://localhost:3000'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins= origins, 
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"], 
    allow_headers=["*"],
)



# Define a Pydantic model for the input data
class Transaction(BaseModel):
    trans_date_trans_time: str
    cc_num: float
    merchant: str
    category: str
    amt: float
    first: str
    last: str
    gender: str
    street: str
    city: str
    state: str
    zip: int
    lat: float
    long: float
    city_pop: int
    job: str
    dob: str
    trans_num: str
    unix_time: float
    merch_lat: float
    merch_long: float
    is_fraud: int

@app.post("/predict")
async def create_transaction(transaction: Transaction):
    #filhal khali hai hai
    return {"received_data": transaction}

# To run the server, use the command:
# uvicorn main:app --reload
