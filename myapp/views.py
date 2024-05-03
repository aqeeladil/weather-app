from django.shortcuts import render
# import json to load json data to python dictionary
import json
# urllib.request to make a request to api
import urllib.request


def index(request):
    if request.method == 'POST':
        city = request.POST['city']

        # appid="place your api_key here"
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=c50203d9534d0f16c6f45d5c50310603').read()
        
        # converting json data to dictionary
        json_data = json.loads(source)

        # data for variable json_data
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp'])+'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }

    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city': city, 'data': data})


    
            


        

        

        

        
        
        
    