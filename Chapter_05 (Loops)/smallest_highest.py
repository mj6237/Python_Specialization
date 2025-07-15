largest = None
smallest = None
invalid = False  # Flag to track invalid input

while True:
    num = input()
    if num == 'done':
        break
    try:
        n = int(num)
    except:
        invalid = True
        continue

    if largest is None or n > largest:
        largest = n
    if smallest is None or n < smallest:
        smallest = n

if invalid:
    print("Invalid input")
print("Maximum is", largest)
print("Minimum is", smallest)
