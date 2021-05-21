from abc import ABC, abstractmethod


class CarException(Exception):
    pass


class StartCar(CarException):
    pass


class Carcass(ABC):
    def drive(self):
        pass

    def lock(self):
        pass

    def park(self):
        pass

    @staticmethod
    def reverse():
        print('This car is riding reverse')


class Engine:
    volume: float
    horse_power: int

    def __init__(self, volume, horse_power):
        self.volume = volume
        self.horse_power = horse_power

    def __str__(self):
        return f"Volume: {self.volume}; HP: {self.horse_power}"


class Car(Carcass):
    fuel = 40
    model: str
    is_mechanic: bool
    year: int
    engine: Engine

    def __init__(self, model, is_mechanic, year, volume, horse_power):
        self.model = model
        self.is_mechanic = is_mechanic
        self.year = year
        self.engine = Engine(volume, horse_power)

    def work(self):
        self.drive()
        self.reverse()
        self.park()
        self.lock()

    def price(self):
        start_price = 1000

        if self.is_mechanic:
            start_price -= 100
        else:
            start_price += 100

        if self.year >= 2010:
            start_price += 100
        elif 2000 <= self.year < 2010:
            start_price += 50
        else:
            start_price -= 100

        if self.engine.volume > 2.0 and self.engine.horse_power > 200:
            start_price += 300
        else:
            start_price -= 300

        return start_price

    def transmission(self):
        if self.is_mechanic:
            return "Mechanical"
        else:
            return "Automatic"

    def drive(self):
        if self.fuel > 5:
            print("Car " + self.model + " is driving")
            self.fuel -= 5
        else:
            raise StartCar("Not enough fuel for driving")

    def lock(self):
        print("Car " + self.model + " has been locked")

    def park(self):
        print("Car  " + self.model + " has been parked")

    def __repr__(self):
        return f"Car Model: {self.model}"

    def __str__(self):
        return f"Model: {self.model}; Transmission: {self.transmission()}; Year: {self.year}; {self.engine}"


def write_f(cars, file_name):
    try:
        with open(file_name, 'w') as f:
            for car in cars:
                f.write(f"{car.model} {car.transmission()} {car.year} {car.engine.volume} {car.engine.horse_power}\n")
    except FileNotFoundError as e:
        print(e)


def read_f(file_name):
    result = []
    try:
        with open(file_name, 'r') as f:
            for line in f:
                attributes = line.split(' ')

                if attributes[1] == "Mechanical":
                    attributes[1] = 'True'
                else:
                    attributes[1] = ''

                result.append(Car(attributes[0], bool(attributes[1]), int(attributes[2]), float(attributes[3]), int(attributes[4])))
    except FileNotFoundError as e:
        print(e)

    return result


# c = Car('S', True, 1990, 1.5, 75)
#
# c.work()
# print(c.fuel, end=" ")
# print(c.model)
# print(Car.fuel, end=" ")
# print(Car.model)
