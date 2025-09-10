from bs4 import BeautifulSoup
import re


def create_bs_obj(file: str) -> BeautifulSoup:
    fichier = open(file,"r")
    content = fichier.read()
    fichier.close()  
    return BeautifulSoup(content, "html.parser")

lecture = create_bs_obj("example.html") 
print(lecture.h1.text)


def find_title(file: str) -> str:
    fichier = create_bs_obj(file)
    titre = fichier.title
    return str(titre) if titre else None 

file = "example.html"
titre = find_title(file)
print(titre)


def find_paragraphs(file: str) -> list[str] :
    fichier = create_bs_obj(file)
    balises = fichier.find_all("p")
    return [str(p) for p in balises]  

file = "example.html"
balises = find_paragraphs(file)
for paragraph in balises:
    print(paragraph)

def find_links(file: str) -> list[str] : 
    fichier = create_bs_obj(file)
    lien = fichier.find_all("a", href=True)
    return [liens["href"] for liens in lien]

file = "example.html"
links = find_links(file)
print(links)


def find_elements_with_css_class(file: str, class_name: str) -> list[str] : 
    fichier = create_bs_obj(file)
    elements = fichier.find_all(class_=class_name)
    return [str(element) for element in elements]

file = "example.html"
css_classes = find_elements_with_css_class(file, "info")

for class_elem in css_classes:
    print(class_elem)

def find_headers(file: str) -> list[str] : 
    fichier = create_bs_obj(file)
    headers = fichier.find_all(re.compile("^h[1-6]"))
    return [header.get_text() for header in headers]

file = "example.html"
headers = find_headers(file)
print(headers)


def extract_table(file: str) -> list[dict] :
    fichier = create_bs_obj(file)
    table = fichier.find("table")
    donnee = []
    for i in table.find_all("tr")[1:]:
        colonnes = i.find_all("td")
        if len(colonnes) == 3:
            fruit = {
                "nom": colonnes[0].get_text().strip(),
                "couleur": colonnes[1].get_text().strip(),
                "prix": float(colonnes[2].get_text().strip().replace('$', '').replace(',', ''))
            }
            donnee.append(fruit)
    return donnee


file = 'example.html'
fruits = extract_table(file)
for fruit in fruits:
    print(fruit)


