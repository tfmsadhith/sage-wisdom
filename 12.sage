

x = len(divisors(polygonal_number(3,1)))

i = 1

while x <= 500:
  x = len(divisors(polygonal_number(3,i)))
  i += 1

print(polygonal_number(3,i - 1))
