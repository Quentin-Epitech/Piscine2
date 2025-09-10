from pymongo import MongoClient


def get_mongo_client(host: str, port: int,user: str = "admin", password: str = "azerty") -> MongoClient : 
    return MongoClient (host,port)

test = get_mongo_client("localhost", 27017)
print(test)


def prizes_per_category_basic(client: MongoClient) -> list[dict] :
    data = [
        {"$group": {"_id": "$category", "count": {"$sum": 1}}},
        {"$project": {"_id": 1, "category": "$_id", "count": 1}},
        {"$sort": {"category": 1}}]
    
    resultat = list(client["nobel"]["prizes"].aggregate(data))
    return resultat

client = MongoClient('localhost', 27017)
result = prizes_per_category_basic(client)
for elem in result :
    print(elem)


 
def prizes_per_category_sorted(client: MongoClient) -> list[dict]:
    data = [
        {"$group": {"_id": "$category", "count": {"$sum": 1}}},
        {"$project": {"_id": 0, "category": "$_id", "count": 1}},
        {"$sort": {"count": -1, "category": 1}}]
    
    resultat = list(client["nobel"]["prizes"].aggregate(data))
    return resultat

result = prizes_per_category_sorted(client)
for elem in result :
    print(elem)


def prizes_per_category_filtered(client: MongoClient, nb_laureates: int) -> list[dict]:
    data = [
        {"$match": { "laureates": {"$size": nb_laureates}}},
        {"$group": {"_id": "$category","prizes": {"$sum": 1}}}]
    resultat = client["nobel"]["prizes"].aggregate(data)
    return list(resultat)


result = prizes_per_category_filtered(client, nb_laureates=1)
for elem in result: 
    print(elem)



def prizes_per_category(client: MongoClient, nb_laureates: int) -> list[dict] : 
    data = [{"$match": {"laureates": {"$size": nb_laureates}}},
            {"$group": {"_id": "$category","prizes": {"$sum": 1}}}, 
            {"$sort": {"prizes": -1,"_id": 1 }}]
    resultat = client["nobel"]["prizes"].aggregate(data)
    return list(resultat)

result = prizes_per_category(client, nb_laureates=1)

for elem in result:
    print(elem)



def laureates_per_birth_country_complex(client: MongoClient) -> list[dict] : 
    return
