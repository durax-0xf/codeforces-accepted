t = int(input())

for i in range(t):
  j = 0
  n = int(input())
  b = input()
  a = []
  a.append(1)
  for j in range(1, n):
    if (int(b[j])+1) == (int(b[j-1])+a[-1]):
      a.append(0)
    else:
      a.append(1)

  print(*a, sep = "")

