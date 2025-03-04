from config import connect_to_mysql
from lab1 import Employee

class Office:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def get_all_employees(self):
        db = connect_to_mysql()
        cursor = db.cursor()

        cursor.execute("SELECT * FROM Employee WHERE office_name = %s", (self.name,))
        rows = cursor.fetchall()

        employees = []
        for row in rows:
            emp = Employee(
                id=row[0],
                name=row[1],
                age=row[2],
                money=row[3],
                mood=row[4],
                healthRate=row[5],
                car=None,  # Assuming you need to handle car separately
                email=row[9],
                salary=row[10],
                distanceToWork=row[11]
            )
            employees.append(emp)

        db.close()
        return employees

    def get_employee(self, employee_id):
        db = connect_to_mysql()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Employee WHERE id = %s", (employee_id,))
        employee_data = cursor.fetchone()
        db.close()
        if employee_data:
            return Employee(*employee_data)
        return None

    def hire(self, employee):
        db = connect_to_mysql()
        cursor = db.cursor()

        #  car attributes
        car_name = employee.car.name
        car_fuel_rate = employee.car.fuel_rate
        car_velocity = employee.car.velocity
        cursor.execute(
            "INSERT INTO Employee (id, name, age, money, mood, healthRate, car_name, car_fuelRate, car_velocity, email, salary, distanceToWork, office_name) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (
                employee.id,
                employee.name,
                employee.age,
                employee.money,
                employee.mood,
                employee.healthRate,
                car_name,
                car_fuel_rate,
                car_velocity,
                employee.email,
                employee.salary,
                employee.distanceToWork,
                self.name
            )
        )
        db.commit()
        db.close()

        print(f"{employee.name} has been hired at {self.name}.")

    def fire(self, employee_id):
        db = connect_to_mysql()
        cursor = db.cursor()
        cursor.execute("DELETE FROM Employee WHERE id = %s", (employee_id,))
        db.commit()
        db.close()
        print(f"Employee with ID {employee_id} has been fired from {self.name}")
