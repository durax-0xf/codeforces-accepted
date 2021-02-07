a, b = input().split()
a = int(a)
b = int(b)
 
h = 1
 
while (h*a) % 10 != b and (h*a) % 10 != 0:
  h += 1
print(h)
