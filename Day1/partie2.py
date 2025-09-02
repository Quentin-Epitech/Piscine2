def concat_with_space(a: str, b: str) -> str : 

    return a + ' ' + b

print(concat_with_space('Hello', 'World!'))
print(concat_with_space('', ''))


def format_with_fstring(username: str, age: int) -> str :
    return (f'hello {username},you are {age} years old ! ')

print(format_with_fstring('Quentin', 19))
