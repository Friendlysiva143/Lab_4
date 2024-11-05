import random
l=[]
for i in range(10):
    n=random.randint(1,100)
    if n%2==0:
        l.append(n)
print(l)
print(sum(l))