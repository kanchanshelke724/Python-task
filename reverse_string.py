def reverse_string(user):
    result = ""
    for char in user:
        result = char + result
    return result

user = input("Enter a string: ")
print(reverse_string(user))
