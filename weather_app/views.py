import requests
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from django.views import View


from django.utils.decorators import method_decorator
from django_ratelimit.decorators import ratelimit


import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('API_KEY')



class GetCity(View):
    def get(self, request):
        return render(request,'index.html')




@method_decorator(ratelimit(key='ip', rate='10/m', method='POST', block=True), name='dispatch')
class WeatherVeiw(APIView):
    def post(self, request):
        city = request.POST.get('city')
        if not city:
            return Response({'error': 'City parameter is required'}, status=400)
        api_url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=us&key={api_key}&contentType=json'
        try:
            response = requests.get(api_url)
            if response.status_code == 401:
                return Response({'error': 'Invalid API key'}, status=401)
            elif response.status_code in [400, 403, 404]:
                return Response({'client error': 'Please enter a valid city or check your network connection'}, status=400)
            elif response.status_code >= 500:
                return Response({'error': 'Weather API is currently down'}, status=503)
        except:
            return Response({'error': 'Please check your network connection'}, status=400)
        data = response.json()
        address = data['address']
        timezone = data['timezone']
        today_temp = data['days'][0]['temp']
        tomorrow_temp = data['days'][1]['temp']
        return Response({'address': address, 'timezone': timezone, 'today temperature': today_temp, 'tomorrow temperature': tomorrow_temp})