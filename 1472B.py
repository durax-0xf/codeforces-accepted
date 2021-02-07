ievade = int(input())

for i in range(ievade):
  cases = int(input())
  w = list(map(int, input().split()))
  viens = 0
  divi = 0
  for x in w:
    if(x == 1):
      viens += 1
    else:
      divi += 1
  if(divi % 2 == 0 and viens % 2 == 0 or viens % 2 == 0 and viens >= 2):
     print("YES\n")
  else:
      print("NO\n")
