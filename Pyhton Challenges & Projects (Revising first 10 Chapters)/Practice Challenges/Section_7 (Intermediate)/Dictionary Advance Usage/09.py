'''
1. Create a dictionary: country_codes = {"USA": "1", "Canada": "1", "UK": "44", "Germany": 
"49"}. 
2. Create a new empty dictionary codes_to_countries. 
3. Loop through country_codes. For each key-value pair, add a new entry to codes_to_countries where the 
original value becomes the key and the original key becomes the value. 
4. Important: Handle cases where multiple original keys map to the same value (e.g., USA and Canada both have 
code "1"). For simplicity, just let the last one encountered override previous ones for the same value. 
5. Print codes_to_countries.
'''
country_codes = {"USA": "1", "Canada": "1", "UK": "44", "Germany": 
"49"}
codes_to_country = {}
for key, values in country_codes.items() :
    codes_to_country[values] = key

print(codes_to_country)