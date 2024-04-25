from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager  # ChromeDriverManager
from selenium.webdriver.common.by import By
import time

target = ['https://ibiblioteka.lt/metis/publication?q=yubs6a4wr']


def scrape_books_data(urls):
    books_data = []
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    for index, url in enumerate(urls):
        driver.get(url)
        time.sleep(3)

        if index == 0:
            try:
                open_dropdown = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'mat-form-field.ng-tns-c69-2')))
                open_dropdown.click()
                time.sleep(2)
                print('Isskleidziamas meniu paspaustas')
                third_option = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, '#mat-option-2')))  #
                third_option.click()
                time.sleep(2)
                print('Pasirinktas 3 meniu elementas')
                search_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, '.c-btn--cta'))
                )
                search_button.click()
                time.sleep(3)
                print("Paieskos mygtukas paspaustas")

                cookie_agreement = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'app-button.cookie-agreement__button:nth-child(1)'))
                )
                cookie_agreement.click()
                print('Accepted Cookie agreement!')

                for _ in range(4):
                    try:
                        load_more = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, '.mat-stroked-button'))
                        )
                        load_more.click()
                        print('Daugiau rezultatu mygtukas paspaustas')
                        time.sleep(3)
                    except (NoSuchElementException, TimeoutException, ElementClickInterceptedException) as e:
                        print(f'Error while clicking "Load more": {e}')
                        break

                    soup = BeautifulSoup(driver.page_source, 'html.parser')
                    table = soup.find('table', class_='c-data-table')
                    if table:
                        for row in table.find_all('tr')[1:]:
                            cells = row.find_all('td')
                            if cells:
                                title_data = cells[1].text.split("Pavadinimas:")[-1]
                                books_data.append({
                                    'title': title_data
                                })
                    else:
                        print('No table found')

            except Exception as e:
                print(f"Error Occurred {e}")

    driver.quit()
    return books_data


all_data = []

for url in target:
    data = scrape_books_data(target)
    all_data.extend(data)


print(all_data)