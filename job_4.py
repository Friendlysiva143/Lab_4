import random
l=[]
s={}
for i in range(10):
    n=random.randint(1,100)
    l.append(n)
for j in range(len(l)):
    p=l[j]
    m=0
    c=[]
    for k in range(1,p+1):
        if p%k==0:
            c.append(k)
    s[p]=c
print(l)
print(s)