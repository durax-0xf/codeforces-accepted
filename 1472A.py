t = int(input())
for i in range(t):
  w, h, n = map(int, input().split())
  suma = 1
  while(w % 2 == 0):
    suma = suma * 2
    w = w / 2
  while(h % 2 == 0):
    suma = suma * 2
    h = h / 2
  if(suma >= n):
    print("YES\n")
  else:
    print("NO\n")
  