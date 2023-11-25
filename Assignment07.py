# ------------------------------------------------------------------------------------------ #
# Title: Assignment07 Classes and Objects
# Desc: This assignment demonstrates how to create and use classes to manage data and
# with structured error handling
# Change Log: (Who, When, What)
#   Nelly,22/11/2023,Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str = ""  # Variable with the choice made by the user.


# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    Nelly,22.11.2023,Created Class
    """
    @staticmethod
    def read_data_from_file(file_name: str):
        """ Reads data from a JSON file and loads it into a list of Student objects

        ChangeLog: (Who, When, What)
        Nelly,22.11.2023,Created function

        :param file_name: string data with name of file to read from

        :return: list of Student objects
        """
        students = []
        try:
            with open(file_name, "r") as file:
                student_dicts = json.load(file)
                for student_dict in student_dicts:
                    students.append(Student(student_dict["FirstName"],
                                            student_dict["LastName"],
                                            student_dict["CourseName"]))
        except FileNotFoundError:
            print("File not found, starting with an empty list of students.")
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)
        return students

    @staticmethod
    def write_data_to_file(file_name: str, student_objs: list):
        """ Writes a list of Student objects to a JSON file

        ChangeLog: (Who, When, What)
        Nelly,23.11.2023,Created function

        :param file_name: string data with name of file to write to
        :param student_objs: list of Student objects to be writen to the file

        :return: None
        """

        try:
            with open(file_name, "w") as file:
                student_dicts = []
                for student in student_objs:
                    student_dicts.append({
                        "FirstName": student.first_name,
                        "LastName": student.last_name,
                        "CourseName": student.course_name
                    })
                json.dump(student_dicts, file)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Check that the file is not open by another program."
            IO.output_error_messages(message=message,error=e)

class Person:
    """
    A class representing person data.

    Properties:
    - first_name (str): The student's first name.
    - last_name (str): The student's last name.

    ChangeLog:
    - Nelly,22.11.2023,Created Class.
    """

    def __init__(self, first_name: str = '', last_name: str = ''):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self._first_name.title()  # formatting code

    @first_name.setter
    def first_name(self, value: str):
        if value.isalpha() or value == "":  # is character or empty string
            self._first_name = value
        else:
            raise ValueError("The first name should not contain numbers.")

    @property
    def last_name(self):
        return self._last_name.title()  # formatting code

    @last_name.setter
    def last_name(self, value: str):
        if value.isalpha() or value == "":  # is character or empty string
            self._last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

    def __str__(self):
        return f'{self.first_name},{self.last_name}'

class Student(Person):
    """
    A class representing student data.

    Properties:
    - first_name (str): The student's first name.
    - last_name (str): The student's last name.
    - course_name (str): The course name of the student.

    ChangeLog:
    - Nelly,22.11.2023,Created Class
    """
    def __init__(self, first_name: str, last_name: str, course_name: str):
        super().__init__(first_name=first_name, last_name=last_name)
        self.course_name = course_name

    @property
    def course_name(self):
        return self._course_name

    @course_name.setter
    def course_name(self, value: str):
        if isinstance(value, str):  # Assuming course name can be any string
            self._course_name = value
        else:
            raise ValueError("Course name must be a string.")

    def __str__(self):
        return f'{self.first_name},{self.last_name},{self.course_name}'

# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    Nelly,22.11.2023,Created Class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ Displays a custom error messages to the user

        ChangeLog: (Who, When, What)
        Nelly,22.11.2023,Created function

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ Displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        Nelly,22.11.2023,Created function


        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        Nelly,22.11.2023,Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_student_and_course_names(student_objs: list):
        """ Displays the student and course names to the user

        ChangeLog: (Who, When, What)
        Nelly,22.11.2023,Created function

        :param student_objs: list of Student objects to be displayed

        :return: None
        """

        print("-" * 50)
        for student in student_objs:
            print(f'Student {student.first_name} {student.last_name} is enrolled in {student.course_name}')
        print("-" * 50)

    @staticmethod
    def input_student_data():
        """ Gets student data from the user and returns a Student object

        ChangeLog: (Who, When, What)
        Nelly,22.11.2023,Created function
        :param None
        :return: Student object
        """

        try:
            student_first_name = input("Enter the student's first name: ").strip()
            student_last_name = input("Enter the student's last name: ").strip()
            course_name = input("Please enter the name of the course: ").strip()
            student = Student(student_first_name, student_last_name, course_name)
            print()
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
            return student
        except ValueError as e:
            IO.output_error_messages(message="One of the values was the correct type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)


# _____________________________________Start of main body_______________________________________________________


# When the program starts, read the file data into a list, students are now a list of Student Object.
# Extract the data from the file.
students = FileProcessor.read_data_from_file(file_name=FILE_NAME)   # students are now a list of Student Object


# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        student = IO.input_student_data()
        if student is not None:
            students.append(student)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_and_course_names(students)
        continue

    # Save the data to a JSON file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_objs=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("You can only choose option 1, 2, or 3")

print("End of the Program")
