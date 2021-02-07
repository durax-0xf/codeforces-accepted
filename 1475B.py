t = int(input())
for i in range(t):
  n = int(input())
  x = n%2020
  sk = x*2021
  if(sk <= n):
    print('yes')
  else:
    print('no')