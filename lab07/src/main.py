import time
import datetime
import random


REGISTERED = []


def count_time(arg):
    print(arg)

    def over(function):
        def wrapper():
            start = datetime.datetime.now()
            function()
            end = datetime.datetime.now()
            print(end - start)
        return wrapper
    return over


def reply(function):
    def wrapper(*args, **kwargs):
        while function(*args, **kwargs) == 0:
            pass
    return wrapper


def is_decorated(function):
    def wrapper(*args, **kwargs):
        REGISTERED.append(function.__name__)
        function(*args, **kwargs)
    return wrapper


@reply
@is_decorated
def several(p):
    if 0 <= p <= 100:
        num = random.randint(0, 100)
        if num <= p:
            return 1
    return 0


@count_time("Show arguments")
@is_decorated
def wait():
    time.sleep(2)


wait()
several(40)
print(REGISTERED)
