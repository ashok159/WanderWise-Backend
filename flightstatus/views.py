# flightstatus/views.py
from django.http import JsonResponse
import requests

def get_flight_status(request, flight_iata):
    api_key = 'fd5bb2e1-ffd0-46bc-a128-0fa2cb205c4c'
    url = f'https://airlabs.co/api/v9/flight?flight_iata={flight_iata}&api_key={api_key}'

    try:
        response = requests.get(url)
        json_data = response.json()
        return JsonResponse({'status': 'success', 'data': json_data['response']})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})

