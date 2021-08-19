# use_parameter.py

def say_hi_to(name, location):
    print(f'Hi there {name}')
    print(f' I hear you are from {location}')


say_hi_to('John', 'England')
say_hi_to('Paul', 'Wales')
say_hi_to('George', 'Scotland')
say_hi_to(location='Glasgow', name='Jimmy')