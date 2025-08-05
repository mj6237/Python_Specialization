import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# User se inputs len
url = input('Enter URL: ')
try:
    count_str = input('Enter count: ')
    count = int(count_str)
except ValueError:
    print("Invalid count. Please enter an integer.")
    exit()

try:
    position_str = input('Enter position: ')
    position = int(position_str)
    # Python ki list indexing 0 se shuru hoti hai, isliye position mein se 1 minus kar dein.
    if position < 1:
        print("Position must be 1 or greater.")
        exit()
    position_index = position - 1
except ValueError:
    print("Invalid position. Please enter an integer.")
    exit()

print("Initial URL:", url)

# Diye gaye count ke mutabiq loop chalaein
for i in range(count):
    print("Retrieving:", url)
    try:
        html = urllib.request.urlopen(url, context=ctx).read()
    except urllib.error.URLError as e:
        print(f"Error retrieving URL: {e.reason}")
        break

    soup = BeautifulSoup(html, 'html.parser')
    
    # Saare anchor tags talash karein
    tags = soup('a')
    
    # Agar position valid na ho to break karein
    if len(tags) <= position_index:
        print("Error: Position is out of range for the current page.")
        break
    
    # Specified position par tag ko talash karein
    tag = tags[position_index]
    
    # Naya URL haasil karein
    url = tag.get('href', None)
    
    # Aakhri naam (last name) ko tag ke contents se haasil karein
    last_name = tag.contents[0]

# Loop khatam hone ke baad, aakhri naam print karein
print("The last name found is:", last_name)
