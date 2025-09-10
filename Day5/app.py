from fastapi import FastAPI
from pymongo import MongoClient
from bson import json_util
import json
from fastapi import Query
from typing import Optional, List

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello world, this is my first web API!"}


client = MongoClient("mongodb://localhost:27017/")
db = client["nobel"]
collection = db["laureates"]

@app.get("/laureates")
def laureats():
    try:
        tri = collection.find().sort([("year", 1),("surname", 1)])
        liste = list(tri)
        data = json_util.dumps(liste)
        return json.loads(data) 
    except Exception as e:
        return {"Erreur": str(e)}
    

@app.get("/prizes")
def prix():
    try:
        tri = collection.find().sort([("year", 1),("category", -1)])
        prix = list(tri)
        data = json_util.dumps(prix)
        return json.loads(data)

    except Exception as e:
        return {"Erreur": str(e)}



@app.get("/prizes_statistics")
def prizes_statistics(
    start: Optional[int] = Query(None, description="Année de début (incluse)"),
    end: Optional[int] = Query(None, description="Année de fin (incluse)"),
    categories: Optional[List[str]] = Query(None, description="Liste des catégories à filtrer")):
    try:
        prix_collection = db["prizes"]
        filtres = {}
        
        if start is not None or end is not None:
            filtre_annee = {}
            if start is not None:
                filtre_annee["$gte"] = start 
            if end is not None:
                filtre_annee["$lte"] = end
            filtres["year"] = filtre_annee
        if categories is not None and len(categories) > 0:
            filtres["category"] = {"$in": categories}
        
        etape_filtrage = {"$match": filtres}
        
        etape_groupement = {
            "$group": {"_id": "$category","nombre_prix": {"$sum": 1},"nombre_laureats": {
                     "$sum": {"$cond": {"if": {"$isArray": "$laureates"},"then": {"$size": "$laureates"},"else": 0}}}}}
        
        etape_calcul = {
            "$project": {"_id": 0,"category": "$_id","total_prizes": "$nombre_prix","average_laureates_per_prize": {"$round": [
                        {"$cond": {"if": {"$eq": ["$nombre_prix", 0]},"then": 0,"else": {"$divide": ["$nombre_laureats", "$nombre_prix"]}}},2]}}}
        
        etape_tri = {"$sort": {"category": 1}}  
        tri = [etape_filtrage, etape_groupement, etape_calcul, etape_tri]
        resultats = list(prix_collection.aggregate(tri))
        statistiques_finales = {}
        for resultat in resultats:
            nom_categorie = resultat["category"]
            statistiques_finales[nom_categorie] = {"total_prizes": resultat["total_prizes"],"average_laureates_per_prize": resultat["average_laureates_per_prize"]}
        
        return {"statistics": statistiques_finales}
        
    except Exception as erreur:
        return {"Erreur": str(erreur)}
    





@app.get("/laureates_statistics")
def laureates_statistics(
    genre: Optional[str] = Query(None, description="Filtre par genre"),
    country_code: Optional[str] = Query(None, description="Code pays de naissance (ex: FR)"),
    categories: Optional[List[str]] = Query(None, description="Liste des catégories à filtrer")):
   
    try:
        laureats_collection = db["laureates"]
        
        filtres = {}
        if genre is not None:
            filtres["gender"] = genre    
        if country_code is not None:
            filtres["bornCountryCode"] = country_code
        if categories is not None and len(categories) > 0:
            filtres["prizes.category"] = {"$in": categories}
        etape_filtrage = {"$match": filtres}
        etape_denormalisation = {"$unwind": "$prizes"}
        
        etape_filtrage_prix = {}
        if categories is not None and len(categories) > 0:
            etape_filtrage_prix = {"$match": {"prizes.category": {"$in": categories}}}
        
        etape_calcul_age = {"$addFields": {"age_valide": {"$cond": {
                        "if": {
                            "$and": [ {"$ne": ["$born", None]}, {"$ne": ["$born", ""]},{"$ne": ["$prizes.year", None]},{"$eq": [{"$type": "$born"}, "string"]},{"$gte": [{"$strLenCP": "$born"}, 4]}]},
                        "then": {"$subtract": ["$prizes.year",{"$toInt": {"$substr": ["$born", 0, 4]}}]},
                        "else": None}}}}
        
        etape_groupement = {
            "$group": {"_id": "$prizes.category","nombre_laureats": {"$sum": 1},"ages_valides": {"$push": {"$cond": {
                            "if": {"$ne": ["$age_valide", None]},
                            "then": "$age_valide",
                            "else": "$$REMOVE"}}},"annees_prix": {"$addToSet": "$prizes.year"}} }
        
        etape_calcul_final = { "$project": {"_id": 0,"category": "$_id", "total_laureates": "$nombre_laureats","average_age": { "$round": [{
                            "$cond": {
                                "if": {"$eq": [{"$size": "$ages_valides"}, 0]},
                                "then": 0,
                                "else": {"$avg": "$ages_valides"}}},2]},
                "years": {"$sortArray": {"input": "$annees_prix", "sortBy": 1}}}}
        
        tri = [etape_filtrage, etape_denormalisation]
        
        if categories is not None and len(categories) > 0:
            tri.append(etape_filtrage_prix)
        tri.extend([etape_calcul_age, etape_groupement,etape_calcul_final,])
        resultats = list(laureats_collection.aggregate(tri))
        statistiques_finales = {}
        
        for resultat in resultats:
            nom_categorie = resultat["category"]
            statistiques_finales[nom_categorie] = {
                "total_laureates": resultat["total_laureates"],
                "average_age": resultat["average_age"],
                "years": resultat["years"]}
        
        return {"statistics": statistiques_finales}
        
    except Exception as erreur:
        return {"Erreur": str(erreur)}
    


    