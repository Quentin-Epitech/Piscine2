import sys

## pas réussi à faire l'exercice 1 ni le 2 



def tuple_discovery(a, b, c, d) -> tuple:
    return (d, c, b, a)

def tuple_display(tpl: tuple):
    print("\n".join(map(str, tpl)))

tuple_display(tuple_discovery(1, 2, 3, 4))




def set_discovery(l1: list, l2: list) -> tuple:
    set1 = set(l1)
    set2 = set(l2)
    union_set = set1 | set2 
    intersection_set = set1 & set2 
    difference_set = set1 - set2
    symmetric_difference_set = set1 ^ set2
    return (union_set, intersection_set, difference_set, symmetric_difference_set)
          
l1 = [1, 2, 3, 4, 5]
l2 = [10, 2, 4, 8, 12]
res = set_discovery(l1, l2)
for elem in res:
    print(elem)


def power_via_comprehension(numbers: list[int]) -> list[int] : 
    return [x**2 if x < 0 else -x for x in numbers]

l = [1,-2,-3, 4,-5]
print(power_via_comprehension(l))