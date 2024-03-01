import unittest

from stage_5 import (
    Student,
    Submission,
    add_points,
    get_finished_course_students,
    notify,
)


class TestNotifyWithoutData(
    unittest.TestCase
):  # Test, so pylint: disable=missing-class-docstring
    def test_get_students_finished_course(
        self,
    ):  # Test, so pylint: disable=missing-function-docstring
        result = get_finished_course_students()
        # print(result)
        self.assertEqual(result, None)

    def test_notify(self):  # Test, so pylint: disable=missing-function-docstring
        emails, students_notified = notify()
        # print(emails)
        # print(students_notified)
        self.assertEqual(None, emails)
        self.assertEqual("Total 0 students have been notified.", students_notified)


# {"python": 600, "dsa": 400, "databases": 480, "flask": 550}
class TestNotifyWithData(
    unittest.TestCase
):  # Test, so pylint: disable=missing-class-docstring
    def setUp(self) -> None:
        students = [
            "Joe Does ato@pro.net",
            "Bob Pops pops@pro.net",
            "Lar Var varl@pro.net",
        ]
        points = ["10000 590 380 470 500", "10001 600 380 1 0", "10002 500 400 480 0"]
        for student in students:
            Student(student)

        for point in points:
            added, message = add_points(
                point
            )  # Just in case, so pylint: disable=unused-variable

    def tearDown(self) -> None:
        Student.all_students.clear()
        Submission.all_submissions.clear()

    def test_get_student(self):  # Test, so pylint: disable=missing-function-docstring
        student = Student.get_student("10000")
        # print(student)
        self.assertEqual(
            "10000", student.id
        )  # pyright: ignore reportOptionalMemberAccess

    def test_get_students_finished_course(
        self,
    ):  # Test, so pylint: disable=missing-function-docstring
        result = get_finished_course_students()
        # print(result)
        self.assertEqual(result, {"10001": ["python"], "10002": ["dsa", "databases"]})

    def test_notify(self):  # Test, so pylint: disable=missing-function-docstring
        emails, students_notified = notify()
        # print(emails)
        # print(students_notified)
        self.assertEqual(
            [
                "To: pops@pro.net\nRe: Your Learning Progress\nHello, Bob Pops! You have accomplished our Python course!",
                "To: varl@pro.net\nRe: Your Learning Progress\nHello, Lar Var! You have accomplished our DSA course!",
                "To: varl@pro.net\nRe: Your Learning Progress\nHello, Lar Var! You have accomplished our Databases course!",
            ],
            emails,
        )
        self.assertEqual("Total 2 students have been notified.", students_notified)

        emails, students_notified = notify()
        # print(emails)
        # print(students_notified)
        self.assertEqual([], emails)
        self.assertEqual("Total 0 students have been notified.", students_notified)


if __name__ == "__main__":
    unittest.main()
