toppings= input('What topping would you like to add:')
while toppings != 'quit':
    #if user input "quit" the code stops
    print ('I will add', toppings, 'to your pizza!')
    toppings = input ('would you like to add more?:')
    #keeps asking user to input a topping
else:
    print ('Thank you, have a great day.')
