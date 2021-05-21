# Наслідування та поліморфізм у Python
# Лабораторна робота № 10-11
### Ціль: розширити попередню роботу абстрактним класом, та класами спадкоємець, додати статичні методи та реалізувати ієрархію виключень1

1. Абстрактний клас "Каркас" має методи управління каркасом(**drive, lock, park**). Та метод зворотного ходу, який є ***статичним***.
2. Клас "Машина" наслідується від "Каркасу" має змінну класу для демонстрації різниці між зміною класу та екземпляром. Також перевизначає абстрактні методи.
3. ***Статичний*** метод визначений у абстрактному класі, виконує функцію зворотного ходу машини.
4. Ієрархія виключень реалізована як декілька пустих класів з різними іменами, які наслідуються з класу "Exception"

Програма виконується наступним чином:
- Створюється екземпляр класу
- Викликаються всі методи абстрактного класу
- Для демонстрації різниці між змінними класу та екземпляром виводяться ці змінні.
- Щоб викликати виключення змінна класу повинна містити значення менше 5.

### Результат роботи
>Car S is driving <br>
This car is riding reverse <br>
Car  S has been parked <br>
Car S has been locked <br>
35 S <br>
40 Traceback (most recent call last): <br>
  File "D:\PyCharm 2020.3.3\plugins\python\helpers\pydev\pydevd.py", line 1477, in _exec <br>
    pydev_imports.execfile(file, globals, locals)  # execute the script <br>
  File "D:\PyCharm 2020.3.3\plugins\python\helpers\pydev\_pydev_imps\_pydev_execfile.py", line 18, in execfile <br>
    exec(compile(contents+"\n", file, 'exec'), glob, loc) <br>
  File "L:/Python/labs/lab10-11/src/main.py", line 140, in <module> <br>
    print(Car.model) <br>
AttributeError: type object 'Car' has no attribute 'model' <br>
> 
