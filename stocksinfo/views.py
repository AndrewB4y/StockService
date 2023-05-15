from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
import requests
from decouple import config
from datetime import datetime

User=get_user_model()

class StocksInfoView(generics.GenericAPIView):

    serializer_class = None
    permission_classes = [IsAuthenticated]

    alpha_vantage_key = config('AV_API_KEY')


    def get(self, request):

        symbol = 'META'
        parameters = request.GET

        if 'symbol' not in parameters:
            response = {'message': 'No stock symbol defined. Using default symbol: META'}

        url = 'https://www.alphavantage.co/query'

        payload = {
            'function': 'TIME_SERIES_DAILY_ADJUSTED',
            'symbol': symbol,
            'outputsize': 'compact',
            'apikey': self.alpha_vantage_key,
        }

        r = requests.get(url, params=payload)
        data = r.json()
        
        # Filtering data from response
        data = data['Time Series (Daily)']
        dates = [datetime.strptime(date, "%Y-%m-%d") for date in list(data.keys())]
        dates.sort()
        last_two_dates = [datetime.strftime(date, "%Y-%m-%d") for date in dates[-2:]]
        last_two = [data[date] for date in last_two_dates]

        variation_two = float(last_two[-1]['4. close']) - float(last_two[0]['4. close'])
        
        resp_data = {
            'symbol': symbol,
            'date': last_two_dates[-1],
            'open': last_two[-1]['1. open'],
            'high': last_two[-1]['2. high'],
            'low': last_two[-1]['3. low'],
            'closing_delta_two': str(variation_two),
        }
        
        return Response(data=resp_data, status=status.HTTP_200_OK)