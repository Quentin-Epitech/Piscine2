import pandas as pd
import pyarrow.parquet as pq


def read_parquet(filename: str) -> pd.DataFrame :
     fichier = pd.read_parquet(filename)
     return fichier.head(10)

print(read_parquet("flights.parquet"))

def read_parquet_columns(filename: str, columns: list) -> pd.DataFrame : 
     fichier = pd.read_parquet(filename,columns=columns)
     return fichier 

print(read_parquet_columns("flights.parquet",["DISTANCE"]))


def read_parquet_batch(filename: str, batch_size: list) -> pd.DataFrame :
    fichier = pq.ParquetFile(filename)
    tableau = []
    for batch in fichier.iter_batches(batch_size=batch_size):
        parametre = batch.to_pandas().head(2).reset_index(drop=True)
        tableau.append(parametre)
    return pd.concat(tableau).reset_index(drop=True)


print(read_parquet_batch("flights.parquet",2)) ## prend énormement de temps à charger

