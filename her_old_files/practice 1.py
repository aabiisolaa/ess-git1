# new_integer = 59
# # print(new_integer)

# new_string = "hope this goes well"
# # print(new_string)

# new_float = 0.59
# # print(new_float)

# new_boolean = False
# # print(new_boolean)

# new_list = [5.9, 65, "yes", 'no', True]
# # print(new_list)

# new_tuple = ("hope", 'goal', "easy", 1)
# print(new_tuple)

# new_set = {"cookies", "junks", "stuff", 'sugar'}
# # print(new_set)

# new_dict = {"name" : "teyana", "gender" : "female", "age" : 30}
# # print(new_dict)

# new_modulus = 32 % 5
# print(new_modulus)

# new_floor = 32 // 5
# # print(new_floor)

# new_assignment = 25 - 5
# # print(new_assignment)

# new_comparison = 66 == 11
# # print(new_comparison)

# new_logical = 77 > 84 and 52 < 4
# # print(new_logical)

# logical_2 = 59 != 59 or 72 > 24
# # print(logical_2)

# logical_3 = 34 < 12 or 23 > 37
# # print(logical_3)

# logical_4 = not(62 >= 71 and 89 < 72)
# # print(logical_4)

# identity = 56 is 92
# # print(identity)

# identity2 = 30 is not 52
# # print(identity2)

# new_first = [50, "False", "Rainy"]
# new_second = [50, "False", "Rainy"]
# # print(new_first)
# # print(new_second)

# membership = "ds" in "friends"
# # print(membership)

# membership2 = {23, 59, 8, 16}
# check = 6 in membership2
# # print(check)

# conc1 = "Just keep practicing"
# conc2 = "your work"
# full_conc = conc1 + " " + conc2
# # print(full_conc)

# new_conc = full_conc[5:11]
# # print(new_conc)

# new_conc = conc1[ : : 3]
# # print(new_conc)

# new_conc = full_conc[-19 : -3]
# # print(new_conc)

# food = "pasta"
# taste = "spicy"
# food_feedback = "The {} tastes really {}".format(food, taste)
# # print(food_feedback)

# # USING F STRING
# new_food_feedback = f"The {food} tastes really {taste}"
# # print(new_food_feedback)

# new_escape = 'The sky\'s blue'
# # print(new_escape)

# food_feedback2 = ",the food tastes really spicy and it is still so hot,"
# mod_one = food_feedback2.title()
# # print(mod_one)

# mod_two = food_feedback2.upper()
# # print(mod_two)

# mod_three = food_feedback2.startswith("the")
# # print(mod_three)

# mod_four = food_feedback2.index("still")
# # print(mod_four)

# mod_five = food_feedback2.find("the")
# # print(mod_five)

# mod_six = food_feedback2.split(" ")
# # print(mod_six)

# mod_seven = food_feedback2.split("it")
# # print(mod_seven)

# mod_eight = ".".join(mod_six)
# # print(mod_eight)

# mod_nine = food_feedback2.count("tastes")
# # print(mod_nine)

# mod_ten = food_feedback2.replace("t" , "a")
# # print(mod_ten)

# mod_eleven = food_feedback2.rstrip(",")
# # print(mod_eleven)

# listt = [59, "donut", 8.2, True, 92, False, "people", "sky", 6.7]

# # item = listt[2]
# # print(item)

# portion = listt[-7: -2: 2]
# # print(portion)

# # listt[4] = "soda"
# # print(listt)

# # listt[1 : : 2] = ["see", "use", "goal", "pay"]
# # print(listt)

# firstt = [4, 7, 8]
# secondd = [6, 2, 5]
# full = firstt + secondd
# # print(full)

# sportss = ["Wrestling", "Football", "Basketball"]
# starss = ["Becky Lynch", "Sallah", "Tristan Thompson"]
# sportss.extend(starss)
# # print(sportss)

# listt.remove(False)
# # print(listt)

# listt.append("Babies")
# # print(listt)

# backup_list = listt.copy()
# # print(backup_list)

# listt.insert(4, "Plain")
# # print(listt)

# integerss = [4, 10, 7, 5]
# integerss.sort(reverse = False)
# # print(integerss)

# listt.pop(3)
# # print(listt)


