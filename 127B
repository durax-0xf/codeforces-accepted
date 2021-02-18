n = int(input())
x = [int(x) for x in input().split()]
d = {}
cnt = 0
for i in x:
    d[i] = x.count(i)
for atsl in d:
  if(d[atsl]%2 != 0):
    cnt = cnt+d[atsl]//2
  elif(d[atsl] >= 4 and d[atsl]%2 == 0):
    cnt = cnt+d[atsl]//2
  else:
    cnt+=1
print(int(cnt//2))
