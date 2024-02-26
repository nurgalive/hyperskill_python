import unittest

from stage_4 import (
    Student,
    Submission,
    get_course_popularity,
    add_points,
    get_course_top_learners,
    get_course_activity,
    get_general_course_statistics,
    get_course_complexity
)

class TestStatisticsCommandWithoutData(unittest.TestCase):

    def testStatisticsCommand(self):
        output = get_course_popularity()
        self.assertEqual(output, ('n/a', 'n/a'))

    def test_most_popular_course(self):
        res = get_course_top_learners("Python")
        # print(res)
        self.assertEqual("Python\nid\tpoints\tcompleted", res)


class TestStatisticsCommandWithData(unittest.TestCase):
    def setUp(self) -> None:
        students = ["Joe Does ato@pro.net", "Bob Pops pops@pro.net"]
        points = ["10000 10 2 3 4",  "10001 1 1 1 0", "10001 1 1 1 0"]
        for student in students:
            Student(student)
        
        for point in points:
            added, message = add_points(point)
    
    def tearDown(self) -> None:
        Student.all_students.clear()
        Submission.all_submissions.clear()

    def test_get_course_popularity(self):
        most_popular_courses, least_popular_courses = get_course_popularity()
        # print(most_popular_courses)
        # print(least_popular_courses)
        self.assertEqual("Python, DSA, Databases", most_popular_courses)
        self.assertEqual("Flask", least_popular_courses)
    
    def test_get_course_activity(self):
        highest_activity_courses, lowest_activity_courses = get_course_activity()
        # print(highest_activity_courses)
        # print(lowest_activity_courses)
        self.assertEqual("Python, DSA, Databases", highest_activity_courses)
        self.assertEqual("Flask", lowest_activity_courses)
    
    def test_get_course_complexity(self):
        hardest_courses, easiest_courses = get_course_complexity()
        # print(hardest_courses)
        # print(easiest_courses)
        self.assertEqual("DSA", hardest_courses)
        self.assertEqual("Python, Flask", easiest_courses)

    def test_get_general_course_statistics(self):
        result = get_general_course_statistics()
        # print(result)
        expected_result = {'Most popular': 'Python, DSA, Databases', 
                           'Least popular': 'Flask', 
                           'Highest activity': 'Python, DSA, Databases', 
                           'Lowest activity': 'Flask', 
                           'Hardest course': 'DSA', 
                           'Easiest course': 'Python, Flask'}
        self.assertEqual(expected_result, result)
    
    def test_top_learners(self):
        res = get_course_top_learners("Python")
        # print(res)
        self.assertEqual("Python\nid\tpoints\tcompleted\n10000\t10\t1.7%\n10001\t2\t0.3%", res)
        # add test that they sorted correctly?

if __name__ == '__main__':
    unittest.main()