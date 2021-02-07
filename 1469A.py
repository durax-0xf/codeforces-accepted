t = int(input())
for i in range(t):
  s = input()
  if(s[0] == ")"):
    print("NO")
  elif(s[-1] == "("):
    print("NO")
  elif(len(s)%2 !=0):
    print('NO')
  else:
    print('YES')