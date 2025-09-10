from pymongo import MongoClient
from bson import ObjectId


def get_mongo_client(host: str, port: int,user: str = "admin", password: str = "azerty") -> MongoClient : 
    return MongoClient (host,port)

test = get_mongo_client("localhost", 27017)
print(test)


def add_laureate(client: MongoClient, laureate: dict) -> ObjectId:
    resultat = client["nobel"]["laureates"].insert_one(laureate)
    print(f"Document inséré avec _id : {resultat.inserted_id}")
    return resultat.inserted_id

ajout = add_laureate(test, {"firstname": "Quentin", "surname": "Bonnet"})


def add_prizes(client: MongoClient, prizes: list) -> list:
    resultat = client["nobel"]["prizes"].insert_many(prizes)
    print(f"Documents insérés avec _id : {resultat.inserted_ids}")
    return resultat.inserted_ids


ajout_prix = add_prizes(test, [{"laureate": ObjectId(ajout), "category": "love"}])


def update_laureate(client: MongoClient, doc_id: ObjectId, dod: str, country: str, city: str) -> (int, int):
    result = client["nobel"]["laureates"].update_one({"_id": doc_id},{"$set": 
        {"died": dod,"diedCountry": country,"diedCity": city}})
    print(f"Documents modifiés : {result.modified_count} et documents trouvés : {result.matched_count}")
    return result.matched_count, result.modified_count


update = update_laureate(test, ObjectId(ajout), "2025-01-01", "France", "Paris")
    


def upper_categories(client: MongoClient) -> (int, int):
    resultat = client["nobel"]["prizes"].update_many({},
    [{"$set": {"category": {"$toUpper": "$category"}}}])
    print(f"Documents modifiés : {resultat.modified_count} et documents trouvés : {resultat.matched_count}")
    return resultat.matched_count, resultat.modified_count


majuscule = upper_categories(test)



