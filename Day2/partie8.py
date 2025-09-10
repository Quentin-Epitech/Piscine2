import pandas as pd 
 
csv = "orders_semicolon.csv"
read = pd.read_csv(csv, sep=';')






def number_uniformisation(df: pd.DataFrame) -> pd.DataFrame :

    df["quantity"] = df["quantity"].astype(int)
    df["total_price"] = df["total_price"].astype(float).round(2)
    return df


exo2 = number_uniformisation(read)
print(exo2)

def string_uniformisation(df: pd.DataFrame) -> pd.DataFrame :
    df["product"] = df["product"].str.lower()
    return df


exo2bis = string_uniformisation(read)
print(exo2bis)




def number_validation(df: pd.DataFrame) -> bool : 
    if not (df["total_price"] > 0).all():
        return False
    
    if not df["quantity"].between(1, 10).all():
        return False
    
    return True


exo3 = number_validation(read)
print(exo3)


def enum_validation(df: pd.DataFrame, products: list) -> pd.DataFrame : 
    pas_valide = df[~df["product"].isin(products)]
    
    return pas_valide

exemple = ["smartphone","keyboard","headphones","tablet","smartwatch","laptop","mouse","camera","printer","monitor"]
exo4 = enum_validation(read,exemple) 

print(exo4)

exemple2 = ["smartphone","keyboard","headphones","tablet"]
exo42 = enum_validation(read,exemple2)

print(exo42)


 
