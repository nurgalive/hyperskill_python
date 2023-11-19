from stage_3 import Student, Course, add_points, print_students_list, is_id_exists
import unittest

class TestAddPoints(unittest.TestCase):
    def setUp(self):
        student = "Joe Does ato@pro.net"
        Student(student)
        # print(Student(student))
        print_students_list()

    def test_correct_points(self):
        points = "10000 1 2 3 4"
        added, message = add_points(points)
        print(added, message)
        print(Course.all_courses)
        self.assertEqual(added, True)
        self.assertEqual(message, "Points updated")

    def test_is_id_exists(self):
        self.assertEqual(is_id_exists(10000), True)
        print("Tested test_is_id_exists")


if __name__ == '__main__':
    unittest.main()