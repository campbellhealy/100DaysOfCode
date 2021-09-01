# area_calculator.py
'''
    The code is to determine the number of tins of paint required to 
    cover a specific wall size.
    Constants: 
        The paint tin as a fixed amount of coverage coverage        
'''
from math import ceil

def coverage_of_wall(height, width):
    one_tin_coverage = 5 # metres square
    number_of_tins = (height * width)/one_tin_coverage
    tins = ceil(number_of_tins)

    # Output
    print(f'For a wall of height {height}mtr and width of {width}mtr.')
    if tins >1:
        print(f'You need {tins} tins of paint for the job. \n')
    else:
        print(f'You need {tins} tin of paint for the job. \n')

coverage_of_wall(5,5)
coverage_of_wall(5,4)
coverage_of_wall(4,3)
coverage_of_wall(1,2)