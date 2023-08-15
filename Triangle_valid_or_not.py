a,b,c=map(int,input().split())
if(a+b>c):
    print("Valid triangle")
elif(a+c>b):
    print("Invalid triangle")
elif(b+c>a):
    print("Valid trinagle")
else:
    print("Invalid triangle")