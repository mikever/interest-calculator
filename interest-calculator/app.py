current_principal
annual_addition
years_to_grow
interest_rate
compound_interest_times_annually
# if False, additions will be at the end of each compounding period
is_addition_at_start = True

current_principal = input('Enter the starting principal? ')
annual_addition = input('How much will be added each year? ')
years_to_grow = input('How many years will this grow? ')
interest_rate = input('What is the expected interest rate? ')


def compouding_period():
    answer = input('Will additions start or end of each compounding period?')
