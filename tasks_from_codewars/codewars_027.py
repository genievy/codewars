

def fizz_buzz_custom(string_one: str = "Fizz", string_two: str = "Buzz", num_one=3, num_two=5):
    result = []
    for i in range(1, 100):
        if not i % num_one:
            if not i % num_two:
                result.append(string_one + string_two)
            else:
                result.append(string_one)
        elif not i % num_two:
            result.append(string_two)
        else:
            result.append(i)
    return result


print(fizz_buzz_custom())
