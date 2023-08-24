a=int(input())
rd=0
while a!=0:
    r=a%10
    rd=rd*10+r
    a=a//10
print(rd)