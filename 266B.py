cik, laiks = input().split()
cik = int(cik)
laiks = int(laiks)
seciba = input()
i = 0
while(i < laiks):
  seciba = seciba[0:] = seciba[-1]
  seciba = seciba[:-1]
  i +=1
print(seciba)
