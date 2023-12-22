def intrinsic_value():
    book_value = 20
    return book_value

def current_market_price():
    market_price = 15 # sample price
    return market_price

def smart_bid():
    asset_amount = intrinsic_value() - current_market_price()
    return asset_amount

# def future_asset_amount(years):
def future_asset_amount():
    current_asset_amount = smart_bid()
    # years = years
    years = 0
    value_not_compounded = current_asset_amount * years
    return value_not_compounded

# def future_compounded_asset_amount(years):
def future_compounded_asset_amount():
    current_asset_amount = smart_bid()
    # years = int(years)
    years = 7
    interest_year1 = 1.08
    interest_year2 = 2.16
    interest_year3 = 4.32
    interest_year4 = 8.64
    interest_year5 = 17.28
    interest_year6 = 34.56
    interest_year7 = 69.12
    value_compounded = current_asset_amount
    # sample of 7 years below: # replace with compounding calculation
    if years == 1:
        value_compounded = value_compounded + interest_year1
    elif years == 2:
        value_compounded = value_compounded + interest_year2
    elif years == 3:
        value_compounded = value_compounded + interest_year3
    elif years == 4:
        value_compounded = value_compounded + interest_year4
    elif years == 5:
        value_compounded = value_compounded + interest_year5
    elif years == 6:
        value_compounded = value_compounded + interest_year6
    elif years == 7:
        value_compounded = value_compounded + interest_year7
    else:
        value_compounded = 0
    return value_compounded


