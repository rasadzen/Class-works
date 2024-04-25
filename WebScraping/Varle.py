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
    product_list = []
    products = soup.find_all('div', {'class': 'GRID_ITEM'})
    for product in products:
        product_name = product.find('div', class_='product-title').text.strip()
        product_price = product.find('span', class_='price-value').text.strip()

        product_list.append({
            'Produkto pavadinimas': product_name,
            'Produkto kaina': product_price
        })
    return product_list


def scrape_page(base_url, start_page=1, max_pages=5):
    url = "https://www.varle.lt/isoriniai-kietieji-diskai-hdd/"
    # varle.lt / isoriniai - kietieji - diskai - hdd /?p = 3
    all_products = []
    current_page = start_page
    while current_page <= max_pages:
        url = f'{base_url}?p={current_page}'
        print(f'Scraping page {url}')
        html = fetch_page(url)
        if html:
            has_products = parse_page(html)
            if has_products:
                all_products.extend(has_products)
            else:
                print('No more products found! Sttopping..')
                break
        else:
            print('Failed to retrieve page')
            break
        current_page += 1
    print(f'Total products: {len(all_products)}')
    for product in all_products:
        print(product)

base_url = "https://www.varle.lt/isoriniai-kietieji-diskai-hdd/"
scrape_page(base_url)
