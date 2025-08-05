import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

# XML data ko parse karein
tree = ET.fromstring(data)

# 'count' elements ko talash karein
counts = tree.findall('.//count')
nums = list()

# Har 'count' element ke text ko number mein tabdeel kar ke list mein daalein
for result in counts:
    # Debug print the data
    print(result.text)

    # **Zaroori Tarmeem (Important Fix):**
    # Yahan hume 'result.text' ko integer mein tabdeel kar ke list mein add karna hai.
    nums.append(int(result.text))


print('Count:', len(nums))
print('Sum:', sum(nums))

