guests = ['Janel', 'Vince', 'Danish']
for guest in guests:
    print ('I am delighted to inform that you are invited to dinner,', guest)

print (guests[0], 'Cant make it to dinner')
print ('Not coming:', guests[0])
guests.remove ('Janel')
print ('Coming:', guests[0], guests[1])

guests.insert (0, 'Dhovie')

guests = ['Dhovie', 'Vince', 'Danish']
for guest in guests:
    print ('I am delighted to inform that you are invited to dinner,', guest)