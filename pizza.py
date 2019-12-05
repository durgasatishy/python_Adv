#introduction to python modules

def make_pizza(*toppings):    #orbitrary arguments  -> by using * in the parameter we can pass many values we want, it wont throw error.
    """print the list of toppings that have been requested"""  # here """ codes will be called as doc strings
    print(toppings)


make_pizza('pepperoni')
make_pizza('corn','extracheese','olives')

"""control + s  to save file
 play button to execute file"""
# above is called multi line commenting

