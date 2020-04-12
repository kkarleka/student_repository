# -*- coding: utf-8 -*-
"""
@Kaustubh

This assignment create a data repository of courses, students, and instructors. 
The system will be used to help students track their required courses, 
the courses they have successfully completed, their grades,  GPA, etc. 
 The system will also be used by faculty advisors to help students to create study plans

"""
from collections import defaultdict
from prettytable import PrettyTable
import os
from typing import Tuple, DefaultDict, Dict, Iterator

class Student:
    """Provides information about each student """

    def __init__(self , cwid, name , major)-> None:
        """ Function to initialize the values """
        self.cwid:int = cwid
        self.name:str = name
        self.major:str = major
        self.stud_detail:Dict[str, str] = defaultdict(str)

    def add_grade(self, course, grade):
        """Add grades for each of the course """

        self.stud_detail[course] = grade

    def pretty_table_stud(self):
        """ Tabular information about student"""
        return [self.cwid, self.name, sorted(self.stud_detail.keys())]


class Instructor:
    """Provides information about each instructor """

    def __init__(self, cwid, name, department):
        """ Function to initialize the values """

        self.cwid:int = cwid
        self.name:str= name
        self.department:str = department
        self.courses:DefaultDict[str, int]= defaultdict(int)

    def add_student_count(self,course:str):
        """Add count of no of students instructor teaches """
        self.courses[course] += 1

    def pretty_table_inst(self)-> None:
         """ Tabular information about Instructor"""

         return [self.cwid,self.name, self.department], self.courses

    
class University:
    """ It holds all of  the students, instructors and grades for a single University """
    def __init__(self,directory)-> None:
        self.directory:str = directory
        self.stud_data:Dict[str, Dict[str, str]] = dict()
        self.inst_data:Dict[str, Dict[str, int]] = dict()
        self.analyze_file() 

    def analyze_file(self)-> None:
        """ This method populates the summarized data. """   ### Used this function from HW08 as well
        dir:str = os.path.isdir(self.directory)
        if not dir:
            raise FileNotFoundError("Path doesnt exists for file!!")
        
        try:
            f:str = os.listdir(self.directory)
        except FileNotFoundError:
             raise FileNotFoundError("Requested file cant be opened!")
        
        if 'students.txt' in f:
            path = os.path.join(self.directory, 'students.txt')
            for cwid, name, major in self.file_reader(path, 3 ,"\t", False):
                self.stud_data[cwid] = Student(cwid, name, major)
        if 'instructors.txt' in f:
            path = os.path.join(self.directory, 'instructors.txt')
            for cwid, name, department in self.file_reader(path, 3 ,"\t", False):
                self.inst_data[cwid] = Instructor(cwid, name, department)

        if 'grades.txt' in f:
            path = os.path.join(self.directory, 'grades.txt')
            for stud_cwid, course, grade,inst_cwid in self.file_reader(path, 4 ,"\t", False):
                if stud_cwid in self.stud_data.keys():
                    self.stud_data[stud_cwid].add_grade(course,grade)
                if inst_cwid in self.inst_data.keys():
                    self.inst_data[inst_cwid].add_student_count(course)

    def file_reader(self,path: str,num_fields:int,sep:str,header:bool)->Iterator[Tuple[str]]:

        """Write a generator function file_reader() to read field-separated text files 
            yield a tuple with all of the values from a single line in the file on each call to next()"""
        try:
            f1:str = open(path,'r')
        except FileNotFoundError:
            raise FileNotFoundError("Could not find the file!")
        else:
            with f1:
                line_num:int = 0
                if header and len(next(f1).split(sep)) != num_fields:
                    f1.seek(0)
                    raise ValueError(f"{path} has {len(f1.readline().split(sep))} fields on line 0 but expected {num_fields}")
                if header:
                    line_num +=1
                for line in f1:
                    line = line.strip().split(sep)
                    line_num +=1
                    if len(line)!= num_fields:
                        raise ValueError(f"{path} has {len(line)} fields on line {line_num} but expected {num_fields}")
                    yield tuple(line)

    

    def pretty_table_student(self)-> Iterator[Tuple[str]]:
        """ Summary table of all of the students with their CWID, name,
         and a sorted list of the courses they've taken"""

        stud_list:Iterator[Tuple[str]] = []

        pt = PrettyTable(field_names = ['CWID','Name','Courses'])
        print(f"Summary of Students")
        for stud in self.stud_data.values():
            pt.add_row(stud.pretty_table_stud())
            stud_list.append(stud.pretty_table_stud())
        print(pt)
        return stud_list

    def pretty_table_instructor(self)-> Iterator[Tuple[str]]:
        """Summary table of each of the instructors who taught at least one course with their
         CWID, name, department, the course they've taught, and the number of students in each class """

        inst_list:Iterator[Tuple[str]] = []

        pt = PrettyTable(field_names = ['CWID','Name','Department','Courses','Student'])
        print(f"Summary of Instructor")
        for inst in self.inst_data.values():
            inst_information, courses = inst.pretty_table_inst()
            for course, students in courses.items():
                inst_information.extend([course,students])
                pt.add_row(inst_information)
                inst_list.append(inst_information)
                inst_information = inst_information[0:3]

        print(pt)

        return inst_list
        

def main():
    try:
        univ = University(r"C:\Users\kaust\Documents\SSW-810") #Change file path
        univ.pretty_table_student()
        univ.pretty_table_instructor()
    except Exception as e:
        raise e

if __name__ == "__main__":
    main()


        
                



        





