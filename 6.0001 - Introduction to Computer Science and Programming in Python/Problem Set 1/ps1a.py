import sys

def is_number(user_input, limit):
    """
    fucntion checks input is a number
    
    user input: string
    
    limit: float or integer if there is a limit otherwise null type
    
    returns: Boolean
    
    """
    try:
        float(user_input)
    except ValueError:
        return False
    
    user_input=float(user_input)
    
    if limit==None:
        return 0<user_input
    else:
        return 0<user_input<=limit
    
def get_input(input_string, upper_limit=None):
    """This function ensures the data entered is a number
    
    input value to be checked: user input
    input string: string describing what to enter
    
    returns: float

    """
  
    value = input(input_string)
   
    while not is_number(value, limit=upper_limit):
        value = input("Previous entry wasn't a number within the required range. Please enter a number, so that 0 < number{limit}, or type 'exit' to quit this script. ".format(limit='' if upper_limit==None else ' <= '+str(upper_limit)) + input_string)
        if value == 'exit':
            sys.exit()
    return float(value) 

if __name__=='__main__':
    
    #create required variables that are fixed
    current_savings = 0 
    months = 0
    
    #create variables which are taken as fixed but could be trivially changed to take user input
    portion_down_payment = 0.25
    annual_return = 0.04
    
    #change annual return to monthly return
    monthly_return = 1+annual_return/12
    
    #get user to input the required information
    annual_salary = get_input("Enter annual salary: £")
    portion_saved = get_input("Enter the portion of your salary that you will save: ", upper_limit=1)
    total_cost = get_input("Enter cost of Dream House: £")
   
    #loop until downpayment can be afforded
    while current_savings < (portion_down_payment*total_cost):
        months+=1
        current_savings*= monthly_return
        current_savings+=(portion_saved*annual_salary/12)
    
    print("It will take you", months, "months of saving before you can buy your dream house!")
    




    
    
    
    