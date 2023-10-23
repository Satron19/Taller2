def add(num_1, num_2):
    result = num_1 + num_2
    print(f'{num_1} + {num_2} is equal to {result}')
    return result


def subtract(num_1, num_2):
    result = num_1 - num_2
    print(f'{num_1} - {num_2} is equal to {result}')
    return result

def multiply(num_1, num_2):
    result = num_1 * num_2
    print(f'{num_1} * {num_2} is equal to {result}')
    return result

def divide(num_1, num_2):
    if num_2 != 0:
        result = num_1 / num_2
        print(f'{num_1} / {num_2} is equal to {result}')
        return result
    else:
        print("Error: Cannot divide by zero.")
        return None

def power(num_1, num_2):
    result = num_1 ** num_2
    print(f'{num_1} raised to the power of {num_2} is equal to {result}')
    return result

def modulus(num_1, num_2):
    if num_2 != 0:
        result = num_1 % num_2
        print(f'The modulus of {num_1} and {num_2} is {result}')
        return result
    else:
        print("Error: Cannot divide by zero (modulus operation).")
        return None