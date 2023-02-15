from pprint import pprint

def calculateTax(input_summ, input_percent, inpu_fun_assign):
    amount = input_summ    
    percent = input_percent  
    tax_name = inpu_fun_assign
    count_percent = amount * (percent / 100)
    total = {
        f"amount for calculation of {tax_name}" : f"{amount}$",
        "name of func assignment"               : tax_name,
        "value of percentag"                    : f"{percent}%",
        "total tax fee"                         : f"{count_percent}$",
    }
    
    pprint(total)

#I have used dictionary, because it is pretty comfortable method to contain data as key + discribs.
