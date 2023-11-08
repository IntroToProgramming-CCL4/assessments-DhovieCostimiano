guests = ['Janel', 'Vince', 'Danish']
#list
for guest in guests:
#you can use for loops in a list
    print ('I am delighted to inform that you are invited to dinner,', guest)
#For loops can shorten a long code

print (guests[0], 'Cant make it to dinner')
print ('Not coming:', guests[0])
guests.remove ('Janel')
#removes guest from the list
print ('Coming:', guests[0], guests[1])
#displays remaining guests

guests.insert (0, 'Dhovie')
#inserts guest in the list

guests = ['Dhovie', 'Vince', 'Danish']
for guest in guests:
    print ('I am delighted to inform that you are invited to dinner,', guest)
#for loop again to make it shorter
