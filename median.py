"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

numbers.sort()
length = len(numbers)

if length % 2 == 0:
    median_avg = (numbers[int(length / 2)] + numbers[int(length / 2 - 1)]) / 2
    print(median_avg)
else:
    print(numbers[int((length - 1) / 2)])
