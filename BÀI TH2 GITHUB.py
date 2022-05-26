#BÀI TH 2
#1
n1=int(input("enter n1 value="))
n2=int(input("enter n2 value="))
if n1>n2:
    print("n1 is big")
elif n1==n2:
    print("n1 = n2")
else:
    print("n2 is big")
#2
import math;
x1=int(input("enter x1--->"))
y1=int(input("enter y1--->"))

x2=int(input("enter x2--->"))
y2=int(input("enter y2--->"))

d1 = (x2 - x1);
d2 = (y2 - y1);
res = math.sqrt(d1*d1+d2*d2)
print("distance between two points:",res);
            
#3
n=int(input("enter a number ---->"))
if n%2 == 0:
    print ("even number");
else:
    print ("odd number");

#4
i=1;
for j in range(2,10):
    print ("i:",i,"j",j)
    print(i,"/",j)
    print (i/j);
#5
n=int(input("enter A number --->"));
while  n>=0:
    print (n);
    n=n-1;
#6
j=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        j.append(str(i))
    print (','.join(j))
#7
n=int(input("nhap vào một số:"))
d=dict()
for i in range(1,n+1):
    d[i]=i*i
print (d)
#8
a,b=1,2
total=0
print(a,end=" ")
while (a <=4000000-1):
    if a%2==0:
        total +=a
    a,b=b,a+b
    print (a,end=" ")
print("\n sum of prime number term in fibonacci seriesL ",total)
#9
str=input("enter a string")
dict={}
for i in str:
    dict[i]=str.count(i)
    print (dict)

#10
a="hi i am python programmer"
b=a.split()
print(b)
c=" ".join(b)
print(c)
#11
l=[1,'python',4,7]
k=['cse',2,'guntur',8]
m=[]
m.append(l);
m.append(k);
print(m)
d={1:l,2:k,'combine_list':m}
print(d)
#12
import re
value=[]
items=[x for x in input("nhập mật khẩu: ").split(',')]
# ########
for p in items:
    if len(p)<6 or len(p)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",p):
        coitinue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    else:
        pass
    value.append(p)
print(",".join(value))
#13
a = float(input("nhap he so a: "))
b = float(input("nhap he so b: "))
c = float(input("nhap he so c: "))
delta = b*b-4*a*c
if delta < 0: print("phuong trinh vo nghiem")
elif delta ==0:
    print("phuong trinh co nghiem kep x1=x2=",-b/(2*a))
else:
    import math
    x1 = (-b+ math.sqrt(delta))/(2*a)
    x2 = -b/a-x1
    print("phuong trinh co 2 nghiem phan biet")
    print ("x1=",x1,"x2=",x2)
