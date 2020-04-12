""" 

@Kaustubh

Test cases to verify Major, Student summary and Instructor summary


"""
import unittest
from HW11_Kaustubh_Karlekar import Student, Instructor,University


class TestUniversity(unittest.TestCase):
    """Test cases to verify major,student and instructor summary """

    def test_major_summary(self):
        """ Verify required courses and electives of each major"""

        test1 = University(r"C:\Users\kaust\Documents\SSW-810\HW11") #change file path
        actual_inst_summary = list(test1.pretty_table_major())
        expected = [['SFEN',['SSW 540','SSW 810','SSW 555'],['CS 501','CS 546']],
                    ['CS',['CS 570','CS 546'],['SSW 810','SSW 565']]]
        self.assertEqual(actual_inst_summary,expected)
    
    def test_student_summary(self):
        """ Verify required courses and electives of each major"""

        test1 = University(r"C:\Users\kaust\Documents\SSW-810\HW11") #change file path
        actual_inst_summary = list(test1.pretty_table_student())
        expected = [['10103', 'Jobs, S', 'SFEN', ['CS 501', 'SSW 810'], ['SSW 540', 'SSW 555'], [], 3.38],
                    ['10115', 'Bezos, J', 'SFEN', ['SSW 810'], ['SSW 540', 'SSW 555'], ['CS 501', 'CS 546'], 4.0],
                    ['10183', 'Musk, E', 'SFEN', ['SSW 555', 'SSW 810'], ['SSW 540'], ['CS 501', 'CS 546'], 4.0], 
                    ['11714', 'Gates, B', 'CS', ['CS 546', 'CS 570', 'SSW 810'], [], [], 3.5]]
        self.assertEqual(actual_inst_summary,expected)

    


    def test_intructor_summary(self):
        """ Verify summary table of all of the instructors"""

        test1 = University(r"C:\Users\kaust\Documents\SSW-810\HW11") #change file path
        actual_inst_summary = list(test1.pretty_table_instructor())
        expected = [['98764', 'Cohen, R', 'SFEN', 'CS 546', 1],
                    ['98763', 'Rowland, J', 'SFEN', 'SSW 810', 4],
                    ['98763', 'Rowland, J', 'SFEN', 'SSW 555', 1],
                    ['98762', 'Hawking, S', 'CS', 'CS 501', 1], 
                    ['98762', 'Hawking, S', 'CS', 'CS 546', 1], 
                    ['98762', 'Hawking, S', 'CS', 'CS 570', 1]]
        self.assertEqual(actual_inst_summary,expected)

    
    def test_intructor_db_summary(self):
        """ Verify summary table of all of the instructors"""

        test1 = University(r"C:\Users\kaust\Documents\SSW-810\HW11") #change file path
        actual_inst_summary = list(test1.instructor_table_db(r"C:\sqlite\StudentRepo.db"))
        expected = [['Bezos, J', '10115', 'CS 546', 'F', 'Hawking, S'], 
                    ['Bezos, J', '10115', 'SSW 810', 'A', 'Rowland, J'],
                    ['Gates, B', '11714', 'CS 546', 'A', 'Cohen, R'],
                    ['Gates, B', '11714', 'CS 570', 'A-', 'Hawking, S'],
                    ['Gates, B', '11714', 'SSW 810', 'B-', 'Rowland, J'], 
                    ['Jobs, S', '10103', 'CS 501', 'B', 'Hawking, S'], 
                    ['Jobs, S', '10103', 'SSW 810', 'A-', 'Rowland, J'], 
                    ['Musk, E', '10183', 'SSW 555', 'A', 'Rowland, J'], 
                    ['Musk, E', '10183', 'SSW 810', 'A', 'Rowland, J']] 
        self.assertEqual(actual_inst_summary,expected)

       


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)