# -*- coding: utf-8 -*-
import sys
from ps1a import is_number
from ps1a import get_input

def in_range(number,comparison,tolerance):
    '''
    '''
    return (comparison-tolerance)<= number <= (comparison + tolerance)
     

def money_saved(months, savings, guess, salary, s_a_r, monthly_return, downpayment, tolerance):
    '''
    '''
    for i in range(months):
        if savings > (downpayment+epsilon):
            break
        savings*= monthly_return
        savings+=(guess*salary/12)
        if ((i+1)%6)==0:
            salary*=(1+s_a_r)
    return savings

def bisection_search(high, low, guess, value, target, tolerance):
    '''
    '''
    
    if value<target-tolerance:
        low = (guess*10000)+1
    elif value>target+tolerance:
        high = (guess*10000)-1
    else:
        pass
    
    return high,low
        
    
    
    
if __name__=='__main__':
    
    #initiate all variables which are taken as fixed  
    total_cost = 1000000 
    portion_down_payment = 0.25 
    current_savings = 0 
    annual_return = 0.04 
    monthly_return= 1+annual_return/12
    months = 36
    semi_annual_raise=0.07
    
    #create guess variable 
    guess = 0
    
    #create variable for bisection search
    epsilon = 100
    high = 10000
    low = 0
    
    #create count to store the number of steps taken in our bisection search
    count = 0
    
    #create a total_saved which will store the amount of money saved after each guess
    total_saved = 0
    downpayment_needed=total_cost*portion_down_payment

    annual_salary = get_input("Enter annual salary: £")

    while not in_range(total_saved,downpayment_needed,epsilon):
        count+=1
        if high==low:
            print("Can't afford down payment in this time period!")
            break
        guess = (high+low)//2
        guess = guess/10000
        total_saved=money_saved(months,current_savings, guess,annual_salary,semi_annual_raise, monthly_return, downpayment_needed, epsilon)
        high, low = bisection_search(high,low,guess,total_saved,downpayment_needed,epsilon)
        
    if in_range(total_saved,downpayment_needed,epsilon):
        print("Best guess is to save",(guess*100),"% of your salary per month to afford home in this time period")
        print("number of bisection steps take was:",count)
