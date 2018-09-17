import math

def decode(x):
    num=0;
    for i in range(len(x)):
        num+=(int(x[len(x)-1-i])*(math.pow(2,i)));
    return num;

x=str(input());
if(x=='1'):
    print('1');
    exit;
else:
    x=list(x);
    t=0;    
    v=[];
    b=0;
    w=[];
    c=0;
    for i in x:
        if(b!=1):
            if(i=='0'):
                t+=1;
            else:
                v.append(i);
                b=1;
        elif(c!=1):
            if(t==0):
                c=1;
                w.append('1');
                w.append(i);
            else:
                v.append(i);
                t-=1;
        else:
            num=decode(v);
            if(num==0):
                break;
            else:
                w.append(i);
                num-=1;
    ans=decode(w);
    print(int(ans));


