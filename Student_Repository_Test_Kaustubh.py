""" 

@Kaustubh

Test cases to verify Student summary and Instructor summary


"""
import unittest
from Student_Repository_Kaustubh import Student, Instructor,University


class TestUniversity(unittest.TestCase):
    """Test cases to verify student and instructor summary """

    def test_student_summary(self):
        """ Verify summary table of all of the students"""
        test = University(r"C:\Users\kaust\Documents\SSW-810") #change file path
        actual_stud_summary = list(test.pretty_table_student())
        expected = [['10103','Baldwin, C',['CS 501','SSW 564', 'SSW 567', 'SSW 687']], ['10115','Wyatt, X',['CS 545','SSW 564', 'SSW 567', 'SSW 687']],
                  ['10172','Forbes, I',['SSW 555', 'SSW 567']],['10175','Erickson, D',['SSW 564', 'SSW 567', 'SSW 687']],['10183','Chapman, O',['SSW 689']],
                  ['11399','Cordova, I',['SSW 540']],['11461','Wright, U',['SYS 611','SYS 750', 'SYS 800']],['11658','Kelly, P',['SSW 540']],
                  ['11714','Morton, A',['SYS 611','SYS 645']],['11788','Fuller, E',['SSW 540']]]
        self.assertEqual(actual_stud_summary,expected)

        with self.assertRaises(FileNotFoundError):
            list(University(r"C:\Users\kaust\Documents\SSW-810").file_reader('xyz.txt',3,'\t',True))


    def test_intructor_summary(self):
        """ Verify summary table of all of the instructors"""

        test1 = University("C:\\Users\\kaust\\Documents\\SSW-810") #change file path
        actual_inst_summary = list(test1.pretty_table_instructor())
        expected = [['98765','Einstein, A','SFEN','SSW 567',4],['98765','Einstein, A','SFEN','SSW 540',3],['98764','Feynman, R','SFEN','SSW 564',3],
                    ['98764','Feynman, R','SFEN','SSW 687',3],['98764','Feynman, R','SFEN','CS 501',1],['98764','Feynman, R','SFEN','CS 545',1],
                    ['98763','Newton, I','SFEN','SSW 555',1],['98763','Newton, I','SFEN','SSW 689',1],['98760','Darwin, C','SYEN','SYS 800',1],
                    ['98760','Darwin, C','SYEN','SYS 750',1],['98760','Darwin, C','SYEN','SYS 611',2],['98760','Darwin, C','SYEN','SYS 645',1]]
        self.assertEqual(actual_inst_summary,expected)

        with self.assertRaises(FileNotFoundError):
            list(University("C:\\Users\\kaust\\Documents\\SSW-810").file_reader('xyz.txt',3,'\t',True))

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
    
