guests = ['Janel', 'Vince', 'Danish']
for guest in guests:
#for loop to make it easier
    print ('I am delighted to inform that you are invited to dinner,', guest)

print (guests[0], 'Cant make it to dinner')
print ('Not coming:', guests[0])
guests.remove ('Janel')
#removes a guest from the list
print ('Coming:', guests[0], guests[1])
#displays remaining guests

guests.insert (0, 'Dhovie')
#inserts a guest in a the original list

guests = ['Dhovie', 'Vince', 'Danish']
for guest in guests:
#for loop to make it easier
    print ('I am delighted to inform that you are invited to dinner,', guest)

print ('Im really sorry i can only invite 2 people for dinner')
poppedguest = guests.pop(0)
#another way to remove a guest
print ('Im sorry but you dont fit', poppedguest, 'maybe next time.')

for poppedguest in guests:
#displays the remaining guests
    print ('I am delighted to inform that you are still invited to dinner,', poppedguest)

del guests [0]
#deletes the remaining guest
del guests [0]
#deletes the remaining guest
print ('Remaining guests:',guests)
