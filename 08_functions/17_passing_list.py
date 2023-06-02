"""
As we are learned we could pass any data types as a parameter
Another  example is passing list
"""


def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_model = unprinted_designs.pop()
        print(f'Printing model: {current_model}')
        completed_models.append(current_model)


def show_completed_models(completed_models):
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['A123', 'BC124', 'PJ98']
completed_models = []
print_models(unprinted_designs, completed_models)
print("\nThe following models have been printed")
show_completed_models(completed_models)

