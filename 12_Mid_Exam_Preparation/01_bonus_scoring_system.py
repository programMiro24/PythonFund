from math import ceil

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
max_bonus_student_attendances = 0

if number_of_lectures:
    for student in range(number_of_students):
        attendances = int(input())
        total_bonus = attendances / number_of_lectures * (5 + additional_bonus)
        if total_bonus > max_bonus:
            max_bonus = total_bonus
            max_bonus_student_attendances = attendances

max_bonus = ceil(max_bonus)

print(f"Max Bonus: {max_bonus}.")
print(f"The student has attended {max_bonus_student_attendances} lectures.")
