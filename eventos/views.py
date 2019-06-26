import requests
from django.shortcuts import render


# Create your views here.
def listar_eventos(request):
    url = 'https://apiauth.conveniar.com.br/conveniar/api/eventos/oauth/token'
    headers = {'X-API-KEY': '7e61b6bb-6841-415f-954e-5e2ba445cc7c'}
    r = requests.get(url, auth=('155', 'goto'), headers=headers)

    print(r.json())

    return render(request, 'listar_eventos.html')




# def index(request):
#     url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=YOUR_API_KEY'
#
#     if request.method == 'POST':
#         form = CityForm(request.POST)
#         form.save()
#
#     form = CityForm()
#
#     cities = City.objects.all()
#
#     weather_data = []
#
#     for city in cities:
#
#         r = requests.get(url.format(city)).json()
#
#         city_weather = {
#             'city' : city.name,
#             'temperature' : r['main']['temp'],
#             'description' : r['weather'][0]['description'],
#             'icon' : r['weather'][0]['icon'],
#         }
#
#         weather_data.append(city_weather)
#
#     context = {'weather_data' : weather_data, 'form' : form}
#     return render(request, 'weather/weather.html', context)
