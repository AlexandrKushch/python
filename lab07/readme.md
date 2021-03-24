# Декоратори
# Лабораторна робота №7
### Ціль: Написати декоратори, які рахують час виконання функції, повторюють виконання функції якщо звершилась невдачно, та запам'ятовує імена функцій які продекаровані.

Для першого дератора використовуємо методи часу **now()**, щоб запам'ятати початок та кінець роботи функції. 
Між цими точками часу викликаємо функцію, яка "спить" дві секунди.

Для другого декоратора потрібно визвати функцію якщо вона повернула **0**

Третій декоратор додає у список функцію.

# Результат роботи програми:
>Show arguments <br>
> 0:00:02.011300 <br>
> [<function count_time.<locals>.over.<locals>.wrapper at 0x0000020A3E275820>, <function reply.<locals>.wrapper at 0x0000020A3E275940>] <br>