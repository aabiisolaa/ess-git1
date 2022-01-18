first_integer = 99
# print (first_integer)
real_life = "this stuff is sort of confusing"
# print (real_life)
my_verdict = True
# print(my_verdict)

randoms = [5, 'aiko', "big", True, 2.56] 
# print(randoms)

states = {"Abia", "Kogi", "Abuja"}
# print(states)

my_info = {"name" : "Lola", "gender" : "Female", "age" : 5}
# print(my_info)

the_remainder = 55 % 6
# print(the_remainder)

the_quotent = 55 // 6
# print(the_quotent)

comparison = 59 == 91
# print(comparison)

logical = (22 >= 71) or (92 != 92)
# print(logical)

feedback = 25 is 25
# print(feedback)

first = [29, "True", "Sunny"]
second = [29, "True", "Sunny"]
# print(first)
# print(second)

check_member = "e" in "money"
# print(check_member)

list_of_scores = [63, 78, 90, 52, 99, 81]
check_score = 90 in list_of_scores
# print(check_score)

first_phrase = "The boy"
second_phrase = "in my class is handsome"

full_sent = first_phrase + " " + second_phrase
# print(full_sent)

new_chunk = full_sent[3:11]
# print(new_chunk)

new_chunk = first_phrase [ : : 2]
# print(new_chunk)

new_chunk = full_sent [-23 : -12]
# print(new_chunk)

weather = "sunny"
temperature = "39 degrees"
weather_report = "It is quite {} with a temperature of {}". format (weather, temperature)
# print(weather_report)

# using f string
weather_report2 = f"It is quite {weather} with a temperature of {temperature}"
# print(weather_report2)

soure_of_income = 'The nation\'s crude oil'
# print(soure_of_income)

new_weather_report = "!It is quite sunny despite the downpour all through the night!"
mod_one = new_weather_report.title()
# print(mod_one)

mod_two = new_weather_report.startswith("It ")
# print(mod_two)

mod_three = new_weather_report.index("night")
# print(mod_three)

mod_four = new_weather_report.find("day")
# print(mod_four)

mod_five = new_weather_report.split(" ")
# print(mod_five)

mod_six = new_weather_report.split("downpour")
# print(mod_six)

mod_seven = ",".join(mod_five)
# print(mod_seven)

mod_eight = new_weather_report.count("the")
# print(mod_eight)

mod_nine = new_weather_report.replace("p" , "f")
# print(mod_nine)

mod_ten = new_weather_report.lstrip("!")
# print(mod_ten)

new_collection = [6, True, 12, 9, False, "name", "Bentley", "Football", None, 9.7, 8.5]

desired_item = new_collection[4]
# print(desired_item)

desired_portion = new_collection[-6: -2: 2]
# print(desired_portion)

new_collection[5] = "School"
# print(new_collection)

new_collection[1 : : 3] = ["Money", "Food", "Ikoyi", "Glass"]
# print(new_collection)

first_list = [1, 2, 3]
second_list = [7,8,9]
full_list = first_list + second_list
# print(full_list)

sports = ["Basketball", "Boxing", "Swimming"]
stars = ["Kobe Bryant", "Mike Tyson", "Michael Phelps"]
sports.extend(stars)
# print(sports)

new_collection.remove(9)
# print(new_collection)

new_collection.append("Biscuit")
# print(new_collection)

backup_collection = new_collection.copy()
# print(backup_collection)

new_collection.insert(2, "Holiday")
# print(new_collection)

integers = [2, 4, 7, 6, 8]
integers.sort(reverse= True)
# print(integers)

# TUPLES
scores= (58, 73, 85, 67)
desired_score = scores[-1]
# print(desired_score)

# SETS
grocery_cart1 = {"Ham", "Burger", "Yoghurt", "Eggs", "Cookies", "Bread", "Sausage"}
grocery_cart2 = {"Beverage", "Cookies", "Wine", "Frozen Turkey", "Burger", "Eggs"}
# print(grocery_cart1)
# print(grocery_cart2)

grocery_cart1.discard("Ham")
grocery_cart1.add("Cheese")
# print(grocery_cart1)

full_cart = grocery_cart1.union(grocery_cart2)
# print(full_cart)

# grocery_cart1.update(grocery_cart2)
# print(grocery_cart1)

# grocery_cart2.difference_update(grocery_cart1)
# print(grocery_cart2)

# common_groceries = grocery_cart1.intersection(grocery_cart2)
# # print(common_groceries)

# grocery_cart1.symmetric_difference_update(grocery_cart2)
# # print(grocery_cart1)

# # DICTIONARY
# customer_info = {
#     "name" :["Adam Freeman", " Alisa Banks", "Ngozi Chukwuma", "John Doe"],
#     "gender" : ["Male", "Female", "Female", "Male"],
#     "nationality" : ["American", "Canadian", "Nigerian" , "British"]
# }
# print(customer_info)
# all_names = customer_info["name"]
# print(all_names)
# all_names[2] = "Ngozi Nnamdi"
# print(customer_info)

