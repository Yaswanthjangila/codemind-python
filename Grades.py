p,ch,b,m,c=map(int,input().split())
per=(p+ch+b+m+c)/5
if(per>=90):
    print("Grade A")
elif(per>=80 and per<=90):
    print("Grade B")
elif(per>=70 and per<=80):
    print("Grade C")
elif(per>=60 and per<=70):
    print("Grade D")
elif(per>=40 and per<=60):
    print("Grade E")
elif(per<40):
    print("Grade F")