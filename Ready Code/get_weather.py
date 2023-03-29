import requests


def get_weather(city):
    url = f'https://api.weather.com/current?city={city}'
    response = requests.get(url, api_key='b85d262a25324df89a9155324232903')
    data = response.json()
    temperature = data['temperature']
    return temperature


print(get_weather('Sofia'))