# Наслідування та поліморфізм у Python
# Лабораторна робота № 12
### Ціль: реалізувати ітератор на основі класу. У спадкоємці ітератора додати генератор. Використовуючи ітератор оновити метод зчитування із файлу. 

1. Клас __ітератора__ містить список елементів та ключ поточного елементу. Перевизначаємо методи "__iter__()" i "__next()__".
2. Клас __генератор__ наслідується від __Ітератора__.  Містить метод який генерує __генератор__.
3. Клас __менеджер__ перевизначає методи "enter()" i "exit()"
4. Функції запису/читання в файл використовує менеджер створений в п. 3
5. Далі демонструємо роботу програми.

### Особливості Ітератора

Метод "next()" містить звичайний цикл який проходить по елементах списку. Метод "enter()" обов'язково повертає ключ поточного елементу до нуля.


### Результат роботи
>>Iterator
Model: S; Transmission: Mechanical; Year: 1990; Volume: 1.6; HP: 79 </br>
Model: T; Transmission: Mechanical; Year: 2000; Volume: 2.2; HP: 103 </br>
Model: V; Transmission: Automatic; Year: 2010; Volume: 3.3; HP: 250 </br>
iterator </br>
Model: S; Transmission: Mechanical; Year: 1990; Volume: 1.6; HP: 79 </br>
Model: T; Transmission: Mechanical; Year: 2000; Volume: 2.2; HP: 103 </br>
Model: V; Transmission: Automatic; Year: 2010; Volume: 3.3; HP: 250 </br>
generator </br>
Model: S; Transmission: Mechanical; Year: 1990; Volume: 1.6; HP: 79 </br>
Model: T; Transmission: Mechanical; Year: 2000; Volume: 2.2; HP: 103 </br>
Model: V; Transmission: Automatic; Year: 2010; Volume: 3.3; HP: 250 </br>
Read cars </br>
Model: S; Transmission: Mechanical; Year: 1990; Volume: 1.6; HP: 79 </br>
Model: T; Transmission: Mechanical; Year: 2000; Volume: 2.2; HP: 103 </br>
Model: V; Transmission: Automatic; Year: 2010; Volume: 3.3; HP: 250
