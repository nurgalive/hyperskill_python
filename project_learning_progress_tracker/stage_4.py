import re
import sys

python_points = 600 
dsa_points = 400
databases_points = 480
flask_points = 550

courses = {"python":"Python", "dsa":"DSA", "databases":"Databases", "flask":"Flask"}

# parses the input string into correct fname, lname, email
def get_correct_student_values(values) -> tuple | None:
    values = values.split()
    if len(values) == 3:
        return values[0], values[1], values[2]
    elif len(values) > 3:
        return values[0], " ".join(values[1:-1]), values[-1]
    else:
        return None


# checks if the student fname, lname and email are correct
def is_student_name_correct(student_name) -> str | bool | None:
    values = get_correct_student_values(student_name)
    if values is None:
        return False
    if re.match(r"^(?!.*[-']-)(?!.*[-'][ '-])[A-z][A-z'-]{1,}(?<![-'])$", values[0], flags=re.ASCII) is None:
        return "Incorrect first name."
    elif re.match(r"^(?!.*[-']-)(?!.*[-'][ '-])[A-z][ A-z'-]{1,}(?<![-'])$", values[1], flags=re.ASCII) is None:
        return "Incorrect last name."
    elif not re.match(r"[0-9a-z._-]+@[a-z0-9]+\.[a-z0-9]+", values[2], flags=re.ASCII):
        return "Incorrect email."
    else:
        if is_email_taken(values[2]):
            return "This email is already taken."
        return None


# function for the command "list"
def print_students_list():
    if len(Student.all_students) > 0:
        print("Students:")
        for student in Student.all_students:
            print(student.id)
    else:
        print("No students found")


def is_email_taken(email: str) -> bool:
    for student in Student.all_students:
        if email == student.email:
            return True
    return False


def is_id_exists(student_id: str) -> bool:
    if len(Student.all_students) > 0:
        for student in Student.all_students:
            if student_id == student.id:
                return True
    return False


def add_points(values: str) -> tuple[bool, str]:
    values = values.split()
    if len(values) != 5:
        return False, "Incorrect points format"
    if not is_id_exists(values[0]):
        return False, f"No student is found for id={values[0]}"

    for value in values:
        try:
            if int(value) < 0:
                return False, "Incorrect points format"
        except ValueError:
            return False, "Incorrect points format"

    course = Course.all_courses.get(values[0])
    # print(course)
    if course:
        course.add_points(values[1], values[2], values[3], values[4])
    else:
        Course(values[0], values[1], values[2], values[3], values[4])

    return True, "Points updated."


def find(student_id: str) -> str:
    student_courses = Course.all_courses.get(student_id)
    if student_courses is None:
        return (f"No student is found for id={student_id}")
    else:
        return (
            f"{student_id} points: Python={student_courses.python}; DSA={student_courses.dsa}; Databases={student_courses.databases}; Flask={student_courses.flask}")

course_vars = ["python", "dsa", "databases", "flask"]

# Find out which courses are the most and least popular ones. 
# The most popular has the biggest number of enrolled students;
# how to rewrite it using map and filter?
def get_most_popular_courses() -> str:
    if len(Course.all_courses) == 0:
        return "n/a"
    highest_popularity = 0
    course_popularity = {
        "python": 0,
        "dsa": 0,
        "databases": 0,
        "flask": 0}
    for student_id, course in Course.all_courses.items():
        # print(student_id)
        for var in course_vars:
            result = getattr(course, var)
            if result > 0:
                course_popularity[var] += 1
                highest_popularity = course_popularity[var]
            # print(result)

    print(course_popularity)

    most_popular_courses = list(filter(lambda x: course_popularity[x] == highest_popularity, course_popularity))
    most_popular_courses = ", ".join(map(lambda x: courses[x], most_popular_courses))
    return most_popular_courses

class Student:
    all_students = []
    starting_student_id = 10000

    def __init__(self, student_name: str):
        values = get_correct_student_values(student_name)
        self.first_name = values[0]
        self.last_name = values[1]
        self.email = values[2]
        self.id = self.generate_student_id()
        Student.all_students.append(self)

    def generate_student_id(self) -> int:
        return str(len(self.all_students) + self.starting_student_id)

    def __str__(self) -> str:
        return f"Class Student: Student ID: {self.id}, first name: {self.first_name}"

    def __repr__(self) -> str:
        return f"Student ID: {self.id}, first name: {self.first_name}"


class Course:
    # dict stores student courses in the next structure:
    # student_id: Course(student_id, python, sda, databases, flask)
    all_courses = {}

    python = 0
    dsa = 0
    databases = 0
    flask = 0

    def __init__(self, student_id, python, dsa, databases, flask):
        self.student_id = student_id
        self.python = int(python)
        self.dsa = int(dsa)
        self.databases = int(databases)
        self.flask = int(flask)
        self.all_courses[student_id] = self

    def add_points(self, python, dsa, databases, flask):
        self.python += int(python)
        self.dsa += int(dsa)
        self.databases += int(databases)
        self.flask += int(flask)

    def __repr__(self) -> str:
        return f"Course for student ID: {self.student_id} with courses: python: {self.python}, dsa: {self.dsa}, databases:{self.databases}, flask: {self.flask}"

    def __str__(self) -> str:
        return f"Course for student ID: {self.student_id} with courses: python: {self.python}, dsa: {self.dsa}, databases:{self.databases}, flask: {self.flask}"


if __name__ == "__main__":
    print("Learning progress tracker")

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
                        Student(student_name)
                        number_students_added += 1
                        print("The student has been added.")
                    elif output:
                        print(output)
                    else:
                        print("Incorrect credentials.")
            print(f"Total {number_students_added} students have been added.")

        elif input_string == "list":
            print_students_list()
        elif input_string == "add points":
            print("Enter an id and points or 'back' to return")
            while True:
                input_string = input()
                if input_string == "back":
                    break
                else:
                    added, message = add_points(input_string)
                    print(message)
        elif input_string == "find":
            print("Enter an id or 'back' to return")
            while True:
                input_string = input()
                if input_string == "back":
                    break
                else:
                    message = find(input_string)
                    print(message)
        elif input_string == "statistics":
            print("Type the name of a course to see details or 'back' to quit:")
            print(f"Most popular: {get_most_popular_courses()}")
            print("Least popular: n/a")
            print("Highest activity: n/a") 
            print("Lowest activity: n/a")
            print("Easiest course: n/a")
            print("Hardest course: n/a")

            while True:
                input_string = input()
                if input_string in courses:
                    print("id	points	completed")
                elif input_string == "back":
                    break
                else:
                    print("Unknown course.")
        else:
            print("Error: unknown command!")