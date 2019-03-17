import random

def dividing_secret(s,n,t,p,wielomian):
    sums=[] #suma z wzoru
    for j in range(1,n+1):
        sum = 0
        for i in range(0,t):
            sum=sum+wielomian[i]*j**i
        sums.append(sum)

    si=[]
    for i in range(0,n):
        si.append(sums[i] % p)

    for i in range(1,len(si)+1):
        print("Wartość udziału %d wynosi %s" %(i,si[i-1]))
    return si

def connecting_secret(si,t,p):
    s=0
    for i in range(1,t+1):
        numerator=1
        denominator=1
        for j in range(1,t+1):
            if j != i:
                numerator=numerator*(-j)
                denominator=denominator*(i-j)
        li=numerator/denominator
        if (li)>=0:
            yili=si[i-1]*li
            s=s+(yili%p)
        else:
            yili=si[i-1]*li
            s=s-((-yili)%p)
    print("Obliczony sekret to %d" %(s))


s=(int)(input("Podaj sekret: "))
n=(int)(input("Na ile udziałów go podzielić? "))
t=(int)(input("Ilu udziałowców jest niezbędnych do rozszyfrowania? "))
wielomian=[s]
for i in range(0,t-1): #generowanie wielomianu o t-1 elementach
     wielomian.append((int)(random.uniform(0,1000)))
if n>s: #generowanie p
    if n < (2 ** 16):
        p = (int)(random.uniform(n, 2 ** 16))
    else:
        p = (int)(random.uniform(n, 2 ** 64))
else:
    if s<(2**16):
        p = (int)(random.uniform(s, 2 ** 16))
    else:
        p = (int)(random.uniform(s , 2 ** 64))

si=dividing_secret(s,n,t,p,wielomian)
connecting_secret(si,t,p)


