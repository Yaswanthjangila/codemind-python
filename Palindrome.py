a=int(input())
b=0
c=a
while c!=0:
    r=c%10
    c=c//10
    b=b*10+r
if b==a:
    print("Palindrome")
else:
    print("Not Palindrome")