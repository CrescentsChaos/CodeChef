T=int(input())
for i in range(1,T+1):
  XY=input()
  X,Y=tuple(XY.split(" "))
  total=int(X)+int(Y)
  if total>6:
    print("YES")
  else:
    print("NO")