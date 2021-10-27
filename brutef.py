# capital guessing
import keyboard as keyb
from time import sleep
s = str(input("Input brute force attempt: "))

def capitalize_thing(s,numberino):
    keyb.write(s[:numberino] + s[numberino].upper() + s[numberino+1:]+"\n")
    sleep(0.5)
    print("Trying again...")
    sleep(0.5)

def guess_try():
    print("Initiating attempt sequence...")
    for x in enumerate(s):
        capitalize_thing(s,x[0])

def main():
    guess_try()

main()

