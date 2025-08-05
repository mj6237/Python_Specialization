
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# User se URL input len
url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Total sum ke liye ek variable shuru karein
total = 0

# Sabhi <span> tags ko dhoondhen
tags = soup('span')
for tag in tags:
    # Tag ke andar ka text haasil karein
    number_string = tag.contents[0]
    
    # Text ko integer mein tabdeel karein
    number = int(number_string)
    
    # Number ko total mein jama karein
    total += number

# Loop khatam hone ke baad, total sum print karein
print('Total sum of all numbers:', total)


