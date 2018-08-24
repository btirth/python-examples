def simple_interest(principal,interest,duration_in_years):
    total_interest=interest*0.01*duration_in_years*principal
    total_amount=principal+total_interest
    print("total_interest is {0}".format(total_interest))
    print("total_amount is {0}".format(total_amount))
    
