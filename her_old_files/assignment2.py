# question 2B
arithmetic = 78 + 4 * 18 - 23**4
print(arithmetic)

# question 2C
yam = 1500
egg = 1100

verdict = (yam + egg < 2450) or (egg /2 > yam /3)
print(verdict)

# QUESTION 2D
list_1 = [21, 67, 24, 94, 21, 55, 67, 88, 88, 92, 20, 45, 55]
print(list_1[2])
print(list_1[3])
print(list_1[9])
print(list_1[10])
print(list_1[11])

# QUESTION 2Dii
print(list_1[0])

# question2E
my_data = (51, 69, 64, 30, 79, 20, 4, 90)
step_one = list(my_data)
step_one.sort()
need_integer = step_one.pop(5)
step_one.insert(2, need_integer)

step_two = tuple(step_one)
print(step_two)

# question 2F
first_list = [13, 48, 9, 98, 77, 34, 45, 6]
second_list =[22, 90, 41, 53, 66, 14, 19, 7, 72, 54]

final_list = first_list[ : : 2] + second_list[1: : 2]
print(final_list)


