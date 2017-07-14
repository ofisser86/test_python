import requests

city = input('City ')
api_url = 'http://api.openweathermap.org/data/2.5/weather'

params = {
    'q': city,
    'appid': '189338b3d193660312efb6f119275d97',
    'units': 'metric'
        }
res = requests.get(api_url, params=params)

#print(res.status_code)
#print(res.headers['Content-Type'])
data = res.json()
print(data['main']['temp'])
