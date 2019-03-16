from math import gcd as bltin_gcd
import time

def primRoots(modulo):
    required_set = {num for num in range(1, modulo) if bltin_gcd(num, modulo) }
    return [g for g in range(1, modulo) if required_set == {pow(g, powers, modulo)
            for powers in range(1, modulo)}]
def isPrime2(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n ** 0.5) + 1, 2):  # only odd numbers
        if n % i == 0:
            return False
    return True
def calculating_x_and_y(g,x,n):
    return (g**x) % n


n=(int)(input("Choose a prime number: "))
check=True
while check:
    if isPrime2(n):
        check=False
        print("Correct prime number.")
    else:
        print("It wasn't prime number, I'll increment it.")
        print("Now trying with "+ str(n+1))
        n+=1
t = time.process_time()
g=primRoots(n)[-1]
elapsed_time = time.process_time() - t
print("Time taken to find  primitive root mod n: " + str(elapsed_time))
print("Let's simulate connection between two people. Now you are person A:")
private_x=(int)(input("Choose your private key: "))
X=calculating_x_and_y(g,private_x,n)
print("Now you are person B:")
private_y=(int)(input("Choose your private key: "))
Y=calculating_x_and_y(g,private_y,n)
print("Sending X and Y to each other.")
print("Now A and B calculate k")
kA=calculating_x_and_y(Y,private_x,n)
kB=calculating_x_and_y(X,private_y,n)
print("k calculated by A: "+str(kA))
print("k calculateb by B: "+str(kB))
