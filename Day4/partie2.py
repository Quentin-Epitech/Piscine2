from pymongo import MongoClient

def get_mongo_client(host: str, port: int,user: str = "admin", password: str = "azerty") -> MongoClient : 
    return MongoClient (host,port)

test = get_mongo_client("localhost", 27017)
print(test)



def create_award_year_index(client: MongoClient) :
    index = client["nobel"]["laureates"].create_index([("prizes.year", -1)])
    print(f"Index  : {index}")
    return index
    
create_award_year_index(test)

def get_laureates_year(client: MongoClient, year: int) -> list[dict]:
    laurea = client["nobel"]["laureates"].find(
        {"prizes": {"$elemMatch": {"year": year}}},  
        {"_id": 0, "firstname": 1, "surname": 1, "prizes": 1}
    )
    return list(laurea)


essai = get_laureates_year(test, 2010)
print(essai)



def create_country_index(client: MongoClient) :
    
    index = client["nobel"]["laureates"].create_index(
        [("bornCountry", "text"), ("diedCountry", "text")])
    print(f"Index  : {index}")
    return index

create_country_index(test)


def get_country_laureates(client: MongoClient, country: str) -> list[dict]:
    
    client["nobel"]["laureates"].create_index(
        [("bornCountry", "text"), ("diedCountry", "text")])
    
    recherche = client["nobel"]["laureates"].find(
        {"$text": {"$search": country}},
        {"_id": 0, "firstname": 1, "surname": 1, "bornCountry": 1, "diedCountry": 1})
    
    return list(recherche)


resultat = get_country_laureates(test, "United States of America")
print(resultat)


def create_gender_category_index(client: MongoClient) : 
    index = client["nobel"]["laureates"].create_index(
        [("prizes.category", -1), ("gender", 1)])
    print(f"Index  : {index}")
    return index

create_gender_category_index(test)


def get_gender_category_laureates(client: MongoClient, gender: str, category: str) -> list[dict] :
    results = client["nobel"]["laureates"].find(
        { "gender": gender,"prizes.category": category},
        { "_id": 0,"firstname": 1,"surname": 1,"born": 1,"died": 1,"bornCountry": 1,"diedCountry": 1,"gender": 1, "prizes": 
         {"$elemMatch": { "category": category }}})
    return list(results)


essai = get_gender_category_laureates(test, "male", "physics")
print(essai)


def create_year_category_index(client: MongoClient) :
    index = client["nobel"]["prizes"].create_index(
        [("year", 1), ("category")],unique=True)
    print(f"Index  : {index}")
    return index

create_year_category_index(test)
