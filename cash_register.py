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

    if not amountPaid.isdigit() or amountDue.isdigit():
        raise TypeError("Amount Paid and Amount Due have to be numerical number")
    else:
        print("These are numerical numbers")
        return amountDue, amountPaid