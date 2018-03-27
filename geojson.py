import urllib.parse
import urllib.request
import json

# Setup the "fixed" part of the requesting URL
serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
API_key= '&key=Your_API_KEY' # to get a key, google "Get API Key" and follow instruction

# Setup the "variable" part of the URL: location names (chosen by you). In my case, I use a list of predetermined locations in a csv file
while True:
    address = input('Enter location: ')
    if len(address) < 1 : break # if no input of address => Stop sending request

# Combine "Fixed" and "Variable" parts together
    url = serviceurl + urllib.parse.urlencode({'address': address}) + API_key
    print ('Retrieving', url) # show the final URL link we are going to use to request

# Use the URL to request 
    uh = urllib.request.urlopen(url)
    data = uh.read()
#   print (data) # original format, but not easy to parse. Because it takes a lot of space, I just use it in the trial phase

# convert Data from String to JSON
    try: js = json.loads(data) 
    except: js = None # if unable to convert, by default set to "None"
# troubleshooting if the data has any error
    if 'status' not in js or js['status'] != 'OK': # if data is wrong, it would not have a status or the status is not "OK"
        print ('==== Failure To Retrieve ====')
        print (data) # this is to view data if things go wrong
        continue # go to next location

#    print (json.dumps(js, indent=4)) # this is to see all information of that address input. Because it's lengthy, I skip

# My interested information: longitude, lattitude and school name
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print ('lat',lat,'lng',lng, 'name', address)
    location = js['results'][0]['formatted_address']
    print (location)
