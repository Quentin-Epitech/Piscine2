import operations.basic_ops
import operations.advanced_ops

def do_op(a, b, carac):
    if carac == '+':
        return operations.basic_ops.add(a, b)
    elif carac == '-':
        return operations.basic_ops.subtract(a, b)
    elif carac == '*':
        return operations.advanced_ops.multiply(a, b)
    elif carac == '/':
        return operations.advanced_ops.safe_divide(a, b)
    else:
        return None
    

print(do_op(1, 1, '+'))
print(do_op(1, 1,'-'))
print(do_op(11, 11,'*'))
print(do_op(2, 2, '/'))
print(do_op(2, 0, '/'))