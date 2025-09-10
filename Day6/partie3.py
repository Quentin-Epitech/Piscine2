import pandas as pd
from datetime import datetime
import numpy as np


def impute_region(df: pd.DataFrame) -> pd.DataFrame:
    implementation = {
        'Japan': 'Japan',
        'China': 'APAC',
        'Australia': 'APAC',
        'France': 'EMEA',
        'Germany': 'EMEA',
        'UK': 'EMEA',
        'USA': 'NA',
        'Canada': 'NA',
        'Norway': 'EMEA',
        'Finland': 'EMEA',
        'Austria': 'EMEA'}
    df.loc[:, 'region'] = df.apply(
        lambda row: implementation.get(row['country'], row['region']) 
        if pd.notna(row['country']) else row['region'], axis=1)
    
    df = df.dropna(subset=['region'])
    df.reset_index(drop=True, inplace=True)
    return df

df = pd.read_csv("sales_outliers.csv")
df_impute = impute_region(df)
print(df_impute)

def impute_quantity(df: pd.DataFrame) -> pd.DataFrame:
    moyenne = df['quantity'].mean()
    df['quantity'] = df['quantity'].fillna(moyenne)
    return df

df_impute = impute_quantity(df)
print(df_impute)


def impute_category(df: pd.DataFrame) -> pd.DataFrame :
    return


def handle_inconsistent_dealsize(df: pd.DataFrame) -> pd.DataFrame:
    valeurs = []
    for val in df['dealsize']:
        i = str(val).strip().lower()
        if i in ['s', 'small', '1']:
            valeurs.append('S')
        elif i in ['m', 'medium', '2']:
            valeurs.append('M')
        elif i in ['l', 'large', '3']:
            valeurs.append('L')
        else:
            valeurs.append('M')
    df['dealsize'] = valeurs
    return df


df_impute = handle_inconsistent_dealsize(df)
print(df_impute)


def handle_inconsistent_dates(df: pd.DataFrame) -> pd.DataFrame : 
    return


def retrieve_quantity_outliers(df: pd.DataFrame) -> pd.DataFrame:
   return


def normalize_total_price(df: pd.DataFrame) -> pd.DataFrame:
    df['total_price'] = df['total_price'].apply(lambda x: np.log1p(x))
    df['total_price'] = df['total_price'].round(10)
    return df

df_norm = normalize_total_price(df)
print(df_norm.head(10))


def normalize_quantity(df: pd.DataFrame) -> pd.DataFrame : 
    moyenne_quantité = df['quantity'].mean()
    ecart_type_quantité = df['quantity'].std()
    df['quantity'] = (df['quantity'] - moyenne_quantité) / ecart_type_quantité
    df['quantity'] = df['quantity'].round(10)
    return df

df_norm = normalize_quantity(df)
print(df_norm.head(10))

def normalize_unit_price(df: pd.DataFrame) -> pd.DataFrame : 
    return
