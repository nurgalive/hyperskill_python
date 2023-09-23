import re
import sys

def get_correct_values(values):
    values = values.split()
    if len(values) == 3:
        return values[0], values[1], values[2]
    elif len(values) > 3:
        return values[0], " ".join(values[1:-1]), values[-1]
    else:
        return None

def is_student_name_correct(student_name):
    values = get_correct_values(student_name)
    if values is None:
        return False
    # print(values)
    # if re.match(r"[a-zA-Z'-]{2,}", values[0], flags=re.ASCII) is None:
    if re.match(r"^(?!.*[-']-)(?!.*[-'][ '-])[A-z][A-z'-]{1,}(?<![-'])$", values[0], flags=re.ASCII) is None:
        return "Incorrect first name."
    elif re.match(r"^(?!.*[-']-)(?!.*[-'][ '-])[A-z][ A-z'-]{1,}(?<![-'])$", values[1], flags=re.ASCII) is None:
        return "Incorrect last name."
    elif not re.match(r"[0-9a-z._-]+@[a-z0-9]+\.[a-z0-9]+", values[2], flags=re.ASCII):
        return "Incorrect email."
    else:
        return None

print("Learning progress tracker")

students = []
while True:
    input_string = input()

    if input_string.strip() == "":
        print("No input.")
    elif input_string == "exit":
        print("Bye!")
        break
    elif input_string == "back":
        print("Enter 'exit' to exit the program.")
    elif input_string == "add students":
        print("Enter student credentials or 'back' to return")
        number_students_added = 0
        while True:
            student_name = input()
            if student_name == "back":
                break
            else:
                output = is_student_name_correct(student_name)
                if output is None:
                    students.append(student_name)
                    number_students_added += 1
                    print("The student has been added.")
                elif output:
                    print(output)
                else:
                    print("Incorrect credentials.")
        print(f"Total {number_students_added} students have been added.")
    else:
        print("Error: unknown command!")