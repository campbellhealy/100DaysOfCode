# add_evens.py
'''
    Add the even numbers from a range.
'''

def even_adder(a,b):
    ''' 
        Add all the even numbers between two values inclusive, using range method
    '''
    if a > b: # Error catch
        c = b 
        b = a 
        a = c 
    total = 0
    b +=1 # This negates the exclusion of the second value
    for i in range (a,b):
        if i%2 == 0:
            total += i
    print(total)

def even_stepper(a,b):
    '''
        This is version using the step method in range.
    '''
    total = 0
    if a%2 != 0:
        a +=1
    b +=1  # This negates the exclusion of the second value
    for i in range(a,b,2):
        if i%2 == 0:
            total += i
    print(total)



even_stepper(1,2)
# even_adder(0,2)
# even_adder(0,20)
# even_adder(0,10)