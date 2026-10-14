def cash_register(amountDue, amountPaid):
    """"
    This app calculate required change and returns it note denominations
    Parameters: 
        amunt due -> float
        amount paid -> float
    Returns change in not denomination
    """
    notes = {
        "20000": 200,
        "10000" : 100,
        "5000" : 50,
        "2000" : 20,
        "1000" : 10,
        "500" : 5,
        "200" : 2,
        "100" : 1,
        "50" : 0.5,
        "20" : 0.2,
        "10" : 0.1
    }

    if not isinstance(amountDue, (int, float)) or not isinstance(amountPaid, (int, float)):
        raise TypeError("Amount paid and amount due must be numerical values")
    if amountDue > amountPaid:
        raise ValueError("Amount paid must be equal or greater than amount due")
    else:
        valid_amountPaid= float(amountPaid)
        valid_amountDue = float(amountDue)

    change_in_cents = round(valid_amountPaid * 100) - round(valid_amountDue * 100)
    
    return change_in_cents






















 