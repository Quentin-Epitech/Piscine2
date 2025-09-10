import pandas as pd 

def create_multi_index_df(df: pd.DataFrame) -> pd.DataFrame : 
    tri = df.set_index(["year", "region"]).sort_index()
    return tri

exo1 = pd.read_csv("sales.csv")

print(create_multi_index_df(exo1))

def retrieve_multi_index_data(df: pd.DataFrame, year: int, region: str) -> pd.DataFrame :
    return df.loc[(year, region)]

exo2 = create_multi_index_df(exo1)
print(retrieve_multi_index_data(exo2, 2003, "APAC"))


def multi_index_aggregate(df: pd.DataFrame) -> pd.DataFrame :
    ajout = df.groupby(['year', 'region']).agg(quantite=('quantity', 'sum'),arrondissement=('total_price', 'sum')).round(2)
    return ajout

exo3 = create_multi_index_df(exo1)
print(multi_index_aggregate(exo3))

def columns_multi_index(df: pd.DataFrame) -> pd.DataFrame :
    ajout = df.groupby(['year', 'region', 'category']).agg(quantity=('quantity', 'sum'),
    arrondissement=('total_price', 'sum')).round(2)
    multi_index_df = ajout.unstack(level='category')
    return multi_index_df

exo4 = create_multi_index_df(exo1)
print(columns_multi_index(exo4))


def swap_columns_multi_index(df: pd.DataFrame) -> pd.DataFrame : 
    swapped_df = df.swaplevel(axis=1).sort_index(axis=1)
    return swapped_df


exo5 = columns_multi_index(exo1)  
print(swap_columns_multi_index(exo5))

def retrieve_multi_index_column(df: pd.DataFrame, category: str) -> pd.DataFrame :
    return df[category]

exo6_1 = swap_columns_multi_index(exo5)
print(retrieve_multi_index_column(exo6_1, "Motorcycles"))

def retrieve_multi_index_basic(df: pd.DataFrame, category: str, year: int) -> pd.DataFrame:
    return df.loc[year, :][category]

exo6_2 = swap_columns_multi_index(exo5)

print(retrieve_multi_index_basic(exo6_2, "Motorcycles", 2003))



def retrieve_multi_index_advanced(df: pd.DataFrame, region: str, sub_column: str) -> pd.DataFrame:
    if isinstance(df.columns, pd.MultiIndex):
        try:
            df_région = df.xs(key=region, level='region')
            résultat = df_région.xs(key=sub_column, axis=1, level=1)
            return résultat
        except KeyError as e:
            raise KeyError(f"Erreur : {str(e)}")
    else:
        raise ValueError("Erreur : Le DataFrame n'a pas de MultiIndex.")

exo6_3 = swap_columns_multi_index(exo5)

print(retrieve_multi_index_basic(exo6_3, "Motorcycles", 2003))

def create_pivot_table_basic(df: pd.DataFrame) -> pd.DataFrame : 
    parametre = pd.pivot_table(
        df,values=['quantity', 'total_price'],index=['year', 'region'],columns='category',aggfunc={'quantity': 'sum', 'total_price': 'sum'}).round(2)
    return parametre


def avg_price_rolling_window(df: pd.DataFrame) -> pd.DataFrame: 
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values(by='date').set_index('date')
    df['rolling_avg'] = df['total_price'].rolling(window="7D", min_periods=3).mean().round(2)
    df = df.reset_index()
    return df

exo8 = pd.read_csv("sales.csv")
exo8_moyenne = avg_price_rolling_window(exo8)
print(exo8_moyenne.head(10))


def highlight_outliers(df: pd.DataFrame) -> pd.DataFrame : 
    return

