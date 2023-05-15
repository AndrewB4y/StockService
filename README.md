# StockService

Simple django REST API to retreive stock market information using Alpha Vantage API

## Prepare your environment

After installing python create your virtual environment

`python -m venv env`

And install all the requirements

`pip install -r requirements.txt`

## ROUTES IMPLEMENTED

| METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ----- | ------------- | ------------- |
| *POST* | ```/auth/signup/``` | _Register new user_| _All users_|
| *POST* | ```/login``` | _Login user - get access token_| _All users_|
| *GET* | ```/stoksinfo/``` | _Get a Stock Information_| _All authenticated users_|
