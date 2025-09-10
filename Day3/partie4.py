import requests
from bs4 import BeautifulSoup

def get_one_book() -> dict :
    url = "https://books.toscrape.com/?"

    reponse = requests.get(url)

    clean = BeautifulSoup(reponse.content, 'html.parser')
    
    premier = clean.find('article', class_='product_pod')

    titre = premier.h3.a['title']
    note = premier.p['class'][1]

    notation = { 'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5 }

    note = notation.get(note, 0)
    prix = float(premier.select('p.price_color')[0].text[1:])
    return {
        'Titre': titre,
        'note': note,
        'prix': prix}

book = get_one_book()
print(book)


def get_one_book_complete() -> dict:
    url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

    reponse = requests.get(url)

    clean = BeautifulSoup(reponse.content, 'html.parser')

    titre = clean.find('h1').text.strip()

    prix = float(clean.find('p', class_='price_color').text[1:])

    note = clean.find('p', class_='star-rating')['class'][1]

    bareme = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}

    notefinal = bareme.get(note, 0)

    idescription = clean.find('div', id='product_description')
    description = idescription.find_next('p').text.strip()
    

    return {
        'Titre': titre,
        'note': notefinal,
        'prix': prix,
        'description': description
    }


book = get_one_book_complete()
print(book)


