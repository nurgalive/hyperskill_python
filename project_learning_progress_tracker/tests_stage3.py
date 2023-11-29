from stage_3 import (
    Student,
    Course,
    add_points,
    print_students_list,
    is_id_exists,
    find
)
import unittest

class TestAddPoints(unittest.TestCase):
    def setUp(self):
        #print("SET UP")
        student = "Joe Does ato@pro.net"
        stud_obj = Student(student)
        #print(stud_obj)
        # print_students_list()
    
    def tearDown(self) -> None:
        #print("TEAR DOWN!")
        Student.all_students.clear()
        Course.all_courses.clear()

    def test_correct_points(self):
        # adding points to the not existing student
        points = "10001 1 2 3 4"
        added, message = add_points(points)
        #print(added, message)
        #print(Course.all_courses)
        self.assertEqual(added, False)
        self.assertEqual(message, "No student is found for id=10001")


        # add point to the not existing stundent course
        points = "10000 1 2 3 4"
        added, message = add_points(points)
        #print(added, message)
        #print(Course.all_courses)
        self.assertEqual(added, True)
        self.assertEqual(message, "Points updated")
        
        # adding points to the existing student course
        points = "10000 4 3 2 1"
        added, message = add_points(points)
        self.assertEqual(message, "Points updated")
        self.assertEqual(added, True)
        #print(Course.all_courses)
    
    def test_is_id_exists(self):
        # id does not exists
        res = is_id_exists("10001")
        self.assertEqual(res, False)

        res = is_id_exists("10000")
        self.assertEqual(res, True)

    def test_find(self):
        # student_course not found
        res = find("10000")
        # print(res)
        self.assertEqual(res, "No student is found for id=10000")

        add_points("10000 1 2 3 4")
        res = find("10000")
        # print(res)
        self.assertEqual(res, "id points: Python=1; DSA=2; Databases=3; Flask=4")




        
    # before executiong each function SetUp method is executed
    # after every function TearDown executed. Tested with print
    # def test_is_id_exists(self):
    #     self.assertEqual(is_id_exists(10000), True)
    #     print("Tested test_is_id_exists")


if __name__ == '__main__':
    unittest.main()