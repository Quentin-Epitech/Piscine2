import pandas as pd

def pandas_excel_read(file: str, sheet: str) -> pd.DataFrame :
    table = pd.read_excel(file)
    return table

def pandas_excel_write(data: pd.DataFrame, filename: str) :
    with pd.ExcelWriter(filename, if_sheet_exists="replace") as writer:
        data.to_excel(writer,sheet_name="orders")

def pandas_excel_selective_read(filename: str) -> pd.DataFrame : 
     
     tableau = pd.read_excel(filename, sheet_name='orders', skiprows=10, usecols=['product', 'total_price'])  
     groupe = tableau.groupby('product').sum()
    
     return groupe


def pandas_excel_manipulation(filename: str) : ## pas réussi 
 return



    