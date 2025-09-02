def multiply(a: int, b: int) -> int:

    multiplication = a * b
    return multiplication

print(multiply(2, 3))


def compare (a: int, b: int) :
    if a > b :
        return print ("Le premier nombre est plus grand que le second")
    elif a < b :
        return print ("Le premier nombre est plus petit que le second")
    else :
        return print ("Les deux nombres sont égaux")
    
compare(2, 1)


def counting(x: int):
    resultat = []
    for i in range(1, x + 1, 2): 
        resultat.append(str(i))
    print(', '.join(resultat) + ',')
    return resultat

counting(10)


def ask_user():
    mot = input()
    print(f"Vous avez entrer : {mot}")

    while (mot !="exit"):
        mot = input()

        if (mot == "exit") :
            break
        
    print(f"Vous avez entrer : {mot}")

ask_user()

def safe_divide(a: int, b: int) -> float | None :
    
    try:
        result = a / b
        return result
    
    except ZeroDivisionError: 
        return None

print(safe_divide(1, 4))
print(safe_divide(1, 0))


def display_square(size: int, char: chr) :
    for i in range(size):
        print(size*char)

display_square(6, '*')
