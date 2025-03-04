class Car:
    def __init__(self, name, fuel_rate, velocity):
        self.name = name
        self._fuel_rate = fuel_rate  # Private variable for fuel_rate
        self._velocity = velocity  # Private variable for velocity

    @property
    def fuel_rate(self):
        """Getter for fuel_rate."""
        return self._fuel_rate

    @fuel_rate.setter
    def fuel_rate(self, value):
        if 0 <= value <= 100:
            self._fuel_rate = value
        else:
            print("fuel rate must be between 0 and 100.")

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        if 0 <= value <= 200:
            self._velocity = value
        else:
            print("velocity must be between 0 and 200.")

    def run(self, velocity, distance):
        if self._fuel_rate <= 0:
            self.stop(distance)  # If there is no fuel, stop the car
            return

        self.velocity = velocity  # Set the car velocity
        fuel_consumed = distance * 0.1
        self._fuel_rate -= fuel_consumed  # decrease fuel rate

        if self._fuel_rate <= 0:
            self.stop(distance)  # Stop if fuel is consumed
        else:
            print(f"The car is running at {velocity} km/h for {distance} km.")
            print(f"Remaining fuel: {self._fuel_rate}%")

    def stop(self, distance):
        print(f"the car has stopped and remaining distance {distance} km")
        self.velocity = 0

