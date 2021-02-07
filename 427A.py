summa = 0
skaits = 0
n = int(input())
l = list(map(int, input().split()))
for x in l:
  if x == -1:
    if skaits > 0:
      skaits = skaits - 1
    else:
      summa = summa + 1
  else:
    skaits = skaits + x
print(summa)