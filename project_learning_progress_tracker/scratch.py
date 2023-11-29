from stage_3 import (
    Student, 
    print_students_list, 
    is_student_name_correct, 
    Course, 
    add_points,
    is_id_exists
    ) 


for student in ["Joe Does ato@pro.net"]:
    output = is_student_name_correct(student)
    print("Output", output)
    if output is None:
        Student(student)

print(is_id_exists("10000"))

# print("10000" == "10000")
