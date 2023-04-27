from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


class Device(BaseModel):
    deviceSerial: str
    mid: str
    tid: str
    acquirer: str
    location: str
    merchantUsername: str
    chargeslipHeader: str
    appKey: str

# class Response(BaseModel):
#     message: str


#     # description: Union[str, None] = None
#     # price: float
#     # tax: Union[float, None] = None


class UserInformation(BaseModel):
    fullname: str
    email: str

app = FastAPI()


# Add CORS middleware to allow requests from all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.get("/api/1.0/form")
# async def get_form_data():  # item: Item
#     return {"hi": "is here"}


@app.post("/api/1.0/form")
async def process_form_data(user_info: UserInformation):  # item: Item
    # do something with the form data
    # for example, print it to the console
    print(f"{user_info.fullname=}")
    print(f"{user_info.email=}")

    return {"message": "Form submitted successfully", "data_submitted": user_info}

        

