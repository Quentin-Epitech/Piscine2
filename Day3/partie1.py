import requests
def get_request(url: str) -> (int, str) : 
    r = requests.get(url)
    return r.status_code, r.json ()

r = get_request("https://restcountries.com/v3.1/all?fields=name,flags`")
print(r)



def get_countries_info(country_codes: list, info: list) -> (int, str) :
    lien = "https://restcountries.com/v3.1/alpha"
    params = {
        "codes": ','.join(country_codes),
        "fields": ','.join(info)
    }
    r = requests.get(lien,params = params)
    return r.status_code, r.json()

r = get_countries_info(["FR"], ["name", "flags"])
print(r)



def handle_request_status(url: str, data: dict = None) -> int | str:
   
    try:
        reponse = requests.post(url,json=data)
        reponse.raise_for_status()  
        return reponse.status_code

    except requests.exceptions.HTTPError as http_erreur:
        return f"Probleme http : {http_erreur}"

    except requests.exceptions.RequestException as req_erreur:
        return f"probleme de requête :  {req_erreur}"


url = "https://webhook.site/85d3b50b-6996-4ffa-81bb-f04f5c3002b7" ##si le lien de l'api n'est plus valable,il y a le screen du panel
parametre = {"message": "je m'appelle quentin et je post"}

reponse = handle_request_status(url, parametre) 
print(reponse) 


def send_query_parameters(params: dict) -> dict :
    url = "https://httpbin.org/response-headers"
    reponse = requests.get(url,params=params)
    return reponse.json()
    
    
params = {"message" : "je m'appelle quentin"}
print(send_query_parameters(params))

def send_headers(headers: dict) -> str :
    url = "https://httpbin.org/headers"
    reponse = requests.get(url,headers=headers)
    return reponse.json().get("headers", "")


headers = {"message" : "je m'appelle quentin"}
print(send_headers(headers))