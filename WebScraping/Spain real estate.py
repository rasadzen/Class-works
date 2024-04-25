import requests
from bs4 import BeautifulSoup


def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    object_list = []
    objects = soup.find_all('li', {'data-object': True})

    for obj in objects:
        object_name = obj.find('div', class_='title')
        object_price = obj.find('div', class_='price js-list-for-show')
        object_bedrooms = obj.find('span', class_='bedrooms')
        object_bathrooms = obj.find('span', class_='bathrooms')

        if object_name:
            object_name = object_name.text.strip()
            print(object_name)
        else:
            print("Informacijos nera!")
        if object_price:
            object_price = object_price.text.strip().replace('EUR €USD $RUB ₽NOK krGBP £', '')
            print(object_price)
        else:
            print("Informacijos nera!")
        if object_bedrooms:
            object_bedrooms = object_bedrooms.text.strip()
            print(object_bedrooms)
        else:
            print("Informacijos nera!")
        if object_bathrooms:
           object_bathrooms = object_bathrooms.text.strip()
           print(object_bathrooms)
        else:
            print("Informacijos nera!")

        object_list.append({
            'Objekto pavadinimas': object_name,
            'Objekto kaina': object_price,
            'Objekte esantys miegamieji': object_bedrooms,
            'Objekte esantys vonios kambariai': object_bathrooms
             })

    return object_list

def scrape_page(url):
    html = fetch_page(url)
    if html:
        parse_page(html)
    else:
        print("Failed")

scrape_page("https://spain-real.estate/property/andalusia/sevilla/")