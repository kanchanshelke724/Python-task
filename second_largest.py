def find_second_largest(numbers):
    if len(numbers) < 2:
        return "List must have at least 2 numbers"

    largest = float('-inf')
    second_largest = float('-inf')

    for num in numbers:
        if num > largest:
            largest = num

    for num in numbers:
        if num > second_largest and num < largest:
            second_largest = num

    return second_largest

user_input = input("Enter numbers: ")
numbers = [int(num) for num in user_input.split()]
result = find_second_largest(numbers)
print(f"The second largest number is: {result}")