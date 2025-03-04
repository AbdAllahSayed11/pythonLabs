from car import Car
from lab1 import Employee
from office import Office

my_car = Car("BMW", 50, 120)

employee1 = Employee(101, "Samy", 32, 3000, "happy", 80, my_car, "samy@gmail.com", 3000, 60)

office = Office("OS")

# office.hire(employee1)
office = Office("OS")

employees = office.get_all_employees()
for emp in employees:
    print(f"Employee: {emp.name}, Age: {emp.age}")

