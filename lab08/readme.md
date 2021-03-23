#  Файли. Виключення. Менеджери контексту.
# Лабораторна робота №8
### Ціль: Навчитись роботи з файлами(редагувати) використовуючи конструкцію *try/catch*, використати менеджери контексту.

Для підрахування кількості символів у кожному рядку спочатку відкриваємо файл на читання
циклом проходимо по файлу та виводимо довжину кожної строки без знаків пробілу справа.

Для видалення з файлу *n*-го рядку чи переставити рядки місцями(це залежить від переданих параметрів)
виконуємо відкриття файлу на читання, та зчитуємо усі строки у список.
Закриваємо файл, та знову відкриваємо на запис. В залежності від переданих параметрів, 
записуємо всі рядки окрім заданого, якщо хочемо видалити. Або міняємо рядки місцями у списку та записуємо їх усі в файл,
якщо користувач передав у функцію замінити рядки.

# Результат роботи
Програма виводить лише роботу першої функції
> 0 line: 56 <br>
> 1 line: 25 <br>
> 2 line: 65 <br>
> 3 line: 61 <br>
> 4 line: 41 <br>
> 5 line: 48

# У файлі (Перед роботою)
> Lorem ipsum dolor sit amet, consectetur adipiscing elit.  <br>
Proin eget dictum ligula. <br>
Mauris tempor, quam sed ultricies rutrum. <br>
Etiam faucibus orci augue, nec consectetur leo faucibus eget. <br>
Mauris urna eros, sollicitudin eu pretium eu, hendrerit nec diam. <br>
Quisque placerat mollis diam ultricies vehicula.

# У файлі (Після роботи)
> Lorem ipsum dolor sit amet, consectetur adipiscing elit. <br>
Proin eget dictum ligula. <br>
Mauris urna eros, sollicitudin eu pretium eu, hendrerit nec diam. <br>
Etiam faucibus orci augue, nec consectetur leo faucibus eget. <br>
Mauris tempor, quam sed ultricies rutrum. <br>
Quisque placerat mollis diam ultricies vehicula. <br>

Третя та п'ята строки змінились місцями.