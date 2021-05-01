# Fibonacci sequence to the nth instance
from random import randint
def fib(n):
    global q
    list_inst = [1,1]
    x=1
    y=1
    for i in range(n):
        x += y
        list_inst.append(x)
        y += x
        list_inst.append(y)
    for item in list_inst:
        print(item)
    q = int(input("How many integers in the fibonacci sequence do you want to print? "))

def true_random_coin_flip():
    so_random = []
    for i in range(int(input("Say da numba: "))):
        so_random.append(randint(1,2))
    print(f"There are {so_random.count(1)} instances of 1 and {so_random.count(2)} instances of 2.")
    if so_random.count(1) - so_random.count(2) < abs(0.05*len(so_random)):
        print("This method seems to work for a coin flip!")
    else:
        print("very sus library")



def collatz(n):
    if n%2==0:
        print(n/2)
    else:
        print(n*3+1) 

def fizzbuzz(n):
    for i in range(1,n):
        if n % 3 == 0:
            print("fizz")
        else:
            print(i)

def reverser(strng):
    return str(strng)[::-1]


    