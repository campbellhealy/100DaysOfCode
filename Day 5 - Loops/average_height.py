# average_height.py
'''
    Input a number of height into a list.
    Do not use LEN or SUM, but calulate the number of items in the list, 
    and the total sum of these values.
    This will allow for the calculation of the average, as an integer, not float.

'''

student_heights = input('Input heights here: \n').split()
# student_heights = ['125', '125', '125', '125']
number_of_students = 0
total_of_heights = 0

for i in student_heights:
    number_of_students +=1
    i = int(i)
    total_of_heights += i

# average_height_i = int(total_of_heights/number_of_students)
average_height = round(total_of_heights/number_of_students)
# print(number_of_students)
# print(total_of_heights)
# print(f'The Average height is {average_height_i}')
print(f'The Average height is {average_height}')

