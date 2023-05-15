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

In order to run your project, you will need to specify the environment mode (local/prod) with the evinronment variable:

`export DJANGO_SETTINGS_MODULE=stock_service.settings.local`

and go to the project's root directory, and run the server as needed:

`python manage.py runserver`

Or, send the flag that will specify the settings environment:

`python manage.py runserver --settings=stock_service.settings.local`

## ROUTES IMPLEMENTED

| METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ----- | ------------- | ------------- |
| *POST* | ```/auth/signup/``` | _Register new user_| _All users_|
| *POST* | ```/login``` | _Login user - get access token_| _All users_|
| *GET* | ```/stocksinfo/``` | _Get a Stock Information_| _All authenticated users_|


Use the signup endpoint to create your user:

![signup](https://github.com/AndrewB4y/StockService/assets/17863198/1d737f2d-31b4-4407-a43e-41365bd2d113)

Proceed to login enpoint to obtain you access token:

![login](https://github.com/AndrewB4y/StockService/assets/17863198/590d466c-d3d9-4f7e-85f0-832aca9771c3)

Call the stocksinfo enpoint to get the given symbol information. Don't forget to send the access token in the Authorization header as a Bearer:

![stockinf](https://github.com/AndrewB4y/StockService/assets/17863198/4fa731f8-b3fc-4b91-a12a-7c95ad50152d)

