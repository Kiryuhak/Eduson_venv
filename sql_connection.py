# Установка библиотеки
# pip intall psycopg2-binary

# Подключаяем библиотеку
import psycopg2

# Прописываем данные для входа
HOST = 'localhost'
DATABASE = 'nordwind'
USER = 'postgres'
PASSWORD = 'qweasd963'

# Устанавливаем подключение к базе
connection = psycopg2.connect(
    host=HOST, 
    database=DATABASE, 
    user=USER, 
    password=PASSWORD
)
cursor = connection.cursor()

# Описываем запрос к базе
query = "select * from categories;"

# Выполняем запрос
cursor.execute(query)

# Получаем данные
data = cursor.fetchall()

print(data)
# [(1, 'Beverages', 'Soft drinks, coffees, teas, beers, and ales', <memory at 0x000001C4A9E2CD00>), (2, 'Condiments', 'Sweet and savory sauces, relishes, spreads, and seasonings', <memory at 0x000001C4A9E2CC40)]

# Закрываем соединение
connection.close()

# Test 