import pandas as pd

def pandas_excel_read(file: str, sheet: str) -> pd.DataFrame :
    table = pd.read_excel(file,sheet_name=sheet)
    return table


exo1 = pandas_excel_read("sales.xlsx", "orders")
print(exo1)


def pandas_excel_write(data: pd.DataFrame, filename: str) :
    try:
        with pd.ExcelWriter(filename, mode="a", if_sheet_exists="replace", engine="openpyxl") as writer:
            data.to_excel(writer, sheet_name="orders", index=False)
   
    except FileNotFoundError:
        with pd.ExcelWriter(filename, mode="w", engine="openpyxl") as writer:
            data.to_excel(writer, sheet_name="orders", index=False)


exemple = pd.DataFrame({
    
    "product": ["airpods", "iphone", "macbook"],
    "quantity": [10, 5, 2],
    "total_price": [100, 200.7, 199.6]
})
exo2 = pandas_excel_write(exemple, "sales.xlsx")


def pandas_excel_selective_read(filename: str) -> pd.DataFrame:
    lecture = pd.read_excel(filename, sheet_name="orders", skiprows = list(range(1, 11)), usecols=["product", "total_price"]) 
    groupe = lecture.groupby("product", as_index=False).sum()
    
    return groupe

exo3 = pandas_excel_selective_read("sales2.xlsx")
print(exo3)

def pandas_excel_manipulation(filename: str) : ## pas réussi 
 return
