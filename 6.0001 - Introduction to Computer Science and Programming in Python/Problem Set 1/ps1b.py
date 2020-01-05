import sys
from ps1a import is_number
from ps1a import get_input

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
    semi_annual_raise = get_input("Enter the percentage salary raise you'll get as a decimal: ",upper_limit=1)
    
    #loop until downpayment can be afforded
    while current_savings < (portion_down_payment*total_cost):
        months+=1
        current_savings*= monthly_return
        current_savings+=(portion_saved*annual_salary/12)
        if (months%6)==0:
            annual_salary*=(1+semi_annual_raise)
        else:
            pass
    
    print("It will take you", months, "months of saving before you can buy your dream house!")
    