# all_nationalities = customer_info.get("nationality")
# print(all_nationalities)

# all_entries = customer_info.items()
# print(all_entries)

# customer_info.update({"age" : [31, 24, 30, 22]})
# print(customer_info)


# BUILTIN FUNCTION
# get_data = input()
# print(get_data)

# get_data = input("Enter data here: ")
# print(get_data)
# random= get_data.split(" ")
# print(random)
# int_1 = int(random[0])
# int_2 = int(random[1])
# average = (int_1 + int_2)/2
# print(average)

# scores = [55, 2, 3]
# no_of_items = len(scores)
# print(no_of_items)

# numbers = sum(scores)
# print(numbers)

# name = ["John", "Dave", "Bill"]
# age = [22, 24, 26]
# zipped_object = zip(name, age)
# print(zipped_object)
# output = list(zipped_object)
# print(output)

# animals = ["Dog", "Cat", "Lion"]
# no_of_age = [5, 7, 10]
# zipped_animals = enumerate(animals)
# print(zipped_animals)
# output = list(zipped_animals)
# print(output)

# my_multiplier = lambda x : x * 2
# output = my_multiplier(20)
# print(output)

# checker = lambda a : a.startswith("is")
# output2 = checker("This is just a basic string")
# print(output2)

# upgraded_scores = map(lambda a : a + 2, scores)
# output3 = list(upgraded_scores)
# print(output3)

# list_of_names = ["steve", "dwayne", "freya", "nelson"]
# checker2 = map(lambda a : a.title(), list_of_names)
# output4 = list(checker2)
# print(output4)

# num = [20, 31, 45, 60, 10, 77]
# my_filter = filter(lambda x : x % 2, num)
# # print(list(my_filter))

list_of_names = ["steve", "dwayne", "freya", "nelson","sam", "john", "abu", "binta"]

# my_range = range(-10, -1, 2)
# print(list(my_range))

# get_data = input("Enter data here: ")
# con_list = get_data.split(" ")
# # to convert the numbers to actual integers
# new_list = list(map(lambda a : int(a), con_list))
# # to get rid of duplicates
# ammended_list = list(set(new_list))
# ammended_list.sort()

# output = ammended_list[-2]
# print(output)

# things = (["30" , "33"])
# print(type(things))
# thingss = str(["30", "33"])
# print(thingss)
# print(type(thingss))
# thingsss = thingss[7]
# print(thingsss)

# BUILT IN MODULES
# import time

# print("I love junks")
# time.sleep(8)
# print("I really love junks")

# Random
import random as rd
# rd.seed(99)
# print(list_of_names)
# print("\n")
# rd.shuffle(list_of_names)
# print("\n")
# print(list_of_names)

# random_pick = rd.choice(list_of_names)
# print(random_pick)

# multiple_picks = rd.sample(list_of_names, k = 4)
# print(multiple_picks)

# random_num = rd.randrange(9, 23, 3)
# print(random_num)

# DATTETIME
from datetime import datetime as dt

# current_dt = dt.now()
# print(current_dt)

# output = current_dt.year
# print(output)

# output = current_dt.strftime("%A")
# print(output)

# output= current_dt.strftime("%B")
# print(output)

# fake_date = "9/4/2021"

# real_date = dt.strptime(fake_date, "%d/%m/%Y")
# print(real_date)

notable_days = ["01/01/2021", "15/01/2021", "14/02/2021", "01/04/2021", "29/05/2021", "12/06/2021", "01/10/2021", "25/12/2021", "26/12/2021"]

# mapped = list(map(lambda a : dt.strptime(a , "%d/%m/%Y"), notable_days))
# print(list(mapped))

# # listt = list(mapped[0])
# print(mapped[0])

# if 77 > 77:
#     print("Yes")  
# else:
#     print("No")

# gett_data = input("Enter data here: ")

# if len(gett_data) == len(set(gett_data)):
#     print("There are no duplicates")
# else:
#     print("There are duplicates")

# get_data = input("Enter data here: ")

# if int(get_data) % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")

# if int(get_data) % 2 == 0 and int(get_data) > 20:
#     print("Both conditions are met")
# else:
#     print("They were not met")

# if int(get_data) % 2 == 0 and int(get_data) > 20:
#     print("Even number and greater than 20")
# elif int(get_data) % 2 != 0 and int(get_data) > 20:
#     print("Odd number and greater than 20")
# else:
#     print("Number is less than 20")

# cracker = 0 
# while(cracker < 5):
#     print("Cracker is less than 5")
#     cracker += 1


###LOOPS!!!
# cracker = 0 
# while (cracker < 5):
#     if cracker == 3:
#         print("This is my ride outta the loop!")
#         break
#     else:
#         print("Cracker is less than 5")
#         cracker += 1

