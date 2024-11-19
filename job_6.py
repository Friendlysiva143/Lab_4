from audioop import reverse
import random
l=[]
for i in range(10):
    n=random.randint(1,100)
    l.append(n)
print(l)
for i in range(9):
    for j in range(i+1,10):
        x=str(l[i])+str(l[j])
        if x==x[::-1]:
            print(x)