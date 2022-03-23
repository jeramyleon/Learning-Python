for item in 'Python':
    print(item)

for item in ['Mosh', 'John', 'Sarah']:
    print(item)

for item in [1, 2, 3, 4]:
    print(item)

for item in range(5, 10, 2): # first par defines start number
# second par defines last number while excluding it 
# third par determines what intervals to go up or down by
    print(item)

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price 
print(f"Total: {total}")



