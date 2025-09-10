import requests
import csv
import os
def get_companies_with_name(name: str):
    try:
        url = "https://recherche-entreprises.api.gouv.fr/search"
        params = {"q": name, "per_page": 10}
        reponse = requests.get(url, params=params)
        reponse.raise_for_status()
        data = reponse.json()
        resultat = data.get("results", [])

        entreprise = []

        for entreprises in resultat:
            info = {"siren": entreprises.get("siren"),"nom_complet": entreprises.get("nom_complet"),"date_creation": entreprises.get("date_creation")}
            entreprise.append(info)
        return entreprise

    except Exception as e:
        print("Erreur :", e)
        return []


print(get_companies_with_name("EPITECH"))


def get_all_companies_with_name(name: str) -> list[dict]:
    try:
        url = "https://recherche-entreprises.api.gouv.fr/search"
        toutes_entreprises = []
        page = 1
        
        while True:
           
            params = {"q": name, "per_page": 25, "page": page}
            reponse = requests.get(url, params=params)
            reponse.raise_for_status()
            data = reponse.json()
            resultats = data.get("results", [])
            
            if not resultats:
                break
    
            for entreprise in resultats:
                info = {"siren": entreprise.get("siren"),"nom_complet": entreprise.get("nom_complet"),"date_creation": entreprise.get("date_creation")}
                toutes_entreprises.append(info)

            total_pages = data.get("total_pages", 1)
            if page >= total_pages:
                break
            page += 1
        
        return toutes_entreprises
        
    except Exception as e:
        print(f"Erreur: {e}")
        return []

print(get_all_companies_with_name("EPITECH"))

def get_and_store_companies(filename: str, name: str)  : 
     try:   
        nouvelles_entreprises = get_all_companies_with_name(name)  
        if not nouvelles_entreprises:
            return
        entreprises_existantes = set()  
        if os.path.exists(filename):
            try:
                with open(filename, 'r', newline='', encoding='utf-8') as fichier:
                    lecteur = csv.reader(fichier) 
                    next(lecteur, None)

                    for ligne in lecteur:
                        if ligne: 
                            entreprises_existantes.add(ligne[0])  
            except Exception: 
                pass 
      
        entreprises_a_ajouter = []
        for entreprise in nouvelles_entreprises:
            siren = entreprise.get("siren")
            if siren and siren not in entreprises_existantes:
                entreprises_a_ajouter.append(entreprise)

        if not entreprises_a_ajouter:
            return
        
        entreprises_a_ajouter.sort(key=lambda x: x.get("siren", ""))     
        ecrire_entete = not os.path.exists(filename) or os.path.getsize(filename) == 0
        
        with open(filename, 'a', newline='', encoding='utf-8') as fichier:
            writer = csv.writer(fichier)
               
            if ecrire_entete:
                writer.writerow(['siren', 'nom_complet', 'date_creation'])
                
            for entreprise in entreprises_a_ajouter:
                writer.writerow([
                    entreprise.get("siren", ""),
                    entreprise.get("nom_complet", ""),
                    entreprise.get("date_creation", "")])        
     except Exception as e:
        print(f"Erreur: {e}")
        return
     
get_and_store_companies("entreprise.csv","EPITECH")
