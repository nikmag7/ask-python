print "Kalispera"
n=input("Give Fibonacci Sequence Term   ")
terms=[1,1]
for i in range (1,n-1):
    p=terms[-1]+terms[-2]
    terms.append(p)
p=terms[-1]
print p
import random
prwtos=0
for i in range (20):
    a=random.randint(1,1000)
    while a-p<0:
        a=random.randint(1,1000)
    y=a**p-a
    x=y-a
    if y%p==0:
        prwtos=prwtos+1
if prwtos==20:
    print ("O arithmos einai prwtos")
else:
    print ("O arithmos den einai prwtos")
print prwtos
