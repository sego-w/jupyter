# Rewriting my growtopia calculator, this time with python generators

def farming_cycle():
    global n
    n = int(input("How many times are you farming? "))
    for i in range(n):
        yield 2496 * 1.08 ** n
g = farming_cycle()
print(f'On average, you will get {next(g):.0f} seeds from farming {n} times')

'''
HOMEWORK
'''

# Generating squares
def square_gen(y):
    for i in range(1,y):
        yield i**2

sqr_to_ten = square_gen(10)
for number in sqr_to_ten:
    print(number)
# Alternatively:
# print(next(sqr_to_ten))


# Yielding random numbers
from random import randint
def rando_num(low,high,N):
    for i in range(N):
        yield randint(low,high)
randos = rando_num(1,50,10)
z = [print(i) for i in randos]
# oneline skillz

# Converting str to iter()
def iter_word(word):
    iter(word)
    for i in word:
        yield i
word_1 = iter_word('Hello, my name jeff')
l = [print(i) for i in word_1]

# Generator comprehension
'''
Given code:

my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)
'''
# In this instance generator comprehension can be seen in
# the one-liner variable called gencomp.
# This variable iterates through a generator's yields
# and prints the ones that fit some condition
# (In this case, if the item > 3)
