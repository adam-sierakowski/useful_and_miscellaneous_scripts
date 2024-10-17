def get_variants(number: str, separators=[',', '.', ' ']):
    """This creates various feasable formats of a number,
    based on a number that looks like a Python int or float.
    Example input: 2000000.00
    Example output:
    {'full_number': ['2,000,000.00', '2.000.000,00', '2 000 000.00'],
    'no_point_zero': ['2,000,000', '2.000.000', '2 000 000'],
    'in_million': ['2 million']}
    """
    number = str(number)
    parts = number.split('.')
    integer_part = parts[0]
    decimal_part = '.' + parts[1] if len(parts) > 1 else ''
    
    def add_separator(integer_part, separator):
        if len(integer_part) <= 3:
            return integer_part
        return add_separator(integer_part[:-3], separator) + separator + integer_part[-3:]
    
    results = {
        "full_number" : [],
        "no_point_zero" : [],
        "in_million" : []
    }
    
    for separator in separators:
        if separator == "." and decimal_part != '':
            results["full_number"].append(add_separator(integer_part, separator) + "," + decimal_part[1:])
        elif separator == "." and decimal_part == '':
            results["full_number"].append(add_separator(integer_part, separator))
        else:
            results["full_number"].append(add_separator(integer_part, separator) + decimal_part)
    
    if re.match(r'\.0+', decimal_part):
        for separator in separators:
            results["no_point_zero"].append(add_separator(integer_part, separator))

    if re.search(r'000000$', integer_part) and re.match(r'\.0+', decimal_part):
        results["in_million"] = [integer_part[:-6] + " million"]

    return results
