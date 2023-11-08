
places= ['Japan','Bali','London','Spain','Monaco']
print ("Original:", places)

print ("Alphabetical:", sorted(places))
#sorts the list alphabetically

print ("Original 2:", places)

print ("Reverse alphabetical:", sorted(places, reverse=True))
#sorts the list alphabetically but in reverse

print ("Original 3:", places)

places.reverse()
#reverses the list

print ('Reversed:', places)

places.reverse()
#reverses the list again, so it went back to the original order

print ('Original after reversing:', places)

places.sort()
#sorts list temporarily

print ('Alphabetical order with Sort():', places)

places.sort(reverse=True)
#reverses the list

print ('Reverse alphabetical with Sort():', places)