# # TUPLES
# marks = (20, 15, 13, 19,)
# desired_marks = marks[2]
# # print(desired_marks)

# marks.count(1)
# # print(marks)

# # SETS
# wrestlers1 = {"Seth", "Brock", "Roman", "Ambrose", "Bayley", "Finn", "kingston", "Mysterio"}
# wrestlers2 = {"Sasha", "Bayley", "Charlotte", "Ripley", "Asuka", "Alexa", "Seth"}
# # print(wrestlers1)
# # print(wrestlers2)

# wrestlers1.discard("Brock")
# wrestlers1.add("Usos")
# # print(wrestlers1)

# all_wrestlers = wrestlers1.union(wrestlers2)
# # print(all_wrestlers)

# wrestlers1.update(wrestlers2)
# # print(wrestlers1)

# wrestlers2.difference_update(wrestlers1)
# # print(wrestlers2)/

# common_wrestlers = wrestlers1.intersection(wrestlers2)
# # print(common_wrestlers)

# wrestlers1.symmetric_difference_update(wrestlers2)
# # print(wrestlers1)

# # DICT
# infos = {
# "names" : ["Khloe Kardashian", "Tom Ford", "Daniel Bryan"],
# "genders" : ["Female", "Male", "Male"],
# "nationality" : ["American", "Canadian", "French"]
# }
# # print(infos)

# all_names = infos["names"]
# # print(all_names)
# all_names[2] = "Kendall Jenner" 
# # print(all_names)

# all_genders =  infos.get("genders")
# # print(all_genders)

# people = infos.items()
# # print(people)

# infos.update({"age" : [38, 42, 25]})
# # print(infos)

# # BUILT-IN FUNCTIONS
# get_dataa = input("Enter data here: ")
# print(get_dataa)
# dataa = get_dataa.split(" ")
# print (dataa)
# int_1 = int(dataa [0])
# int_2 = int(dataa [3])
# average = (int_1 + int_2)/2
# print(average)

# marks = [1, 7, 90, 2]
# numbers = len(marks)
# print(numbers)

# total = sum(marks)
# print(total)

# names = ["Kourtney", "Khloe", "Kendall"]
# age = [42, 37, 25]
# zipped = zip(names, age)
# new_list = list(zipped)
# print(new_list)

# actors = ["Kira", "Ebony", "Novi"]
# ages = [23, 33, 34]
# en = enumerate(actors)
# lists = list(en)
# print(lists)

# fun = lambda p: p + 12
# fund = fun(32)
# print(fund)

# try1 = lambda x: x.title()
# try2 = try1("back in office")
# print(try2)

# some = [5, 8 ,72]
# upgrade = map(lambda r : r * 3, some)
# upgraded = list(upgrade)
# print(upgraded)

# numerics = [34, 5, 7, 91]
# fill = filter(lambda t : t % 2, numerics)
# fills = list(fill)
# print(fills)

people = ["Jasmine", "Freda", "Steven", "Tami", "Yusef", "North"]

# ran = range(-16, -3, 3)
# print(list(ran))

# BUILT IN MODULES
# import time
# print("never forget")
# time.sleep(10)
# print("from the regular")

# Random
# import random as rd
# rd.seed(4)
# print(people)
# print("\n")
# rd.shuffle(people)
# print(people)

# pick = rd.choice(people)
# print(pick)

# choose = rd.sample(people, k =5)
# print(choose)

# roll = rd.randrange(5, 20, 2)
# print(roll)

# DATETIME
from datetime import datetime as dt
# present = dt.now()
# print(present)

# presen = dt.now().hour
# print(presen)

# put = present.year
# print(put)

# putt = present.strftime("%a")
# print(putt)

# fave = present.strftime("%x")
# print(fave)

# date = "22/3/2021"

# main = dt.strptime(date, "%d/%m/%Y")
# print(main)

# if 56 < 2:
#     print("yes")
# else:
#     print("no")

# if "lamba" == "lamb" or 22 > 12:
#     print("true")
# else:
#     print("not met")

# away = input("Enter data here: ")

# if int(away) != 4 and int(away) < 13:
#     print("met")
# elif int(away) == 4 or int(away) < 13:
#     print("not met")
# else:
#     print("greater than 13")
    
