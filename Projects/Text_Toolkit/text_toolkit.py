# 🧵 Python Text Transformation Toolkit

# Step 1: Display a menu to the user
print("🧠 Welcome to the Text Transformation Toolkit!")
print("Choose a transformation:")
print("1. Reverse Text")
print("2. Convert to Uppercase")
print("3. Convert to Lowercase")
print("4. Title Case")
print("5. Count Vowels")
print("6. Remove All Spaces")
print("7. Replace Vowels with '*'")
print("8. Check if Palindrome")
print("9. Word Frequency Counter")

# Step 2: Get the user's choice
choice = int(input("Enter the number corresponding to your choice: "))

# Step 3: Get the input string
text = input("Enter the text: ")

# Step 3.1: Variable for answer
answer = ""

# Step 4: Apply the selected transformation
if choice == 1:
    # TODO: Reverse the text using slicing or a loop
    answer = text[::-1]

elif choice == 2:
    # TODO: Convert the text to uppercase using string methods
    answer = text.upper()

elif choice == 3:
    # TODO: Convert the text to lowercase using string methods
    answer = text.lower()

elif choice == 4:
    # TODO: Convert the text to title case (capitalize each word)
    answer = text.title()
    """ 
    new = ""
    slicing_string = ""
    index = previous_index = 0
    for character in text:
        if character == ' ':
            slicing_string = text[previous_index:index+1]
            new += slicing_string.capitalize()
            previous_index = index + 1
        index += 1
    slicing_string = text[previous_index:index + 1]
    new += slicing_string.capitalize()
    answer = new
    """
elif choice == 5:
    # TODO: Count how many vowels are in the text (a, e, i, o, u)
    text = text.lower()
    answer = text.count('a') + text.count('e') + text.count('i') + text.count('o') + text.count('u')
    """
    counter = 0
    for character in text:
        if character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u':
            counter += 1
    answer = counter
    """

elif choice == 6:
    # TODO: Remove all spaces from the string using replace() or join()
    answer = text.replace(' ', '')

elif choice == 7:
    # TODO: Replace all vowels with "*" using a loop or comprehension
    new_string = ""
    index = previous_index = 0
    for character in text:
        if ((character.lower() == 'a' or character.lower() == 'e' or
                character.lower() == 'i' or character.lower() == 'o' or
                character.lower() == 'u')):
            new_string += (text[previous_index:index] + "*")
            previous_index = index + 1
        index += 1
    answer = new_string

elif choice == 8:
    # TODO: Check if the text is a palindrome (ignoring case and spaces)
    # ignoring case and spaces
    text = text.lower()
    text = text.replace(' ', '')
    second_text = text[::-1]
    if text == second_text:
        answer = "The text is palindrome"
    else:
        answer = "The text isn't palindrome"

elif choice == 9:
    # TODO: Count the frequency of each word and display the result
    previous_index = 0
    text = text.lower()
    for character_index in range(len(text)):
        if text[character_index] == ' ':
            word = text[previous_index:character_index]
            frequency_of_each_word = text.count(word)
            previous_index = character_index + 1
            print(frequency_of_each_word)
    word = text[previous_index:len(text)]
    frequency_of_each_word = text.count(word)
    print(frequency_of_each_word)

else:
    raise SystemExit("❌ Invalid choice! Please restart the program.")

if choice != 9:
    print(f"Transformed Text: {answer}")
