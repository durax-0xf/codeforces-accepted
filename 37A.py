n = int(input())
x = list(map(int, input().split()))
t = {}
p = 0
for i in x:
  if i in t:
    t[i] += 1
  else:
    t[i] = 1
for k in t:
  p = max(t[k], p)
print(p, len(t))


""""
alternate version
for i in x:
  t[i]= 1+t.get(i, 0)
print(max(t.values()), len(t))
"""""