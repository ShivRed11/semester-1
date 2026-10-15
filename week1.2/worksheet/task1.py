# Worksheet 1.2: Task 1 Solution
integer_grade_1 = input("What mark did you get on the test (0 - 100)?")
if not integer_grade_1.isdecimal():
    print("Error: Grade must be an integer between 0 and 100")
    exit()

integer_grade_2 = int(integer_grade_1)

if integer_grade_2 > 100:
    print("Error: Grade must be an integer between 0 and 100")
    exit()



if integer_grade_2 <= 39:
    print(f"{integer_grade_2} is a Fail")
elif 40 <= integer_grade_2 <= 69:
    print(f"{integer_grade_2} is a Pass")
else:
    print(f"{integer_grade_2} is a Distiction")