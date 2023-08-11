import math
A,B,C=map(int,input().split())
s=(A+B+C)/2
area=math.sqrt(s*(s-A)*(s-B)*(s-C))
print("%.2f"%area)