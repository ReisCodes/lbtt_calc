def calc_lbbt(price):
    """
    This Function will take the value of the house as input and
    return the landing and buildings transaction tax they need to pay.
    given this is their only house, and it's for personal use. (Not first house either)
    """
    max_tax_bracket_1 = (250000 - 145000) * 0.02                    # Create variables for the max tax in each bracket
    max_tax_bracket_2 = ((325000 - 250000) * 0.05) + max_tax_bracket_1
    max_tax_bracket_3 = ((750000 - 325000) * 0.1) + max_tax_bracket_2

    # Depending on the price the function will perform the required calculation to return the correct tax pay
    # if the price is equal or less than 0, the function will return a value Error
    if price < 0:
        raise ValueError("This price is invalid!")
    elif 0 < price < 145000:
        return 0
    elif 145001 < price < 250000:
        tax_bracket_1 = (price - 145000) * 0.02
        return tax_bracket_1
    elif 250001 < price < 325000:
        tax_bracket_2 = (price - 250000) * 0.05
        return max_tax_bracket_1 + tax_bracket_2
    elif 325001 < price < 750000:
        tax_bracket_3 = (price - 325000) * 0.1
        return max_tax_bracket_2 + tax_bracket_3
    else:
        tax_bracket_4 = (price - 750000) * 0.12
        return max_tax_bracket_3 + tax_bracket_4
