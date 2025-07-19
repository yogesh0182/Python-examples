'''
1. Randomly generate a number between 1 and 1000.
2. Allow the user to guess until they find the correct number.
3. Provide hints if the guess is too high or too low.
4. If user found the number, print their score on basis of how many attempts they have used.
'''
import random
import os
import time

rand=random.randint(1,1000)
num=0
count = -1
print(f"{rand=}")

#print success case
def print_success(attempts):
    print("Found it!!")
    print("Your score: ", attempts)

while num!=rand :
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    num=int(input("Enter a number: "))
    count+=1
    diff = num - rand
    if num == rand:
        print_success(count)
    elif abs(diff) > 500:
        if num < rand:
            print("too low")
        else:
            print("too high")
    elif abs(diff) > 100:
        if num < rand:
            print("low")
        else:
            print("high")
    elif abs(diff) > 20:
        print("near")
    else:
        print("so so close")
    time.sleep(2)

 

        
