import requests
from rest_framework.views import APIView
from rest_framework.response import Response


import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('API_KEY')




class WeatherVeiw(APIView):
    def get(self, request):
        city = request.GET.get('city')
        api_url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=us&key={api_key}&contentType=json'
        response = requests.get(api_url)
        if response.status_code == 400:
            return Response({'client error': 'please Enter City or check your network connection'}, status=400)
        elif response.status_code == 401:
            return Response({'error': 'Invalid API key'},status=401)
        elif response.status_code in [500, 501, 502, 503, 504]:
            return Response({'error': 'API is down'})
        return Response(response)
