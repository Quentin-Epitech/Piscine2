import pandas as pd 

def create_series() -> pd.Series :
    tab = [1,2,3,4,5,6,7,8,9]
    series = pd.Series(tab)
    return series

exo1 = create_series()
print(exo1)

def series_operations(series: pd.Series) -> (int, float, float) :
    somme = series.sum()
    moyenne = series.mean()
    ecart = series.std()
    return (somme, moyenne, ecart)

exo2 = create_series()
print(series_operations(exo2))


def create_dataframe(file_path: str) -> pd.DataFrame:
    read = pd.read_csv(file_path)
    return read
file_path = "orders.csv"

exo4 = create_dataframe(file_path)
print(exo4)



#4 pas réussi

