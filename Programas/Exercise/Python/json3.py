import json
import urllib.request, urllib.parse, urllib.error

servic = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('enter location')
    if len(address) <1:break

    url =servic +urllib.parse.urlencode({'address': address})
    print('retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('retrive', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('-- faiulure ---')
        print(data)
        continue
    lat = js['results'][0]['geometry']['location']['lat']
    ing = js['results'][0]['geometry']['location']['ing']
    print('lat', lat, 'ing', ing)
    location = js['results'][0]['formated_address']
    print(location)
