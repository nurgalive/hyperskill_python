from stage_3 import Student, print_students_list, is_student_name_correct, Course, add_points


for student in ["Joe Does ato@pro.net"]:
    output = is_student_name_correct(student)
    print(output)
    if output is None:
        Student(student)

print_students_list()

added, message = add_points("10000 1 2 3 4 5")
if added:
    print("All added")
else:
    print(message)

print(Course.all_courses)

# print([student.id for student in Student.all_students])

