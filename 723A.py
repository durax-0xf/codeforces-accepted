a = input()
lis = a.split()
res = [int(i) for i in lis]
res.sort()
s = res[-1] - res[0]
print(s)