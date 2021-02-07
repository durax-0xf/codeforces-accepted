cena, ir, grib = input().split()
i = 0
izt = 0

cena = int(cena)
ir = int(ir)
grib = int(grib)

while(i < grib):
  i += 1
  izt = izt + (cena*i)

fin = izt-ir

if(fin < 1):
  print("0")
else:
  print(fin)
