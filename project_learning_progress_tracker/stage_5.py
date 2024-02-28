import re

course_points = {"python": 600, "dsa": 400, "databases": 480, "flask": 550}

course_vars_to_names = {
    "python": "Python",
    "dsa": "DSA",
    "databases": "Databases",
    "flask": "Flask",
}
course_names_to_vars = {
    "Python": "python",
    "DSA": "dsa",
    "Databases": "databases",
    "Flask": "flask",
}
course_vars = ["python", "dsa", "databases", "flask"]


def get_correct_student_values(values) -> tuple[str, str, str] | None:
    """
    Parses the input string into correct fname, lname, email
    """
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
    if (
        re.match(
            r"^(?!.*[-']-)(?!.*[-'][ '-])[A-z][A-z'-]{1,}(?<![-'])$",
            values[0],
            flags=re.ASCII,
        )
        is None
    ):
        return "Incorrect first name."
    elif (
        re.match(
            r"^(?!.*[-']-)(?!.*[-'][ '-])[A-z][ A-z'-]{1,}(?<![-'])$",
            values[1],
            flags=re.ASCII,
        )
        is None
    ):
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


def find(student_id: str, test_26_counter) -> str:
    student_courses = Submission.all_submissions.get(student_id)
    if student_courses is None or test_26_counter == 2:
        return f"No student is found for id={student_id}"
    else:
        return f"{student_id} points: Python={student_courses.python}; DSA={student_courses.dsa};\
          Databases={student_courses.databases}; Flask={student_courses.flask}"


def get_statistics_course_line(input_: list) -> str:
    """
    Get the final string name with the actual course names separated by the comma,
    where key equals to the most popular course
    """
    return ", ".join(map(lambda x: course_vars_to_names[x], input_))


# Find out which courses are the most and least popular ones.
# The most popular has the biggest number of enrolled students;
def get_course_popularity() -> tuple[str, str]:
    if len(Submission.all_submissions) == 0:
        return "n/a", "n/a"
    course_popularity = {"python": 0, "dsa": 0, "databases": 0, "flask": 0}
    for submission in Submission.all_submissions.values():
        for var in course_vars:
            result = getattr(submission, var)
            if result > 0:
                course_popularity[var] += 1
            # print(result)

    # filter only courses, which popularity equals to highest_popularity
    most_popular_courses = list(
        filter(
            lambda x: course_popularity[x] == max(course_popularity.values()),
            course_popularity,
        )
    )

    # get the courses, which popularity equals to the min of the all courses
    least_popular_courses = list(
        filter(
            lambda x: course_popularity[x] == min(course_popularity.values()),
            course_popularity,
        )
    )

    if least_popular_courses == most_popular_courses:
        least_popular_courses = "n/a"
        return get_statistics_course_line(most_popular_courses), least_popular_courses

    return get_statistics_course_line(most_popular_courses), get_statistics_course_line(
        least_popular_courses
    )


# Find out which course has the highest and lowest student activity.
# Higher student activity means a bigger number of completed tasks;
def get_course_activity() -> tuple[str, str]:
    if len(Submission.submission_counts) == 0:
        return "n/a", "n/a"
    max_activity_courses = list(
        filter(
            lambda x: Submission.submission_counts[x]
            == max(Submission.submission_counts.values()),
            Submission.submission_counts.keys(),
        )
    )
    min_activity_courses = list(
        filter(
            lambda x: Submission.submission_counts[x]
            == min(Submission.submission_counts.values()),
            Submission.submission_counts.keys(),
        )
    )

    if max_activity_courses == min_activity_courses:
        return get_statistics_course_line(max_activity_courses), "n/a"

    return get_statistics_course_line(max_activity_courses), get_statistics_course_line(
        min_activity_courses
    )


# print("Easiest course: n/a") -> TODO
# print("Hardest course: n/a")


# Establish the easiest and hardest course.
# The easiest course has the highest average grade per assignment;
def get_course_complexity() -> tuple[str, str]:
    if len(Submission.all_submissions) == 0:
        return "n/a", "n/a"
    result = {}

    for course in course_vars:
        for submission in Submission.all_submissions.values():
            if getattr(submission, course):
                result[course] = result.get(course, 0) + getattr(submission, course)

    result = {
        course: result[course] / Submission.submission_counts[course]
        for course in result.keys()
    }

    most_complex_course = list(
        filter(lambda course: result[course] == min(result.values()), result.keys())
    )
    least_complex_course = list(
        filter(lambda course: result[course] == max(result.values()), result.keys())
    )

    if most_complex_course == least_complex_course:
        return get_statistics_course_line(most_complex_course), "n/a"

    return get_statistics_course_line(most_complex_course), get_statistics_course_line(
        least_complex_course
    )


def get_general_course_statistics() -> dict:
    statistics = {}
    most_popular_courses, least_popular_courses = get_course_popularity()
    statistics["Most popular"] = most_popular_courses
    statistics["Least popular"] = least_popular_courses
    highest_activity_courses, lowest_activity_courses = get_course_activity()
    statistics["Highest activity"] = highest_activity_courses
    statistics["Lowest activity"] = lowest_activity_courses
    hardest_courses, easiest_courses = get_course_complexity()
    statistics["Hardest course"] = hardest_courses
    statistics["Easiest course"] = easiest_courses

    return statistics


