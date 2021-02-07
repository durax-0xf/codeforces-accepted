n = int(input())
l = list(map(int, input().split()))
o = 0
p = l.count(1)
m = l.count(2)
pe =l.count(3)
lists = [p, m, pe]
lists.sort()
if(p == 0 or m == 0 or pe == 0):
  print("0")
  exit()
else:
  print(lists[0])

i1 = [i for i, e in enumerate(l) if e == 1]
i2 = [j for j, b in enumerate(l) if b == 2]
i3 = [k for k, c in enumerate(l) if c == 3]
b1 = [x+1 for x in i1]
b2 = [x+1 for x in i2]
b3 = [x+1 for x in i3]

big = [len(b1), len(b2), len(b3)]
big.sort(reverse = True)

while(o<lists[0]):
  print(b1[0],b2[0],b3[0])
  b1.pop(0)
  b2.pop(0)
  b3.pop(0)
  o +=1

 


