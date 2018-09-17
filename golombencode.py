import math

def decode(t):
    x=[];
    while(t>0):
        x.append(t%2);
        t=int(t/2);
    return x

def gamma(t):
    x=[];
    y=[];
    while(t>0):
        x.append(t%2);
        t=int(t/2);
    for i in range(len(x)):
        y.append(0);
    y.append(1)
    return y;    


pp=1;
while(pp>0):
    x=int(input())  
    b=int(input())
    q=int(x/b)
    y=gamma(q+1)
    print(y)
    r=x-(q*b)
    i=math.floor(math.log(b,2));
    d=math.pow(2,i+1)-b;
    if(r>=d):
        r+=int(d);
    r2=decode(r);
    print(r2)
    if(len(r2)<i):
        r2.append(0);
    print(r2);
    r2=r2[::-1];
    y=y+r2;
    print(y);
