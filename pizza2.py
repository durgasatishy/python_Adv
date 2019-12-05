#obj ---> size,toppings ... print out requesetd toppings

def make_pizza(size,*toppings):
    """summarize the pizzas we are about to make"""
    print(f"\nmaking a {size}-inch pizza with the flowwing toppings")
    for topping in toppings:    # here for loop will split the values with in the orbitrary variable.
        print(f"-{topping}")

make_pizza(12,'corn','tomatos','olives')
make_pizza(16,'extracheese','chicken')