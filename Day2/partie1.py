import pandas 
import csv 
def read_one_line(filename: str) -> str:
    with open(filename, "r") as file:
        return file.readline()

ex1=read_one_line("orders.csv")
print(ex1)

def write_text(filename: str, text: str) : 
    f = open(filename, "w")
    f.write(text)
    f.close()

ex2=write_text("exo2.txt","je m'appelle quentin")
print(ex2)


def copy_characters(input_file: str, output_file: str, nb: int) : 
    try:
        with open(input_file, 'r') as infile:
            content = infile.read(nb)
        with open(output_file, 'a') as outfile:
             if content or nb == 0:
                 outfile.write(content + '\n')
    except:
        print("Erreur lors de la copie")

ex3 = copy_characters("orders.csv","exo3.txt",100)
print(ex3)

    


def write_text_better(filename: str, text: str) :
    with open(filename,"w") as file : 
        file.write(text)


ex5 = write_text_better("exo5.txt","je m'appelle quentin")
print(ex5)

def copy_characters_better(input_file: str, output_file: str, nb: int):
    with open(input_file,"r",) as file ,open (output_file,"a") as rendu :
        texte=file.read(nb)
        rendu.write(f"{texte}\n")


ex5bis = copy_characters_better("orders.csv","exo5bis.txt",100)
print(ex5bis)

