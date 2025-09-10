def struct_index_display(elems):
    for i, elem in enumerate(elems):
        print(f"{i} = {elem}")


struct_index_display([1, 2, 3, 4, 5])








def combine_lists(l1: list, l2: list) -> None | list:

    if len(l1) != len(l2):
        return None
    return list(zip(l1, l2))

res1 = combine_lists([1, 2, 3], [4, 5, 6])
print(res1)

res2 = combine_lists([1, 2], [4, 5, 6])
print(res2)


def display_combined_lists(l: list):
    for elemid, (elem1, elem2) in enumerate(l):
        print(f"{elemid} = {elem1} - {elem2}")

res = combine_lists([1, 2, 3], [4, 5, 6])
display_combined_lists(res)


#exo 3 non réussi 





def remove_negatives(numbers):
    return [x for x in numbers if x >= 0]

def keep_strings(elements):
    return [x for x in elements if type(x) == str]


t1 = remove_negatives([-1, 2, 3, 4, -5, 6, 7])
print(t1)  

t2 = keep_strings(["Hello", 1, 3, "spam", 5.5, (1, 2)])
print(t2)  







def cut_in_two(numbers: list[float]):
   milieu = len(numbers) // 2
   return (numbers[:milieu], numbers[milieu:])

t1, t2 = cut_in_two([1, 2, 3, 4, 5, 6, 7, 8,9])
print(t1)  
print(t2)  

