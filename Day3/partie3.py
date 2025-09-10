import requests
from bs4 import BeautifulSoup
import os
from html_utils import fetch_html

def find_links_in_paragraphs(url: str) -> list[str] : 
    try:
        response = requests.get(url)
        
        if response.status_code != 200:
            raise Exception(f"Erreur {response.status_code}")
      
        page_content = response.content
        page = BeautifulSoup(page_content, "html.parser")

        paragraphs = page.find_all("p")
        
        lien = []
        for a in paragraphs:
            tags = a.find_all("a", href=True)
            for i in tags:
                lien.append(i["href"])
        return lien
    except requests.exceptions.ConnectionError:
        raise Exception("Erreur lors de la requête ")
    
    
    
url = "https://stackoverflow.com/questions/18831380/how-can-i-from-bs4-import-beautifulsoup" ##lien Wiki KO
liens = find_links_in_paragraphs(url)
print(liens)


##2 et 3 pas fait : je peux rien tester , depuis la 1 ère requête je suis en erreur 403 sur wiki 


