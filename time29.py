n=int(input())
if n<=60:
    print("0",n)
else:
    a=n//60
    b=n%60
    print(a,b)
