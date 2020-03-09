def convert(number):
    result = ""
    factors = {
        "Pling": 3,
        "Plang": 5,
        "Plong": 7,
    }

    for x in factors:
        if number % factors[x] == 0:
            result += x
    
    if not result:
        result = str(number)

    return result
