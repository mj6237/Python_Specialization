import urllib.request, urllib.parse, urllib.error
import json
import ssl

# The API endpoint specified in the assignment
serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'

# Ignore SSL certificate errors, as sometimes required by the environment
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Main loop to repeatedly ask for locations
while True:
    address = input('Enter location: ')
    # Break the loop if the user enters nothing
    if len(address) < 1:
        break

    # Prepare the query parameters for the URL
    parms = dict()
    parms['q'] = address
    
    # URL encode the parameters and append them to the service URL
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    
    # Use a try/except block to handle potential network errors
    try:
        # Open the URL and read the data
        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read().decode()
        print('Retrieved', len(data), 'characters')

    except urllib.error.URLError as e:
        print(f"Error retrieving URL: {e.reason}")
        continue # Continue to the next loop iteration

    # Parse the retrieved data as JSON
    try:
        js = json.loads(data)
    except json.JSONDecodeError:
        js = None

    # Check if JSON parsing was successful and if the expected structure exists
    if not js or 'features' not in js or len(js['features']) == 0:
        print('==== Failed to retrieve plus code (invalid response) ====')
        print(data)  # Print the raw data for debugging
        continue # Continue to the next loop iteration

    # Now, try to safely access the nested plus_code
    try:
        # The plus code is inside 'features' -> first item -> 'properties' -> 'plus_code'
        plus_code = js['features'][0]['properties']['plus_code']
        print('Plus code', plus_code)

        # Optional: Print the full formatted location as well
        location = js['features'][0]['properties']['formatted']
        print('Location:', location)
    except KeyError:
        print('==== Plus code not found in the data ====')
        print(data) # Print the raw data to see the actual keys
    except IndexError:
        print('==== No features found in the data ====')
        print(data)
