import urllib.request, urllib.parse
import json

# UPDATE THE BELOW API KEY WITH YOUR OWN
api_key = 'AIzaSyBHVoSx_XblDeBLUts_HWf2lvWb2llwqGc'

api = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    location = input('Enter a Location to get complete address details. e.g.- "tajmahal, india": ')
    if len(location)<1:
        print ('Good Bye')
        break
    print ('Fetching complete address . .. ...')
    url= api+ urllib.parse.urlencode({'address':location,'key':api_key,'sensor':'false'})
    uh= urllib.request.urlopen(url)
    data = uh.read().decode()

    try:
        json_data=json.loads(data)
    except:
        print ('No json data Found in google.')

    if not json_data or 'status' not in json_data or json_data['status'] != 'OK':
        print ('No Address Found, Please enter valid address.')
        continue

#Extracting required field from raw data
    comp_add=json_data['results'][0]['formatted_address']
    post_code=json_data['results'][0]['address_components'][-1]['long_name']
    lat=json_data['results'][0]['geometry']['location']['lat']
    lng=json_data['results'][0]['geometry']['location']['lng']
    type=json_data['results'][0]['types']

    print ('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print ('Complete Address :', '\n','\t','\t', comp_add)
    print ('PostCode :', '\n','\t','\t', post_code)
    print ('Lattitude :', '\n','\t','\t', lat)
    print ('Longitude :', '\n','\t','\t', lng)
    print ('Address Type :', '\n','\t','\t', ', '.join(type) )
    print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~','\n')