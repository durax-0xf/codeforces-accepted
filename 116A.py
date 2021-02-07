n = int(input())
iev = []
i = 0
maxim = 0
pasreiz = 0

while(i<n):
  iev.append(list(map(int, input().split(" "))))
  i +=1
  
for b in iev:
  maini = b[1]-b[0]
  pasreiz+=maini
  if(pasreiz>maxim):
   maxim = pasreiz
 
print(maxim)