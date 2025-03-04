# # lab1 python - Q1
# print("hello sara") ;
# # chara=('a', 'e', 'i', 'o', 'u') ;
#  def num_vowel (words):
#         vowel="aeiou";
#         count = 0 ;
#
# # words =("Hello World Abdallah")
#
#  for char in words:
#         if char in vowel:
#             count += 1
#
#     return count
#
# words = input("enter what you want  ") ;
# print( {num_vowel(words)})
###########################//\\//\\//\\//\\//\\//\\//\\//\\//\\#########################
#Q1
# def num_vowel(words):
#     vowels = "aeiou"
#     count = 0
#
#     for char in words:
#          if char in vowels:
#             count += 1 ;
#
#     return count
# words = input("enter what you want ")
#
# print( {num_vowel(words)})
# from operator import indexOf


# Q2
#
# def aear (length , start):
#     list[];
#     if length == list.lenght() :
#         list[index]=start ;
#
#  list = input (enter yout element in the array )

# def arr(length, start):
#     return [start
#             for i in range(length)]
#
# result = arr (5, 10)
# print(result)

# Q3
#
# n = int(input("enter size of array "))
# array = []
# for i in range(n):
#     element = input( {i} )
#     array.append(element)
# array.sort()
# print("sorted array",array)
# array.reverse()
# print ("reversed",array)


# Q4
# def fizz_bizz(num):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FIZZ BIZZ")
#     elif num % 3 == 0:
#             print("fizz")
#     elif num % 5 == 0:
#          print("bizz")
#     else:
#           print("no devided")
#
# x = 15
# fizz_bizz(x)
# requrment . text self study

 #Q5
# def rev():
#     user_input = input(" enter string ")
#     rev_string = user_input[::-1] # hereeee to reverse the string
#     return rev_string
# print(rev())

#Q6
# import math
# def cal_circle():
#     radius = float(input("enter the radius "))
#     area = math.pi * (radius ** 2)
#     mohet = 2 * math.pi * radius
#
#     print(f"area of circle {area}")
#     print(f"mohet of circle: {mohet}")
# cal_circle()

#Q7
# name = input("please enter name ")
# while not name or name.isdigit():
#     print("name cannot be empty or a number")
#     name = input("please enter name ")
#
# email = input("please enter email")
#
# print(f"Name: {name}")
# print(f"Email: {email}")

#Q8
# pattern = "iti";
# s="hello iti and hello iti ";
# count =0
# for word in s.split() :
#     if word ==pattern:
#         count +=1 ;
# print (count);


#lab2 --

#Q1

#
# def pattern (arg,char) :
# indexs=[]
#     for char in enumerate(arg):
#         if char == pattern:
#     # count +=1 ;
#         indexs = [arg.index()];
#     return (indexs)
#
# pattern = "i";
# str="hello iti and hello iti";
# # count =0
# print (str,pattern)

###################################################\/\/\//\/\/\/\/\/\/\####################################################
#Q1 lab2
# def find (arg, char):
#     indexs =[]
#     for index, c in enumerate(arg):
#         if c == char:
#             indexs.append(index)
#     return indexs
#
# pattern = "i"
# str = "hello iti and hello iti"
#
# print (find(str,pattern));

#Q2
# def multi(num):
#     results = []
#     for i in range(1, num +1):
#             innerResults = []
#             for j in range(1, i + 1):
#                 innerResults.append(i * j)
#             results.append(innerResults)
#     return results
#
# print(multi(4))

#Q3
# words = ["Abdallah","Sayed","Thabet"]
#
# my_dict = {item[0] :item for item in words}
#
# print(my_dict)
###################################################\/\/\/\/\/\/\/\\//\/\/\/\/\/####################################################
#lab3
class Person:
    def __init__(self, name, age, money, mood, healthRate):
        self.name = name
        self.age = age
        self.money = money
        self.mood = mood
        self.healthRate = healthRate

    def myfunc(self):
        print("My name is " + self.name)

    mood = ("happy", "sad", "tired")

    def sleep(self, hours):
        if hours == 7:
            self.mood = "happy"
        elif hours < 7:
            self.mood = "sad"
        else:
            self.mood = "tired"

    def eat(self, meals):
        if meals == 3:
            self.mood = "very very very happy"
            self.healthRate = 100
        elif meals == 2:
            self.mood = "happy"
            self.healthRate = 75
        elif meals == 1:
            self.mood = "sad"
            self.healthRate = 50

    # @property
    # def healthRate (self) :
    #     return self.healthRate
    # @property.setter
    # def sethethRate (self,rate) :
    #     if rate in range (1,100):
    #         self.healthRate = rate
    #     else :
    #         print ("you can not set this rate")
###

class Employee(Person):
    def __init__(self, id, name, age, money, mood, healthRate, car, email, salary, distanceToWork):
        super().__init__(name, age, money, mood, healthRate)
        self.id = id
        self.car = car  # boject of car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork


    status = ("happy", "normal", "tired")
    def work(self, hour):
        if hour < 7:
            self.status = "tired"
        elif hour == 7:
            self.status = "normal"
        else:
            self.status = "happy"

    def drive(self, distance, velocity):
        print(f"{self.name} is driving the car.")
        self.car.run(velocity, distance)

    def refuel(self, gas_amount=100):
        new_fuel_rate = self.car.fuel_rate + gas_amount
        if new_fuel_rate > 100:
            self.car.fuel_rate = 100  # Cap the fuel rate to 100
        else:
            self.car.fuel_rate = new_fuel_rate

    def send_mail(self, To, content):
        print(f"{self.name} sends email to {To}. Content: {content}")


        @property
        def salary(self):
            return self._salary

        @salary.setter
        def salary(self, value):
            if isinstance(value, int):  # Ensure that salary is an integer
                if value >= 1000:
                    self._salary = value
                else:
                    print("salary must be at least 1000")
            else:
                print("salary should be an integer")

# test
#
# p1 = Person("Samy", 30, 3000, "happy", "good")
# print(p1.age)
# p1.myfunc()
# p1.sleep(8)
# p1.eat(2)
# p1.eat(3)
# print (p1.mood)
# p1.buy(500)
#
# # Creating an Employee object
# e1 = Employee("samy", 28, 5000, "excited", "excellent", 101, "samy@gmail.com", 500, 10)
# e1.myfunc()
# e1.work(10)
# e1.drive(20,80)
# e1.refuel()
# e1.send_mail("manager@example.com", "Project Update")





