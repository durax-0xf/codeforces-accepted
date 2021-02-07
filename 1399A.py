a = int(input())
i = 0


while(a > i):
  n = int(input())
  l = list(map(int, input().split()))
  l.sort()
  i += 1


if(len(set(l)) <= 2):
  print("YES")
else:
  print("NO")


