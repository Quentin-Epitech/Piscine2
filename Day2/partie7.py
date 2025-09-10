import pandas as pd  

def sort_dataframe_simple(data: pd.DataFrame) -> pd.DataFrame:
    return data.sort_values(by="product", ascending=False)

def sort_dataframe_advanced(data: pd.DataFrame) -> pd.DataFrame :
    return data.sort_values(by=["quantity", "total_price", "product"], ascending=[True, False, True])


test = pd.read_csv("orders.csv")

premier = sort_dataframe_simple(test)

print(premier)

premierdeux = sort_dataframe_advanced(test)

print(premierdeux)



def filter_dataframe_simple(data: pd.DataFrame, product: str) -> pd.DataFrame:
    return data[(data["product"] == product) &  (data["quantity"] >= 5)] 

troisieme_un = filter_dataframe_simple(test,"Smartphone")

print(troisieme_un)


def dataframe_operations(data: pd.DataFrame) -> (float, int, float, float, float) :
    montant_total = data["total_price"].sum().round(2)
    quantite_total = data["quantity"].sum()
    prix_moyen = (montant_total / len(data)).round(2)
    montant_maximum = data["total_price"].max().round(2)
    montant_minimum = data["total_price"].min().round(2)
    return montant_total, quantite_total, prix_moyen, montant_maximum, montant_minimum

exo4 = dataframe_operations(test)

print(exo4)

