"""
1- Use a for loop to print the numbers from 1 to 20 inclusive
2- One million: Make a list of the numbers from one to one million, and then
use a for loop to print the numbers.
3- Summing a million: Make a list of the numbers from one to one million, and then use min()
and max() to make sure your list actually starts at one and ends at one million. Also, use the
4-sum() function to see how quickly python can add a million
5- Odd numbers use the third argument of the range function to make a list of the odd numbers from 1 to 20.
Use a for loop to print each number
6- Threes: Makes a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list
7. A number raised to the third power is called a cube. Make a list of the first 10 cube, and use a for loop to print on
the value of each cube
8. Cube comprehension. Use a list comprehension to generate a list of the first 10 cubes

"""
# for item in range(1, 21):
#   print(item)
# for item in range(1, 1_000_001):
#    print(item)
numbers = []
# for item in range(1, 1_000_001):
#    numbers.append(item)

# print(f"sum : {sum(numbers)}")
# print(f"min: {min(numbers)}")
# print(f"max: {max(numbers)}")

odd_numbers = []
for item in range(1, 21, 3):
    if item % 2 != 0:
        odd_numbers.append(item)
print(f"odd numbers {odd_numbers}")

for number in range(3, 31, 3):
    print(number)
third_power = []

for value in range(1, 30, 3):
    third = value ** 3
    third_power.append(third)

print(third_power)

cube_comprenhension = [value ** 3 for value in range(1, 10)]
print(cube_comprenhension)

example = [value * 2 for value in range(1, 10)]
print(example)

sum_5 = [ value + 5 for value in range(1,11, 2)]
print(sum_5)