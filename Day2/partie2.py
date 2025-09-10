import pandas as pd
import csv 

def native_csv_read(file: str) -> list[tuple]:
   resultat = []
   with open(file, mode="r") as csvfile:
         reader = csv.reader(csvfile, delimiter=";")
         next(reader) 
         for index, line in enumerate(reader):
            resultat.append((index,) + tuple(line))
   return resultat
 
input_file = "orders_semicolon.csv"
t = native_csv_read(input_file)
print(t)



def native_csv_write(file: str, headers: list, data: list[tuple]) :
    with open(file, mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(headers)
        for ligne in data:
            writer.writerow(ligne[1:])


exo2 = native_csv_write("exo2.csv",["index","product","quantity","total_price"],t)
print(exo2)