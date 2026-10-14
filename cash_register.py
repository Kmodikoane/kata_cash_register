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

        change = valid_amountPaid - valid_amountDue

        denominations = [200.00, 100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00, 0.5]

        breakdown = {}

        remaining = change

        for note_coin in denominations:
            count = (remaining // note_coin)
            remaining = remaining % note_coin
            breakdown[note_coin] = int(count)

        print(f"The remainder of your change is: {round(remaining, 2)}")
        print(f"Your change due is: R{round(change,2)}")
        for key, value in breakdown.items():
            if key >= 1.00:
                print(f"R{key} | {value}")
            else:
                print(f"{key}c | {value}")
      
        #print(breakdown, round(remaining,2))           

    return breakdown, remaining




















 