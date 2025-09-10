from pymongo import MongoClient

def get_mongo_client(host: str, port: int,user: str = "admin", password: str = "azerty") -> MongoClient : 
    return MongoClient (host,port)

test = get_mongo_client("localhost", 27017)
print(test)


def get_all_laureates(client: MongoClient) -> list[dict] : 
    return list(client["nobel"]["laureates"].find())

liste = get_all_laureates(test)
print(liste)


def get_laureates_information(client: MongoClient) -> list[dict] :
    return list(client["nobel"]["laureates"].find({}, {"_id": 0, "firstname": 1, "surname": 1, "born": 1}))

information = get_laureates_information(test)
for i in range(2):
    print(information[i])

def get_prize_categories(client: MongoClient) -> list[str] : 
    return list(client["nobel"]["prizes"].distinct("category"))

categorie = get_prize_categories(test)
print(categorie)


def get_category_laureates(client: MongoClient, category: str) -> list[dict] :
    tri = client["nobel"]["laureates"].find(
        {"prizes.category": category},
        {"_id": 0, "firstname": 1, "surname": 1, "prizes.category": 1})          
    resultat = []
    for result in tri:
        prix = [{"category": prize.get("category")} for prize in result.get("prizes", [])]
        resultat.append({
            "firstname": result.get("firstname"),
            "surname": result.get("surname"),
            "prizes": prix})
    return resultat     

physique = get_category_laureates(test, "physics")

print(physique)

def get_country_laureates(client: MongoClient, country: str) -> list[dict]:
   
    tri = client["nobel"]["laureates"].find(
        {"bornCountry": country},
        {"_id": 0, "firstname": 1, "surname": 1, "bornCountry": 1})
    resultat = []
    for result in tri:

        resultat.append({
            "firstname": result.get("firstname"),
            "surname": result.get("surname"),
            "bornCountry": result.get("bornCountry")})
    return resultat

pays = get_country_laureates(test, "France")
print(pays)




def get_laureates_information_sorted(client: MongoClient) -> list[dict]:
    tri = list(client["nobel"]["laureates"].find({},
        {
            "_id": 0,
            "firstname": 1,
            "surname": 1,
            "bornCountry": 1,
            "born": 1}))

    sorted_laureates = sorted(
        tri,
        key=lambda x:(x.get("bornCountry", ""), x.get("born", "")),
        reverse=False)

    sorted_laureates = sorted(
        sorted_laureates,
        key=lambda x: x.get("bornCountry", ""),
        reverse=True)

    return sorted_laureates


tri = get_laureates_information_sorted(test)
print(tri)