### Task
# get_password1 = input("Enter password here: ")
# while True:
#     get_password2 = input("Repeat password here: ")
#     if get_password1 == get_password2:
#         print("Sign up successful")
#         break
#     else:
#         pass

# get_password1 = input("Enter password here: ")
# limit = 0
# while (limit < 2):
#     get_password2 = input("Repeat password here: ")
#     if get_password1 == get_password2:
#         print("Login successful")
#         break
#     else:
#         limit += 1

# figure = input("input figures here: ")
# figure = figure.split(" ")
# fig = map(lambda a: int(a), figure)
# fid = list(fig)
# print(fid)

# import random as rd
# rand = rd.randrange(fid[0],fid[1])
# print(rand)

# while True:
#     guess_number = input("Guess number")
#     guess_number = int(guess_number)
#     if guess_number == rand:
#         print("YOU WIN")
#         break
#     elif guess_number < rand:
#         print("Hint: YOUR NUMBER IS LESS")
#     elif guess_number > rand:
#         print("Hint: YOUR NUMBER IS MORE")
#     else:
#         pass    

# entry_data = "Universe"
# for a in entry_data:
#     print("home for all")

# new_list = ["pop", "rock", "country"]
# for item in new_list:
#     print(item)

# names = ["Sheldon", "Penny", "Howard", "Leonard", "Rajesh"]
# for index, item in enumerate(names):
#     print(item, index)

# burna = input()
# print(burna)
# boy = burna.split(" ")
# print(boy)
# burnaa = map(lambda u: int(u), boy)
# burnaa1 = list(burnaa)
# print(burnaa1)

# for index, entry in enumerate(burnaa1):
#     if entry % 2 == 0:
#         burnaa1[index] *= 0.9
#         print(burnaa1)
#     elif entry % 2 != 0:
#         burnaa1[index] *= 1.1
#         print(burnaa1)
#     else:
#         pass        

# num = (159000000)
# numb = str(num)
# print(numb)
# numm = map(lambda a: a.isdigit(), numb)
# nummm = list(numm)
# print(len(nummm))

# gret =  57.98
# grett = str(gret)
# print(grett)
# grettt = grett.split(".")
# print(grettt)
# gty = "".join(grettt)
# print(gty)
# print(len(gty))
# gre = list(map(lambda a: a.isdigit(), gty))
# print(gre)
# grt = len(gre)
# print(grt)

# ruger = input()
# bounce = ruger.split(" ")
# ounce = list(bounce)
# print(ounce)

# ounce.reverse()
# print(ounce)

# from datetime import datetime as dt
# random_date = "25/12/2021"

# ayra = input()
# print(ayra)
# geygey = dt.now().hour
# geygey = str(geygey)
# astalavi = dt.now().minute
# astalavi = str(astalavi)
# print(type(astalavi))
# holy = dt.now().second
# holy = str(holy)
# father = ayra + "/" + geygey + "/" + astalavi + "/" + holy
# print(father)
# normal = dt.strptime(father, "%d/%m/%Y/%H/%M/%S")
# print(normal)


#TASK: WRITE A PROGRAM THAT TAKES IN A DATE: Jun 30 2021 3:30pm, CONVERTS IT TO AN ACTUAL DATE AND ADDS THE TIME
# task = input()
# rate = dt.strptime(task, "%b %d %Y %I:%M%p")
# print(rate)

#LIST COMPREHENSION
#[expression for item in iterable]
#EXAMPLE:
# scores = [32, 41, 14, 16]
# upgrade = [num + 2 for num in scores]
# print(upgrade)

#EXAMPLE 2
# scores = [32, 41, 14, 16]
# upgraded = [num + 2 for num in scores if num %2 !=0]
# print(upgraded)


# for t in range(21):
#     print(t)

# for f in range(20, 0, -1):
#     print(f)

# import time

# for i in range(10):
#     for j in range(10):
#         for k in range(60):
#             for l in range(60):
#                 print(i, ":", j, ":", k, l)
#             # time.sleep(1)

# for i in range(10, 0, -1):
#         for j in range(10, 0, -1):
#             for k in range(60, 0, -1):
#                 for l in range(60, 0, -1):
#                     print(i, ":", j, ":", k, l)
#                     time.sleep(1)

# for i in range(1, 1000):
#     sum_num = i + i + i

#     place_holder = str(i)[-1]
#     triple_placeholder = place_holder * 3

#     if int(triple_placeholder) == sum_num:
#         print("YAY", sum_num)
#         break
#     print(i, sum_num, place_holder, triple_placeholder)
        

# num = 10
# word = "new"

# try:
#     print(num + word)

# except:
#     output = num * 3
#     print(output) 


# words = "I dont know how to"
# wordss = " deal with birthday anxiety"

# try:
#     sent = words - 2
#     print(sent)

# except:
#     print(words + wordss)
    
