# your_life_in_weeks.py
'''
    Calculate your life in weeks.
    To get the result as per the teaching the following is correct.
    A couple of things have to be mentioned.
    Only using the age in years cannot get you the days, weeks months until 90yrs old.
    So the f string should use 'or' instead of 'and', like I have done in my code.
    As it is calculating the number of days/weeks/months for 90 - age(years)
'''


years = 90
months = 12
weeks = 52
days = 365
age = int(input('What is your age? \n'))

age_days_left = ((years * days) - age * days)
age_weeks_left = ((years * weeks) - age * weeks)
age_months_left = ((years * months) - age * months)
if_i_lived_to_ninety = 90

print(f'You have {age_days_left} days,{age_weeks_left} weeks or {age_months_left} months until you are 90 yrs')