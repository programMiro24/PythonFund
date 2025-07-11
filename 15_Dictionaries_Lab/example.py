"""
keys = ['name', 'age', 'major']
values = ['Ivan', 22, 'Developer']

student = dict(zip(keys, values))

print(student)
"""

'''
student = {
    'name': 'Pesho',
    'age': 25,
    'major': 'Developer',
    'language': 'Python'
}

"""
print(student['name'])
print(student['age'])
print(student['major'])
print(student['language'])
print(student.keys())
print(student.values())
print(student.items())
"""

for key, value in student.items():
    print(key, value)
'''

text = """
Hello I'm here of there! Hello i'm print.And print of print of loop actualy is micro code.
"""

word_count = {}
for word in text.lower().split():
    word = word.strip('.,')
    word_count[word] = word_count.get(word, 0) + 1

sorted_word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))

print(sorted_word_count)
