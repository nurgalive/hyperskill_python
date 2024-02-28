import unittest

from stage_5 import Student, Submission, add_points, get_finished_course_students


class TestNotifyWithoutData(unittest.TestCase):
    def test_get_students_finished_course(self):
        result = get_finished_course_students()
        # print(result)
        self.assertEqual(result, None)


# {"python": 600, "dsa": 400, "databases": 480, "flask": 550}
class TestNotifyWithData(unittest.TestCase):
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
            added, message = add_points(point)

    def tearDown(self) -> None:
        Student.all_students.clear()
        Submission.all_submissions.clear()

    def test_get_students_finished_course(self):
        result = get_finished_course_students()
        print(result)
        # self.assertEqual(result, None)


if __name__ == "__main__":
    unittest.main()
