def cash_register(amountDue, amountPaid):
    """"
    This app calculate required change and returns it note denominations
    Parameters: 
        amunt due -> float
        amount paid -> float
    Returns change in not denomination
    """

    if not isinstance(amountDue, (int, float)) or not isinstance(amountPaid, (int, float)):
        raise TypeError("Amount paid and amount due must be numerical values")
    if amountDue > amountPaid:
        raise ValueError("Amount paid must be equal or greater than amount due")
    if amountDue == amountPaid:
        return 0
    
    else:
        valid_amountPaid= float(amountPaid)
        valid_amountDue = float(amountDue) 

        change = round(valid_amountPaid *100) - round(valid_amountDue * 100)

        denominations = [20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50]

        breakdown = {}

        remaining = change

        print(f"Your change due is: R{round(valid_amountPaid - valid_amountDue),2}")

        for note_coin in denominations:
            count = (remaining // note_coin)
            remaining = remaining % note_coin
            breakdown[note_coin] = count

        for key, value in breakdown.items():
            if key >= 1.00:
                print(f"R{key/100} | {value}")
            else:
                print(f"{key/100}c | {value}")

    print(breakdown)

    return breakdown, remaining

cash_register(34887, 34932.21)




















 