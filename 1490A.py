t = int(input())
for j in range(t):
  rez = 0
  n = int(input())
  l = list(map(int, input().split()))
  for i in range(n-1):
    while(l[i] * 2 < l[i+1]):
      l[i] = l[i] * 2
      rez = rez + 1
    x = l[i+1]
    while(x * 2 < l[i]):
      x = x * 2
      rez = rez + 1
  print(rez)
