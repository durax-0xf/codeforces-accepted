t = int(input())
for i in range(t):
  a, b, c = map(int, input().split())
  z = a+b+c
  if(z%9 == 0 and min(a, b, c) >= z//9):
    print("YES")
  else:
    print('NO')
