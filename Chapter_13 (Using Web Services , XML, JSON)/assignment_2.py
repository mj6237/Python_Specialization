import urllib.request, urllib.parse, urllib.error
import json
import ssl

# SSL certificate errors ko nazar andaz karein
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# User se URL input len
url = input('Enter location: ')

# Agar URL khali ho to default URL istemal karein
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'

print('Retrieving', url)

try:
    # URL se data haasil karein
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    # JSON data ko parse karein
    try:
        js = json.loads(data)
    except:
        js = None
    
    # Agar JSON parse na ho to error message dein
    if not js or 'comments' not in js:
        print('==== Failure To Retrieve ====')
        print(data)
        exit()

    # Total sum aur count ke liye variables
    total_sum = 0
    count = 0

    # 'comments' list par loop chalaein
    for item in js['comments']:
        # Har item mein se 'count' ki value extract karein
        comment_count = item['count']
        
        # Values ko jama karein
        total_sum += comment_count
        count += 1

    # Aakhri natija print karein
    print('Count:', count)
    print('Sum:', total_sum)

except urllib.error.URLError as e:
    print(f"Error retrieving URL: {e.reason}")

