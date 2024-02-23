import unittest

from stage_4 import (
    Student,
    Course,
    get_most_popular_courses,
    add_points
)

class TestStatisticsCommandWithoutData(unittest.TestCase):

    def testStatisticsCommand(self):
        output = get_most_popular_courses()
        self.assertEqual(output, "n/a")

class TestStatisticsCommandWithData(unittest.TestCase):
    def setUp(self) -> None:
        students = ["Joe Does ato@pro.net", "Bob Pops pops@pro.net"]
        points = ["10000 1 2 3 4",  "10001 0 1 1 0"]
        for student in students:
            Student(student)
        
        for point in points:
            added, message = add_points(point)
    
    def tearDown(self) -> None:
        Student.all_students.clear()
        Course.all_courses.clear()

    def test_most_popular_course(self):
        output = get_most_popular_courses()
        # print(output)
        self.assertEqual("DSA, Databases", output)

if __name__ == '__main__':
    unittest.main()