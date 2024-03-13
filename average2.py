grades = ()
while True:
    grade = input("enter a grade or type exit to finish ")
    if grade.lower() == 'exit':
        break
    try:
        grades.append(float(grade))
    except ValueError:
        print("please enter a valid number")


if grades:
    average = sum(grades) / len(grades)
    print(f"your final grade:{average}")
else:
    print("no grades entered")