st = set()
for i in range(int(input())):
  w=input()
  if(w in st):
    print("YES")
  else:
    st.add(w)
    print("NO")
