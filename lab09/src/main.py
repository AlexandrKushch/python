class Engine:
    volume: float
    horse_power: int

    def __init__(self, volume, horse_power):
        self.volume = volume
        self.horse_power = horse_power

    def __str__(self):
        return f"Volume: {self.volume}; HP: {self.horse_power}"


class Car:
    model: str
    is_mechanic: bool
    year: int
    engine: Engine

    def __init__(self, model, is_mechanic, year, volume, horse_power):
        self.model = model
        self.is_mechanic = is_mechanic
        self.year = year
        self.engine = Engine(volume, horse_power)

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


tesla1 = Car("S", False, 2018, 2.2, 120)
tesla2 = Car("E", False, 2013, 1.6, 80)
tesla3 = Car("T", False, 2022, 3.3, 220)

teslas = [tesla1, tesla2, tesla3]
write_f(teslas, '1.txt')

# print('First car:', tesla1)

teslas_r = read_f('1.txt')
print('Car was read from file:', teslas_r)
# print('Prise:', tesla1.price())
