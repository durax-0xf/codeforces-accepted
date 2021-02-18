n = int(input())
t = {}
l = []
for j in range(n):
   x = input()
   l.append(x)
for i in l:
  if i in t:
    t[i] += 1
  else:
    t[i] = 1
  if t[i] == 1:
    print("OK")
  else:
      print(i+str(t[i]-1))
#was making it outside of the loop in the begining.
#what a way to waste 1 hour.
