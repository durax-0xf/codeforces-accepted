t = int(input())

for i in range(t):
  case = int(input())
  z = case/2
  while(z%2 == 0):
    z = z/2
  if(z > 1): 
    print('yes')
  else:
    print('no')