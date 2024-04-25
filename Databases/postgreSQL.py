import requests
from bs4 import BeautifulSoup
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def create_database(database_name, user, password):
    connection = psycopg2.connect(
        dbname='postgres',
        user=user,
        password=password,  # reika ivesti
        host='localhost'
    )
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()
    cursor.execute(sql.SQL('CREATE DATABASE {}').format(sql.Identifier(database_name)))
    cursor.close()
    connection.close()


def create_table(database_name, user, password):
    connection = psycopg2.connect(
        dbname=database_name,
        user=user,
        password=password,
        host='localhost'
    )
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS objektai(
    id SERIAL PRIMARY KEY, 
    title VARCHAR,
    price decimal(10, 3))
    """)
    connection.commit()
    print('Lentele buvo sukurta sekmingai')
    cursor.close()
    connection.close()

def scrape(url):
    header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0'}
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.content, 'html.parser')
    data = []
    objects = soup.find_all('article', class_='re-CardPackPremium')
    for obj in objects:
        title = obj.find('span', class_='re-CardTitle re-CardTitle--big').text.strip()
        price = obj.find('span', class_='re-CardPrice').text.strip().replace('€ /month', '')
        data.append({
            'title': title,
            'price': price
        })
    return data


def insert_data(database_name, data, user, password):
    connection = psycopg2.connect(
        database=database_name,
        user=user,
        password=password
    )
    cursor = connection.cursor()
    for objj in data:
        cursor.execute('INSERT INTO objektai (title, price) VALUES (%s, %s)', (objj['title'], objj['price']))
    connection.commit()
    print('Data inserted')
    cursor.close()
    connection.close()


def main():
    url = 'https://www.fotocasa.es/en/rental/homes/malaga-province/all-zones/l'
    database_name = 'fotocasa'
    user = 'postgres'
    password = '****'
    # create_database(database_name, user, password)
    data = scrape(url)
    # create_table(database_name, user, password)
    insert_data(database_name, data, user, password)
    print(data)


if __name__ == '__main__':
    main()





