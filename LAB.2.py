import requests

city= "Moscow,RU"
appid = "d124547bd20d42979f9214cf9c8dc201"

# Сегодня
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                  params={'q': city, 'units': 'metric', 'lang':'ru', 'APPID': appid})
data = res.json()

print("Город:", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])
print("Скорость ветра: ", data["wind"]["speed"])
print("Видимость: ", data["visibility"])

# Недельный прогноз
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
    params={'q': city,'units':'metric','lang':'ru','APPID': appid})
data = res.json()
print('прогноз погоды на неделю')
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература<",
          '{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодные условия <",
          i['weather'][0]['description'], ">")
    print('_______________________')