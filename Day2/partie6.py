import pandas as pd

def pandas_json_read(file: str) -> pd.DataFrame :
    tableau = pd.read_json(file)
    return tableau

def pandas_json_write(file: str, data: pd.DataFrame) :

    data.to_json(file,orient = "records",indent=4)
    print(data.to_json(orient='records', indent=4))


Lecture = pandas_json_read('complex_orders.json')
pandas_json_write('complex_orders_nouveau.json', Lecture)


def  pandas_complex_json(file: str, product: dict) : ## pas réussi
    return
