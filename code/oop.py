# class HumanKind:   #class creation

#     skin = True
#     eyes = True
#     legs = True
#     species = "mammal"

# human_kind_object = HumanKind()   #object creation class instantiation
# print(human_kind_object)
# another_name = HumanKind()   #object creation class instantiation
# print(another_name)

# print(human_kind_object.skin)
# print(human_kind_object.species)
# print(another_name.skin)
# print(another_name.species)

from typing import ValuesView
import winsound, time 
# class HumanKind:   #class creation

#     skin = True
#     eyes = True
#     legs = True
#     species = "mammal"

#     def describe(self):          #self points to the current instance of that class
#         print(f"Hello my dog is {self.species}")

#     def makenoise(self):
#         print("Hello")
#         winsound.Beep(700, 500)
#         time.sleep(1)
#         winsound.Beep(1000, 500)
#         time.sleep(1)
#         winsound.Beep(4000, 500)

        
# varname = HumanKind()
# varname.describe()
# varname.makenoise()

##create a class of cat with attributes name fur colour family and method describe that prints hello i am a cat, my fur colour is{fur colour}and my name is {name}
# class Cat:

#     name = "israel"
#     fur_colour = "grey"
#     family = "exoticshorthair"


#     def describe(self):
#         print(f"hello i am a cat, my fur colour is {self.fur_colour} and my name is {self.name}")

# meow = Cat()
# meow.describe()

import random
#instance attributes  attributes that are different and unique in its own way
# class Person:

#     #class attribute
#     species = "Homo-Sapien"
#     _class = "Mammal"

#     def __init__(self, name, complexion, height):

#         self.name = name
#         self.complexion = complexion
#         self.height = height
#         self.voice_freq = random.randint(50, 1500)

#     def unique(self):
#         print(f"Hello, my name is {self.name}. \n I am a {self._class}, and my height is {self.height}")
#         winsound.Beep(self.voice_freq, 500)
#         time.sleep(0.5)
#         winsound.Beep(self.voice_freq, 500)
#         time.sleep(0.5)
#         winsound.Beep(self.voice_freq, 500)

# person1 = Person(name = "Jim", complexion ="Brownskin", height="5ft9'")
# person1.unique()

        
# class EthnicMeal:
#     def igbo(self):       #instance method
#         print("Akpu")

#     def yoruba(self):
#         print("Amala")

#     def hausa(self):
#         print("Tuwo Shinkafa")


# meal_one = EthnicMeal()
# meal_one.hausa()


# class Student:
#     def __init__(self, name, gender, age):
#         self.name = name
#         self.gender = gender
#         self.age = age

#     def get_name(self):              #accessor instance method
#         return self.name

#     def get_gender(self):
#         return self.gender

#     def get_age(self):
#         return self.age

#     def set_name(self, value):        #mutator instance method
#         self.name = value

#     def set_gender(self, value):
#         self.gender = value

#     def set_age(self, value):
#         self.age = value


# stu_one = Student("Kelsey", "Female", 22)
# stu_two = Student("Bryan", "Male", 35)
# stu_three = Student("Ernie", "Male", 27)

# # print(stu_one.get_name())
# print(stu_two.get_age())
# stu_two.set_age(24)
# print(stu_two.get_age())


# class School:
#     no_of_students = 0           #class attributes
#     sum_of_scores = 0

#     def __init__(self, student_name, student_score):
#         self.student_name = student_name
#         self.student_score = student_score
#         School.increase_count()
#         School.sum_of_scores += self.get_student_score()

#     def get_student_name(self):
#         return self.student_name

#     def get_student_score(self):
#         return self.student_score

#     def set_student_name(self, value):
#         self.student_name = value

#     def set_student_score(self, value):
#         self.student_score = value

#     @classmethod            #decorator is used to show class method
#     def increase_count(cls):
#         cls.no_of_students += 1

#     @classmethod
#     def average_score(cls):
#         output = cls.sum_of_scores / cls.no_of_students
#         return round(output, 2)


# edu_one = School("Emeka", 24.56)
# edu_two = School("Oluwagbemisola", 99.00)
# print(School.no_of_students)
# print(School.sum_of_scores)
# print(School.average_score())

# instance_collection = [School("Ifeoma", 64.22), School("Musa", 76.99), School("Bamishe", 58.40)]
# print(instance_collection[1].get_student_score())


##write a class that takes in user's personal info and writes it into a csv file. (name, gender, age, location). If the user can supply the name and age correctly, create an avenue to change the location.

# import csv
# class Info:

#     def __init__(self, name, gender, age, location):
#         self.name = name
#         self.gender = gender
#         self.age = age
#         self.location = location
#         self.cfile()


#     def cfile(self):
#         files = open("C:/Users/User/Desktop/univel city/code/task.csv", mode = "w",  encoding = "utf-8", newline = "")
#         kun = csv.writer(files)
#         kun.writerow(["Name", "Gender", "Age", "Location"])
#         kun.writerow([self.name, self.gender, self.age, self.location])



#     def get_name(self):
#         return self.name

#     def get_age(self):
#         return self.age

#     def get_location(self):
#         return self.location

#     def set_location(self, place):
#         self.location = place


# vidual = Info(input("Input name: "), input("input gender: "), input("input age: "), input("input location: "))
# print(vidual)


##Inheritance
# class Staff:
#     def __init__(self, name, gender, age):
#         self.name = name
#         self.gender = gender
#         self.age = age

#     def status(self):
#         print("I am a registered staff")

#     def get_name(self):
#         return self.name


# class Manager(Staff):
#     def __init__(self, name, gender, age, department, level):
#         super().__init__(name, gender, age)
#         self.department = department
#         self.level = level
            
#     def role_dist(self):
#         print("I distribute roles!")


# m_one = Manager("Aliyah", "Female", 30, "I.T", 3)   #for the child class
# m_one = Manager("Lisa", "Female", 25)
# m_one.role_dist()      #method
# m_one.status()          #method
# print(m_one.get_name())              #to get the name

