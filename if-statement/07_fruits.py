favorite_fruits = ["mango", "cerezas", "mandarina"]

if 'mango' in favorite_fruits:
    print("mango is in favorite fruits")

if 'cerezas' in favorite_fruits:
    print(f'{favorite_fruits[1]} are in favorite fruits')

if 'mandarina' in favorite_fruits:
    print("Mandarinas are in favorite fruits")

fruit = input('Favorite fruit').lower()

if fruit in favorite_fruits:
    print(f"{fruit} is in favorite fruit")
