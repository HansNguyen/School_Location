import urllib.parse
import urllib.request
import json

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
API_key= '&key=Your_API_KEY' # to get a key, google "Get API Key" and follow instruction

while True:
    address = input('Enter location: ')
    if len(address) < 1 : break # if no input of address => Stop sending request

    url = serviceurl + urllib.parse.urlencode({'address': address}) + API_key
    print ('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print ('Retrieved',len(data),'characters')
#    print (data) # original format, but not easy to parse

    try: js = json.loads(data) # convert Data from String to JSON
    except: js = None # our input data is unable to be converted to JSON
    if 'status' not in js or js['status'] != 'OK':
        print ('==== Failure To Retrieve ====')
        print (data) # this is to view data if things go wrong
        continue # go to next location

#    print (json.dumps(js, indent=4)) # this is to see all information of that address input

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print ('lat',lat,'lng',lng)
    location = js['results'][0]['formatted_address']
    print (location)
