import math

def gamma(t):
    x=[];
    y=[];
    while(t>0):
        x.append(t%2);
        t=int(t/2);
    for i in range(len(x)-1):
        y.append(0);
    for i in range(len(x)):
        y.append(x.pop());
    return y;
 

x=int(input('Enter a number: '));
t=math.floor(1+math.log(x,2));
p=gamma(t);
y=[];
while(x>0):
    y.append(x%2);
    x=int(x/2);
y.pop();
for i in range(len(y)):
    p.append(y.pop());
a=''.join(map(str,p));
print('Elias Delta Code: '+a)
