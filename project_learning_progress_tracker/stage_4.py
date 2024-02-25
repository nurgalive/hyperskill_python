import re
import sys

course_points = {"python": 600, "dsa": 400, "databases": 480, "flask": 550}

course_vars_to_names = {"python":"Python", "dsa":"DSA", "databases":"Databases", "flask":"Flask"}
course_names_to_vars = {"Python":"python", "DSA":"dsa", "Databases":"databases", "Flask":"flask"}

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

    course = Submission.all_submissions.get(values[0])
    # print(course)
    if course:
        course.add_points(values[1], values[2], values[3], values[4])
    else:
        Submission(values[0], values[1], values[2], values[3], values[4])

    return True, "Points updated."


def find(student_id: str) -> str:
    student_courses = Submission.all_submissions.get(student_id)
    if student_courses is None:
        return (f"No student is found for id={student_id}")
    else:
        return (
            f"{student_id} points: Python={student_courses.python}; DSA={student_courses.dsa}; Databases={student_courses.databases}; Flask={student_courses.flask}")

course_vars = ["python", "dsa", "databases", "flask"]

# Find out which courses are the most and least popular ones. 
# The most popular has the biggest number of enrolled students;
def get_most_popular_courses() -> tuple[str, str]:
    if len(Submission.all_submissions) == 0:
        return "n/a"
    highest_popularity = 0
    course_popularity = {
        "python": 0,
        "dsa": 0,
        "databases": 0,
        "flask": 0}
    for student_id, submission in Submission.all_submissions.items():
        # print(student_id)
        for var in course_vars:
            result = getattr(submission, var)
            if result > 0:
                course_popularity[var] += 1
                highest_popularity = course_popularity[var]
            # print(result)

    # print(course_popularity)

    # filter only courses, which popularity equals to highest_popularity
    most_popular_courses = list(filter(lambda x: course_popularity[x] == highest_popularity, course_popularity))
    # get the final string name with the actual course names separated by the comma, where key equals to the most popular course
    most_popular_courses = ", ".join(map(lambda x: course_vars_to_names[x], most_popular_courses))

    # get the courses, which popularity equals to the min of the all courses
    least_popular_courses = list(filter(lambda x: course_popularity[x] == min(course_popularity.values()), course_popularity))
    least_popular_courses = ", ".join(map(lambda x: course_vars_to_names[x], least_popular_courses))

    if least_popular_courses == most_popular_courses:
        least_popular_courses = "n/a"

    return most_popular_courses, least_popular_courses

# print(f"Most popular: {statistics["Most popular"]}")
# print("Least popular: n/a")
# print("Highest activity: n/a") 
# print("Lowest activity: n/a")
# print("Easiest course: n/a")
# print("Hardest course: n/a")

def get_general_course_statistics() -> dict:
    statistics = {}
    most_popular_courses, least_popular_courses = get_most_popular_courses()
    statistics["Most popular"] = most_popular_courses
    statistics["Least popular"] = least_popular_courses

    return statistics

def get_course_top_learners(course: str) -> str:
    return_line = "id\tpoints\tcompleted"
    if len(Submission.all_submissions) == 0:
        return return_line

    course = course_names_to_vars[course]
    top_learners = {}
    for submission in Submission.all_submissions.values():
        score = getattr(submission, course)
        if score:
            # course completion progress as a percentage = 100% * student_score / course_points
            course_completion = round(100 * score / course_points[course], 1)
            top_learners[submission.student_id] = [str(score), str(course_completion) + "%"]
    # print(top_learners)
    if top_learners: # if not empty, return with points
        # sorts the top learnears according to the requiements
        top_learners = dict(sorted(top_learners.items(), key=lambda item: item[1], reverse=True))
        for stud_id, points in top_learners.items():
            return_line = return_line + "\n" + stud_id + "\t" + "\t".join(points)
        return return_line
    else: 
        return return_line

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


class Submission:
    # dict stores student courses in the next structure:
    # student_id: Course(student_id, python, sda, databases, flask)
    all_submissions = {}

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
        self.all_submissions[student_id] = self

    def add_points(self, python, dsa, databases, flask):
        self.python += int(python)
        self.dsa += int(dsa)
        self.databases += int(databases)
        self.flask += int(flask)

    def __repr__(self) -> str:
        return f"Submissions for student ID: {self.student_id} with courses: python: {self.python}, dsa: {self.dsa}, databases:{self.databases}, flask: {self.flask}"

    def __str__(self) -> str:
        return f"Submissions for student ID: {self.student_id} with courses: python: {self.python}, dsa: {self.dsa}, databases:{self.databases}, flask: {self.flask}"


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
            statistics = get_general_course_statistics()
            print("Type the name of a course to see details or 'back' to quit:")
            print(f"Most popular: {statistics['Most popular']}")
            print(f"Least popular: {statistics['Least popular']}")
            print("Highest activity: n/a") 
            print("Lowest activity: n/a")
            print("Easiest course: n/a")
            print("Hardest course: n/a")

            while True:
                input_string = input()
                if input_string in course_names_to_vars:
                    print(get_course_top_learners(input_string))
                elif input_string == "back":
                    break
                else:
                    print("Unknown course.")
        else:
            print("Error: unknown command!")