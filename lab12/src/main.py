from lab10_11.src.main import Car


class Iterator:
    _list: list
    _i: int

    def __init__(self, _list):
        self._list = _list

    def __iter__(self):
        self._i = 0
        return self

    def __next__(self):
        if self._i < len(self._list):
            res = self._list[self._i]
            self._i += 1
            return res
        else:
            raise StopIteration


class Generator(Iterator):
    def generate(self, it):
        for self.it in self._list:
            yield self.it


class Manager:
    def __init__(self, file_name, mode='r'):
        self.file = open(file_name, mode=mode)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.file.close()


def write_car(iterator, file_name):
    try:
        with Manager(file_name, mode='w') as file:
            for i in iterator:
                file.write(f"{i.model} {i.transmission()} {i.year} {i.engine.volume} {i.engine.horse_power}\n")
    except FileNotFoundError as e:
        print(e)


def read_car(file_name):
    result = []
    try:
        with Manager(file_name, mode='r') as f:
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


c1 = Car('S', True, 1990, 1.6, 79)
c2 = Car('T', True, 2000, 2.2, 103)
c3 = Car('V', False, 2010, 3.3, 250)

cars = [c1, c2, c3]
it = Iterator(cars)

print("iterator")
for i in it:
    print(i)

print("iterator")
for i in it:
    print(i)

gt = Generator(cars)
generated_cars = gt.generate(it)
print("generator")

for i in generated_cars:
    print(i)

file_name = '1.txt'
write_car(it, file_name)

read_cars = read_car(file_name)

print("Read cars")
for i in read_cars:
    print(i)
