# highest_score.py
'''
    Getting the highest score from a list.
    This is very similar to the previous task of the average height.
    I have included the average score and used the same prinicipal here.
    GEtting the highest score is based on whether the next iterate from the list is
    higher that highest_score and if it is then change the highest_score to that value,
    otherwise ignore and iterate to the next score in the list.
'''

student_scores = input('Input scores here: \n').split()
# student_scores = ['125', '125', '125', '130']
number_of_scores = 0
total_of_scores = 0
highest_score = 0
for i in student_scores:
    number_of_scores +=1
    i = int(i)
    total_of_scores += i
    if i > highest_score:
        highest_score = i

average_score = round(total_of_scores/number_of_scores)

print(f'The highest score is {highest_score}')
print(f'The average score is {average_score}')
