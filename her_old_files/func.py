from xlwt.antlr import ifelse


def basic():
    print("Pretty basic function")

basic()

def left(a):
    print(a + 2)

left(2)

def password_1(a):
    print("a == password_2")
    password_1 = input("Enter password here")
    while True:
        password_2 = input("repeat password here")
        if password_1 == password_2:
            print("login successful")
            break
password_1("password_2")