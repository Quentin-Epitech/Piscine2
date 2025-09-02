def multiply(a: int, b: int) -> int:

    multiplication = a * b
    return multiplication


def safe_divide(a: int, b: int) -> float | None :
    
    try:
        result = a / b
        return result
    
    except ZeroDivisionError: 
        return None
    