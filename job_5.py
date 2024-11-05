import random
l=[]
m=[]
for i in range(10):
    n=random.randint(1,100)
    l.append(n)
for j in range(len(l)-1,-1,-1):
    m.append(l[j])
print(l)
print(m)