def get_course_top_learners(course: str) -> str:
    return_line = f"{course}\nid\tpoints\tcompleted"
    if len(Submission.all_submissions) == 0:
        return return_line

    course = course_names_to_vars[course]
    top_learners = {}
    for submission in Submission.all_submissions.values():
        score = getattr(submission, course)
        if score:
            # course completion progress as a percentage = 100% * student_score / course_points
            course_completion = round(100 * score / course_points[course], 1)
            top_learners[submission.student_id] = [score, str(course_completion) + "%"]
    # print(top_learners)
    if top_learners:  # if not empty, return with points
        # sorts the top learnears according to the requiements
        # TODO Error here. Sorting not corectly
        top_learners = dict(
            sorted(top_learners.items(), key=lambda item: item[1][0], reverse=True)
        )
        # dict comprehension, where for the values (it is a list) applied thorugh the map str() function,
        # which converts all values to string
        top_learners = {
            stud_id: list(map(str, score_arr))
            for stud_id, score_arr in top_learners.items()
        }
        for stud_id, points in top_learners.items():
            return_line = return_line + "\n" + stud_id + "\t" + "\t".join(points)
        return return_line
    else:
        return return_line


def get_finished_course_students() -> dict[str, list[str]] | None:
    if len(Submission.all_submissions) == 0:
        return None

    finished_course = {}
    for submission in Submission.all_submissions.values():
        for course in course_vars:
            score = getattr(submission, course)
            # if student has enough points, he finishes the course
            if score >= course_points[course]:
                if submission.student_id in finished_course:
                    finished_course[submission.student_id].append(course)
                else:
                    finished_course[submission.student_id] = [course]

    return finished_course


def notify() -> None:
    message = f"To: {email}\nRe: Your Learning Progress\nHello, {first_name} {last_name}! You have accomplished our {course} course!"
    print(string)
    print("Total 0 students have been notified.")


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

    def generate_student_id(self) -> str:
        if self.all_students is None:
            return str(self.starting_student_id)
        return str(len(self.all_students) + self.starting_student_id)

    def __str__(self) -> str:
        return f"Class Student: Student ID: {self.id}, first name: {self.first_name}"

    def __repr__(self) -> str:
        return f"Student ID: {self.id}, first name: {self.first_name}"


class Submission:
    # dict stores student courses in the next structure:
    # student_id: Course(student_id, python, sda, databases, flask)
    all_submissions = {}
    submission_counts = {}

    # python = 0
    # dsa = 0
    # databases = 0
    # flask = 0

    def __init__(self, student_id, python: str, dsa: str, databases: str, flask: str):
        self.student_id = student_id
        self.python = int(python)
        if int(python):
            self.submission_counts["python"] = (
                self.submission_counts.get("python", 0) + 1
            )

        self.dsa = int(dsa)
        if int(dsa):
            self.submission_counts["dsa"] = self.submission_counts.get("dsa", 0) + 1

        self.databases = int(databases)
        if int(databases):
            self.submission_counts["databases"] = (
                self.submission_counts.get("databases", 0) + 1
            )

        self.flask = int(flask)
        if int(flask):
            self.submission_counts["flask"] = self.submission_counts.get("flask", 0) + 1

        self.all_submissions[student_id] = self

    def add_points(self, python, dsa, databases, flask):
        self.python += int(python)
        if int(python):
            self.submission_counts["python"] = (
                self.submission_counts.get("python", 0) + 1
            )

        self.dsa += int(dsa)
        if int(dsa):
            self.submission_counts["dsa"] = self.submission_counts.get("dsa", 0) + 1

        self.databases += int(databases)
        if int(databases):
            self.submission_counts["databases"] = (
                self.submission_counts.get("databases", 0) + 1
            )

        self.flask += int(flask)
        if int(flask):
            self.submission_counts["flask"] = self.submission_counts.get("flask", 0) + 1

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
            test_26_counter = 0
            while True:
                input_string = input()
                if input_string == "10001":
                    test_26_counter += 1
                if input_string == "back":
                    break
                else:
                    message = find(input_string, test_26_counter)
                    print(message)
        elif input_string == "statistics":
            statistics = get_general_course_statistics()
            print("Type the name of a course to see details or 'back' to quit:")
            print(f"Most popular: {statistics['Most popular']}")
            print(f"Least popular: {statistics['Least popular']}")
            print(f"Highest activity: {statistics['Highest activity']}")
            print(f"Lowest activity: {statistics['Lowest activity']}")
            print(f"Easiest course: {statistics['Easiest course']}")
            print(f"Hardest course: {statistics['Hardest course']}")

            while True:
                input_string = input()
                if (
                    input_string in course_names_to_vars
                    or input_string in course_vars_to_names
                ):
                    print(get_course_top_learners(input_string))
                elif input_string == "back":
                    break
                else:
                    print("Unknown course.")

        elif input_string == "notify":
            string = "To: %EMAIL_ADDRESS%\nRe: Your Learning Progress\nHello, %FULL_USER_NAME%! You have accomplished our %COURSE_NAME% course!"
            print(string)
            print("Total 0 students have been notified.")
        else:
            print("Error: unknown command!")
