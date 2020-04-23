import requests
from twilio.rest import Client

def get_weather_dictionary(api_key, city_id='6176823'):
    """Request the weather from OpenWeatherMap
    
    Request the weather for a city, using its city_id, from OpenWeatherMap 
    using the provided api_key. Process the response object assuming it is
    valid JSON and return a Python dictionary version of that JSON.
    Parameters
    ----------
    api_key: str
        A valid API key for OpenWeatherMap in the form of a string
    city_id: str, optinal
        A number from OpenWeatherMap's city id list passed as a string. 
        Defaults to Waterloo Canada.
    Returns
    -------
    resp: dict
        Processed response from server; interpreted as JSON and turned into a
        Python dictionary.
    """
    payload = {'id': city_id, 'appid': api_key, 'units': 'metric'}
    
    raw_resp = requests.get('http://api.openweathermap.org/data/2.5/weather', params=payload)
    resp = raw_resp.json()
    return resp

a = get_weather_dictionary('===api_key===')
print (a)

keys = a.keys()
print ("KEYS in dictionary: ",keys)

for i in a:
    print (i, a[i])
    print ('==== key:value pairs =====')

hnm = str(a['main'])
print ("STRING: ",hnm)

lst = list(a['main'])
print ("LIST: ",lst)

for i in lst:
    print (i, a['main'][i])


# Your Account Sid and Auth Token from twilio.com/console
account_sid = '==sid==='
auth_token = '===token==='
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
            body= '\n' + 'WEATHER SMS'  + '\n' +
                  str(lst[0]) + ': ' + str(a['main'][lst[0]]) + '\n' + 
                  str(lst[1]) + ': ' + str(a['main'][lst[1]]) + '\n' + 
                  str(lst[2]) + ': ' + str(a['main'][lst[2]]) + '\n' + 
                  str(lst[3]) + ': ' + str(a['main'][lst[3]]) + '\n' +
                  str(lst[4]) + ': ' + str(a['main'][lst[4]]) + '\n',

            from_='+12268873676',
            to='+11234567890'
        )

print(message.sid)
