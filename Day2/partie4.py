import pandas as pd

def pandas_csv_read(file: str) -> pd.DataFrame :
    lecture = pd.read_csv(file)
    return lecture 


def pandas_csv_write(file: str, headers: list, data: list[tuple]) : 
    table = pd.DataFrame(data, columns=headers)
    table.to_csv(file)

