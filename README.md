# StockService

Simple django REST API to retreive stock market information using Alpha Vantage API

## Prepare your environment

After installing python create your virtual environment

`python -m venv env`

And install all the requirements

`pip install -r requirements.txt`

Add an .env file that contains your:
* SECRET_KEY: your django api secret key
* DEBUG: True or False. False when in production
* AV_API_KEY: Your Alpha Vantage API Key

## ROUTES IMPLEMENTED

| METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ----- | ------------- | ------------- |
| *POST* | ```/auth/signup/``` | _Register new user_| _All users_|
| *POST* | ```/login``` | _Login user - get access token_| _All users_|
| *GET* | ```/stoksinfo/``` | _Get a Stock Information_| _All authenticated users_|


Use the signup endpoint to create your user:

[image here]

Proceed to login enpoint to obtain you access token:

[image here]

Call the stocksinfo enpoint to get the given symbol information. Don't forget to send the access token in the Authorization header as a Bearer:

[image here]
[image here]
