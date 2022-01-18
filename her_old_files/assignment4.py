# 4A
figures = []
for s in range(148, 599):
    new_figures = str(s)
    if (int(new_figures[0])%2!=0) and (int(new_figures[1])%2!=0) and (int(new_figures[2])%2!=0):
        figures.append(new_figures)
print(",".join(figures))

# 4B
e = int(input("Enter data here: "))
num = 0
while (e > 0):
    ber = e % 10
    num = num * 10 + ber
    e = e // 10
print("the reverse of the number: ", num)

# 4C
cap = ("faSHIoN")
caps = (list(cap))
print(caps)
caps.sort(reverse = True)
print(str(caps))
no = "".join(caps)
print(no)

# 4D
digits = {55, 99, 77, 44, 33, 88, 11, 66}
some = filter(lambda x : x % 2 != 0, digits)
print(list(some))