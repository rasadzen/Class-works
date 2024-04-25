import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.goodreads.com/genres/most_read/psychology'
# url = 'https://www.goodreads.com/genres/most_read/biography'
# url = 'https://www.goodreads.com/genres/most_read/romance'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())
knygu_nuorodos = []
knygu_duomenys = []
knygos = soup.select('div.coverWrapper a')
# print(knygos)
for nuoroda in knygos:
    knygu_nuorodos.append('https://www.goodreads.com' + nuoroda.get('href'))

#PSICHOLOGINES
for knygos_nuoroda in knygu_nuorodos:
    knygos_ats = requests.get(knygos_nuoroda)
    if knygos_ats.status_code == 200:
        knygos_soup = BeautifulSoup(knygos_ats.text, 'html.parser')
        pavadinimas = knygos_soup.find('h1').text.strip()
        autorius = knygos_soup.find('span', class_='ContributorLink__name').text.strip()
        reitingas = knygos_soup.find('div', class_='RatingStatistics__rating').text.strip()
        kindle_kaina = knygos_soup.find('button', class_='Button Button--buy Button--medium Button--block').text.strip().replace('Kindle $','').replace('Kindle Unlimited $','')
        atsiliepimai = knygos_soup.find('span', class_='u-dot-before').text.strip().replace('\xa0reviews','')
        puslapiu_skaicius = knygos_soup.find('div', class_='FeaturedDetails').text.strip().split()[0]
        pirma_priskirta_kategorija = knygos_soup.find('span', class_='BookPageMetadataSection__genreButton').text.strip()

        knygu_duomenys.append({
            'Knygos pavadinimas': pavadinimas,
            'Knygos autorius': autorius,
            'Knygos reitingas': reitingas,
            'Knygos kaina': kindle_kaina,
            'Atsiliepimai': atsiliepimai,
            'Puslapiu skaicius': puslapiu_skaicius,
            'Pirma priskirta kategorija': pirma_priskirta_kategorija
        })
    else:
        print("Nera info")


# #BIOGRAFINES
# for knygos_nuoroda in knygu_nuorodos:
#     knygos_ats = requests.get(knygos_nuoroda)
#     if knygos_ats.status_code == 200:
#         knygos_soup = BeautifulSoup(knygos_ats.text, 'html.parser')
#         pavadinimas = knygos_soup.find('h1').text.strip()
#         autorius = knygos_soup.find('span', class_='ContributorLink__name').text.strip()
#         reitingas = knygos_soup.find('div', class_='RatingStatistics__rating').text.strip()
#         kindle_kaina = knygos_soup.find('button', class_='Button Button--buy Button--medium Button--block').text.strip().replace('Kindle $','').replace('Kindle Unlimited $','')
#         atsiliepimai = knygos_soup.find('span', class_='u-dot-before').text.strip().replace('\xa0reviews','')
#         puslapiu_skaicius = knygos_soup.find('div', class_='FeaturedDetails').text.strip().split()[0]
#         pirma_priskirta_kategorija = knygos_soup.find('span', class_='BookPageMetadataSection__genreButton').text.strip()
#
#         knygu_duomenys.append({
#             'Knygos pavadinimas': pavadinimas,
#             'Knygos autorius': autorius,
#             'Knygos reitingas': reitingas,
#             'Knygos kaina': kindle_kaina,
#             'Atsiliepimai': atsiliepimai,
#             'Puslapiu skaicius': puslapiu_skaicius,
#             'Pirma priskirta kategorija': pirma_priskirta_kategorija
#         })
#     else:
#         print("Nera info")

#ROMANAI

# for knygos_nuoroda in knygu_nuorodos:
#     knygos_ats = requests.get(knygos_nuoroda)
#     if knygos_ats.status_code == 200:
#         knygos_soup = BeautifulSoup(knygos_ats.text, 'html.parser')
#         pavadinimas = knygos_soup.find('h1').text.strip()
#         autorius = knygos_soup.find('span', class_='ContributorLink__name').text.strip()
#         reitingas = knygos_soup.find('div', class_='RatingStatistics__rating').text.strip()
#         kindle_kaina = knygos_soup.find('button', class_='Button Button--buy Button--medium Button--block').text.strip().replace('Kindle $','').replace('Kindle Unlimited $','')
#         atsiliepimai = knygos_soup.find('span', class_='u-dot-before').text.strip().replace('\xa0reviews','')
#         puslapiu_skaicius = knygos_soup.find('div', class_='FeaturedDetails').text.strip().split()[0]
#         pirma_priskirta_kategorija = knygos_soup.find('span', class_='BookPageMetadataSection__genreButton').text.strip()
#
#         knygu_duomenys.append({
#             'Knygos pavadinimas': pavadinimas,
#             'Knygos autorius': autorius,
#             'Knygos reitingas': reitingas,
#             'Knygos kaina': kindle_kaina,
#             'Atsiliepimai': atsiliepimai,
#             'Puslapiu skaicius': puslapiu_skaicius,
#             'Pirma priskirta kategorija': pirma_priskirta_kategorija
#         })
#     else:
#         print("Nera info")

for knyga in knygu_duomenys:
    print(knyga)

# df = pd.DataFrame(knygu_duomenys)
# df.to_csv('knygu_duomenys_psichologines.csv')


