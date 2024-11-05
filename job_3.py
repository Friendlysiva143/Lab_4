import random
l=[]
s=[]
for i in range(10):
    n=random.randint(1,100)
    l.append(n)
for j in range(len(l)):
    p=l[j]
    m=0
    for k in range(1,p):
        if p%k==0:
            m+=1
    if m<2:
        s.append(p)
print(l)
print(s)
print(sum(s))
