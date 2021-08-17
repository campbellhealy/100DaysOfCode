# fizzbuzz.py
'''
    Count a sequence of numbers.
    If the number is divisbke by three say 'Fizz'
    If the number is divisble by five say 'Buzz'.
    If the number is divisble by both three and five say 'FizzBuzz'

    I am creating a list initially. This is a step that is not needed just
    to solve the problem as the range (0,101) could have replaced the variable
    name in the for loop of the fizzbuzz.
    I just like to break out variables, that can be changed, from the main code to prevent
    errors in the future.
'''
# Create list of numbers
number_list = []
for i in range (0,101):
    number_list.append(i)

for i in number_list:
    if i %3 ==0 and i %5 ==0:
        print('FizzBuzz')
    elif i %3 ==0:
        print('Fizz')
    elif i %5 ==0:
        print('Buzz')
    else:
        print(i)

