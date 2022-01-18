'''
username = input("What username will you like to use?: ")
username = username.islower()
while True:
    username_2 = input("confirm username: ")
    username_2 = username_2.islower()
    if username != username_2:
        print("Login successful")
        break
    else:
        print('login failed')
        pass
'''
'''
counter = 1
username = input("What username will you like to use?: ")
username = username.islower()
while counter<=2:
    username_2 = input("confirm username: ")
    username_2 = username_2.islower()
    if username != username_2:
        print("Login successful")
        break
    else:
        print('login failed')
        counter+=1
'''
# figure = input("input figures here: ")
# figure = figure.split(" ")
# fig = map(lambda a: int(a), figure)
# fid = list(fig)
# print(fid)

#using while loop, write a code that displays out a list of foods and if a user inputs the name of any of the fruits it displays "You will have (name of the fruit) for dinner".
# foods = input("food: (rice,beans,garri): ") 
# while True:
#     if foods == 'rice':
#         print(f"you'll be having {foods} for dinner.")
#         break
#     elif foods == 'beans':
#         print(f"you'll be having {foods} for dinner.")
#         break
#     else:
#         print("you'll be having garri for dinner.")
        # break

#Funcions
# def area_of_circle():
#     r=2
#     area = 3.142*r**2
#     print(area)


# area_of_circle()

# def area_of_sphere(radius):
#     area = (4/3)*3.142*radius**3
#     print(area)

# area_of_sphere(6.2)

import time

# def useless():
#          for i in range(10, 0, -1):
#             for j in range(10, 0, -1):
#                 for k in range(60, 0, -1):
#                     for l in range(60, 0, -1):
#                         print(i, ":", j, ":", k, l)
#                         time.sleep(1)
# useless()

# name = range(10,0,1)
# for i in name:
#     print(i)

# import random as rd
# def collect_data():

#     figure = input("input figures \n: ")
#     name = input("input name \n: ")
#     figure = figure.split(" ")
#     fig = map(lambda a: int(a), figure)
#     fid = list(fig)
#     print(fid)
#     rand = rd.randrange(fid[0],fid[1])
#     print(rand)
#     return rand, name

# def play():
#     tries = 0 #adds a counter and makes it empty at first

#     rand, name = collect_data()

#     while True:
#         guess_number = input("Guess number")
#         guess_number = int(guess_number)  #TYPE CASTING
#         tries += 1  #increment at every try

#         if guess_number == rand:
#             print("YOU WIN")
#             break

#         elif guess_number < rand:
#             print("Hint: YOUR NUMBER IS LESS")

#         elif guess_number > rand:
#             print("Hint: YOUR NUMBER IS MORE")

#         else:
#             pass
#     return name, tries 

# play()


# Write a guessing game in a function that displays a list of items and picks any at random, if the item picked is the same as the users guess, it should display 'you win' otherwise,'you lose'. 
import random as rd
# items = input("enter items here: ")
# itemss = items.split(" ")
# print(itemss)
def shuffle():
    name = input("what is your name?: ")
    print(f"Goodluck {name}")
    items = input("Input a list of items separaterd by a comma.: ")
    word = items.split(",")
    dom = rd.choice(word)
    print(f"This is your list: {word}")
    words = input("Guess a word out of your list: ")
    
    for i in dom:
        if i == words:
            print(f"You have successfully guessed the correct word: {words}")
            break
        elif i != words:
            print("Try again")
            pass
                
    


shuffle()