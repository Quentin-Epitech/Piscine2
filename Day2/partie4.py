import pandas as pd

def pandas_csv_read(file: str) -> pd.DataFrame :
    lecture = pd.read_csv(file)
    return lecture 

ex1 = pandas_csv_read("orders.csv")
print(ex1)


def pandas_csv_write(file: str, headers: list, data: list[tuple]) : 
    table = pd.DataFrame(data, columns=headers)
    table.to_csv(file)

ex2 = pandas_csv_write("exo2part4.csv", ["a", "b", "c"], [(1, 2, 3), (4, 5, 6), (7, 8, 9)])