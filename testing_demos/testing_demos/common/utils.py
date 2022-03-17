def transform_to_2digits(number):
    if number < 10:
        return f'0{number}'
    return str(number)
