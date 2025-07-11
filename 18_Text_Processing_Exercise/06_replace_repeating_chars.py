some_string = input()
final_string = some_string[0]
for character in some_string:
    if character != final_string[-1]:
        final_string += character
print(final_string)
