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

    def prise(self):
        start_prise = 1000

        if self.is_mechanic:
            start_prise -= 100
        else:
            start_prise += 100

        if self.year >= 2010:
            start_prise += 100
        elif 2000 <= self.year < 2010:
            start_prise += 50
        else:
            start_prise -= 100

        if self.engine.volume > 2.0 and self.engine.horse_power > 200:
            start_prise += 300
        else:
            start_prise -= 300

        return start_prise

    def transmission(self):
        if self.is_mechanic:
            return "Mechanical"
        else:
            return "Automatic"

    def __repr__(self):
        return f"Car Model: {self.model}"

    def __str__(self):
        return f"Model: {self.model}; Transmission: {self.transmission()}; Year: {self.year}; {self.engine}"


def write_f(car, file_name):
    try:
        with open(file_name, 'w') as f:
            f.write(f"{car.model} {car.transmission()} {car.year} {car.engine.volume} {car.engine.horse_power}")
    except FileNotFoundError as e:
        print(e)


def read_f(file_name):
    try:
        with open(file_name, 'r') as f:
            line = f.readline()
            attributes = line.split(' ')

            if attributes[1] == "Mechanical":
                attributes[1] = 'True'
            else:
                attributes[1] = ''

            result = Car(attributes[0], bool(attributes[1]), int(attributes[2]), float(attributes[3]), int(attributes[4]))
    except FileNotFoundError as e:
        print(e)

    return result


tesla = Car("S", False, 2018, 2.2, 120)
print('First car:', tesla)
write_f(tesla, '1.txt')
tesla_r = read_f('1.txt')
print('Car was read from file:', tesla_r)
print('Prise:', tesla.prise())
