"""
list in a dictionary
"""
pizza = {
    'crust': 'crust',
    'toppings': ['mushrooms', 'extra cheese']
}
print(f"You ordered a pizza with crust: {pizza['crust']} and the toppings:")
for topping in pizza['toppings']:
    print(topping)

