#formating an output
x = "Liverpool"
y = "Premier League"

print ('{} are gonna win the {}'.format(x,y))

print ('{0} are gonna finish {1}'.format('Man City', 'second'))

print ('{1} might get relegated to the {0}'.format('Championship', 'Man Utd'))

#using keyword arguments to format the string

print ('{team} are the best of the {statement} teams'.format(team='Sheffield Utd', statement='promoted'))

what_position = input('Please enter what position in a number where Arsenal will finish: ')

print ('You think Arsenal will finish', what_position)