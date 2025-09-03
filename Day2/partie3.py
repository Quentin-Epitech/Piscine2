import pandas as pd 

def create_series() -> pd.Series :
    tab = [1,2,3,4,5,6,7,8,9]
    series = pd.Series(tab)
    return series

Test = create_series()
print(Test)

def series_operations(series: pd.Series) -> (int, float, float) :
    somme = series.sum()
    moyenne = series.mean()
    ecart = series.std()
    return (somme, moyenne, ecart)

t = create_series()
print(series_operations(t))


def create_dataframe(file_path: str) -> pd.DataFrame:
    read = pd.read_csv(file_path)
    return read
file_path = 'orders.csv'

creation = create_dataframe(file_path)
print(creation)



#4 pas réussi

