# # question 3A
# get_data = input()
# print(get_data)

# gett_data = get_data.split(" ")
# print(gett_data)
# new_data = list(map(lambda h : int(h), gett_data))
# print(new_data)

# even_numbers, odd_numbers = 0, 0
# numeric = 0
# while(numeric <len(new_data)):
#     if new_data[numeric] %2 == 0:
#         even_numbers += 1
#     else:
#         odd_numbers += 1
#     numeric += 1
# print(even_numbers)
# print(odd_numbers)

# # question 3B
# artist = "6lack"
# digits = letters = 0
# for tw in artist:
#     if tw.isdigit():
#         digits = digits +1
#     elif tw.isalpha():
#         letters = letters +1
#     else:
#         pass
# print("Letters:", letters)
# print("Digit:", digits)

# CORRECTION
# get_data = input("Enter integers here: ")
# con_list = get_data.split(" ")

# real_integers = list(map(lambda a: int(a), con_list))
# odd_numbers = list(filter(lambda a: a % 2, real_integers))

# no_of_inputs = len(real_integers)
# no_of_odd = len(odd_numbers)
# no_of_even = no_of_inputs - no_of_odd
# print(f"There are {no_of_odd} odd numbers.")
# print(f"There are {no_of_even} even numbers")

# odd = 0
# even = 0
# for entry in real_integers:
#     if entry % 2 == 0:
#         even += 1
#     elif entry % 2 != 0:
#         odd += 1
#     else:
#         pass

# print("there are {} odd numbers".format (odd))
# print(f"there are {even} even numbers")

# 2
word = input()
words = word.split(" ")
print(words)
inpu = "".join(words)
print(inpu)
lend = len(inpu)
inp = list(filter(lambda a : a.isalpha(), inpu))
land = len(inp)
ans = lend - land
print(f"there are {land} letters")
print(f"there are {ans} digits")

