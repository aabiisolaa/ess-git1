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

#     # write_to_file()
#     # print("You tried", tries)  #print tries

# def write_to_file(name, tries):
    
#     with open("database.csv", "a") as our_log_file: #file open context manager

#         our_log_file.write(f"{name}, {tries}\n")
#     # print("logged")


# # write_to_file("Bisola", 40)
# # play()

# def play_shot():
#     name, tries = play()
#     with open("database.csv", "a", newline = "") as our_file:
#         our_file.write(f"{name}: {tries} \n")
# play_shot()




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
    

#     write_to_file(name, tries)

# def write_to_file(name, tries):
    
#     with open("database.csv", "a") as our_log_file: #file open context manager

#         our_log_file.write(f"{name}, {tries}\n")
#     # print("logged")

# play()


import random as rd
import time
def collect_data():

    figure = input("input figures \n: ")
    name = input("input name \n: ")
    figure = figure.split(" ")
    fig = map(lambda a: int(a), figure)
    fid = list(fig)
    print(fid)
    rand = rd.randrange(fid[0],fid[1])
    print(rand)
    return rand, name

def play():

    limit = 1
    tries = 0 #adds a counter and makes it empty at first

    rand, name = collect_data()

    while limit <= 10:
        guess_number = input("Guess number")
        guess_number = int(guess_number)  #TYPE CASTING
        tries += 1  #increment at every try
        limit += 1

        if guess_number == rand:
            print("YOU WIN")
            break

        elif guess_number < rand:
            print("Hint: YOUR NUMBER IS LESS")

        elif guess_number > rand:
            print("Hint: YOUR NUMBER IS MORE")

        if limit == 10:
            print("You missed", tries)
            print("We are now delaying you")
            limit = 1
            time.sleep(10)
    

    write_to_file(name, tries)

def write_to_file(name, tries):
    
    with open("database.csv", "a") as our_log_file: #file open context manager

        our_log_file.write(f"{name}, {tries}\n")
    # print("logged")

play()