import pandas as pd  

def sort_dataframe_simple(data: pd.DataFrame) -> pd.DataFrame:
    return data.sort_values(by="product", ascending=False)

def sort_dataframe_advanced(data: pd.DataFrame) -> pd.DataFrame :
    return data.sort_values(by=['quantity', 'total_price', 'product'], ascending=[True, False, True])


test = pd.read_csv("orders.csv")

premier = sort_dataframe_simple(test)

print(premier)

premierdeux = sort_dataframe_advanced(test)

print(premierdeux)



def filter_dataframe_simple(data: pd.DataFrame, product: str) -> pd.DataFrame:
    return data[(data['product'] == product) &  (data['quantity'] >= 5)] 

troisieme_un = filter_dataframe_simple(test,"Smartphone")

print(troisieme_un)


def dataframe_operations(data: pd.DataFrame) -> (float, int, float, float, float) :
    total_amount = data['total_price'].sum().round(2)
    total_quantity = data['quantity'].sum()
    mean_price = (total_amount / len(data)).round(2)
    max_price = data['total_price'].max().round(2)
    min_price = data['total_price'].min().round(2)
    return total_amount, total_quantity, mean_price, max_price, min_price

