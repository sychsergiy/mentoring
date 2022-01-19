# Select Practice

## Simple SELECT
[SELECT](https://www.w3schools.com/sql/sql_select.asp)

[SELECT DISTINCT](https://www.w3schools.com/sql/sql_distinct.asp)
* Вибрати всі записи з таблиці Автор, включити всі поля
* Вибрати всі записи з таблиці Автор, включити лише ім'я та прізвище
* Вибрати унікальні адреси з таблиці АккаунтКористувача

## WHERE
[WHERE](https://www.w3schools.com/sql/sql_where.asp)
* Вибрати відгуки в яких оцінка більше 3
* Відібрати ім'я та прізвище авторів, прізвище яких закінчується на *кий

## ORDER BY
[ORDER BY](https://www.w3schools.com/sql/sql_orderby.asp)
* Вибрати авторів, сортувати за алфавітом по прізвищу

## Aggregations
[COUNT, AVG, SUM](https://www.w3schools.com/sql/sql_count_avg_sum.asp)

[LIKE](https://www.w3schools.com/sql/sql_like.asp)

[MAX, MIN](https://www.w3schools.com/sql/sql_min_max.asp)
### COUNT
* Отримати кількість відгуків

### COUNT + LIKE
* Отримати кількість книг, які містять в назві слово "Фундація"

### AVG + WHERE
* Отримати середню оцінку серед всіх відгуків
* Отримати середню оцінку серед відгуків однієї книги(взяти довільну книгу на свій вибір, саму книгу в результат включати не потрібно)

### MAX
* Отримати масимальну оцінку серед відгуків

### AVG + MAX
* Відабрати відгуки з максимальною оцінкою (максимальну оцінку отримати за допомогою MAX)

### GROUP_BY + AVG
[GROUP BY](https://www.w3schools.com/sql/sql_groupby.asp)
* Отримати середню оцінку для кожної книги (самі книги включати в результат не потрібно)

## JOINS

### FULL JOIN
[FULL JOIN](https://www.w3schools.com/sql/sql_join_full.asp)
* Отримати декартовий добуток таблиць Книги та Відгуки
* Отримати декартовий добуток таблиць Книги, Автора та розв'язної таблиці

### INNER JOIN
[INNER JOIN](https://www.w3schools.com/sql/sql_join_inner.asp)
* Відібрати (прізвище користувача, номер телефону, адресу)
* Відібрати (назву книги, текст відгуку, оцінку)

### INNER JOIN + GROUP BY + AVG
[GROUP BY](https://www.w3schools.com/sql/sql_groupby.asp)
* Відібрати (назва книги, середню оцінку)
* Відібрати (ім'я користувача, прізвище користувача, середня оцінка)

### INNER + GROUP BY + HAVING
[GROUP BY](https://www.w3schools.com/sql/sql_groupby.asp)
[HAVING](https://www.w3schools.com/sql/sql_having.asp)
* Отримати (назва книги, ім'я автора, прізвище автора)

### INNER JOIN X2
* Отримати (назва книги, ім'я автора, прізвище автора)

### Complex Queries
* Відібрати (ім'я користувача, прізвище користувача, email користувача, текст відгуку, назва книга)
* Відібрати (назву книги, ім'я автора, середню оцінку), відфільтрувати: середня оцінка більше 3
* Визначити яку середню оцінку користувач поставив книгам написаним одним автором, 
   для цього відібрати (ім'я користувача, прізвище користувача, ім'я автора, прізвище автора, середня оцінка)

