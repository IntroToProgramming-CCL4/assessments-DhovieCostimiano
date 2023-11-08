print ("Pastrami is out of stock")
sandwich_orders = ['Cheese Sandwich', 'Pastrami','Bacon Sandwich', 'Pastrami','Grilled Cheese', 'Pastrami', 'Chicken Sandwich']
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')
    #removes pastrami from the existing list
finished_sandwiches =[]
#emplty list

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    #this puts all the sandwich in sandwich_orders inside current_sandwich
    print("\nI made your",current_sandwich)
    #this prints out that you make the sandwich
    finished_sandwiches.append(current_sandwich)
    #appends puts all the sandwiches in the finished_sandwiches which was before empty
print()
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich , " is done\n")
    #displays finished sandwiches
