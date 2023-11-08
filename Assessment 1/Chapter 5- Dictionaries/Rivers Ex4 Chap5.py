rivers = {'Nile River': 'Egypt', 'Amazon River': 'South America', 'Yangtze River': 'China'}
for key, value in rivers.items():
#Calls both key and value
    print ('\nThe', key, 'is located in', value)
#displays both values and keys
for key in rivers.keys():
#calls only keys
    print ('\nRiver name:', key)
#displays only keys
for value in rivers.values():
#call only values
    print ('\nlocation:', value)
#displays only values
