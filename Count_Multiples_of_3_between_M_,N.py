a,b=map(int,input().split())
n=0
for i in range(a,b):
    if i%3==0:
        n=n+1
print(n)