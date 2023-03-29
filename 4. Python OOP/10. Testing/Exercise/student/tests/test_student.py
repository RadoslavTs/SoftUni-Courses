from project.student import Student

import unittest


class TestTheStudent(unittest.TestCase):
    def setUp(self) -> None:
        self.my_student = Student('Rado', {'Maths': ['my note']})

    def test_constructor(self):
        self.assertEqual(self.my_student.name, 'Rado')
        self.assertEqual(self.my_student.courses, {'Maths': ['my note']})

    def test_constructor_empty_notes(self):
        student = Student('Miro')
        self.assertEqual(student.courses, {})

    def test_ernrollment_existing(self):
        self.assertEqual(self.my_student.enroll('Maths', ['cool', 'nice'], ''), "Course already added. Notes have been updated.")
        self.assertEqual(self.my_student.courses, {'Maths': ['my note', 'cool', 'nice']})

    def test_enrollment_new_empty_string(self):
        self.assertEqual(self.my_student.enroll('Bilogy', ['cool'], ''),
                         "Course and course notes have been added.")
        self.assertEqual(self.my_student.courses, {'Maths': ['my note'], 'Bilogy': ['cool']})
        
    def test_enrollment_new_y_string(self):
        self.assertEqual(self.my_student.enroll('Bilogy', ['cool'], 'Y'),
                         "Course and course notes have been added.")
        self.assertEqual(self.my_student.courses, {'Maths': ['my note'], 'Bilogy': ['cool']})

    def test_enroll_add(self):
        self.assertEqual(self.my_student.enroll('Bilogy', ['cool'], 'p'),
                         "Course has been added.")
        self.assertEqual(self.my_student.courses, {'Maths': ['my note'], 'Bilogy': []})

    def test_add_notes_fail(self):
        with self.assertRaises(Exception) as error:
            self.my_student.add_notes('Biology', ['just one'])
        self.assertEqual(str(error.exception), "Cannot add notes. Course not found.")

    def test_add_note(self):
        self.assertEqual(self.my_student.add_notes('Maths', 'hello'), "Notes have been updated")
        self.assertEqual(self.my_student.courses, {'Maths': ['my note', 'hello']})

    def test_leave_course_fail(self):
        with self.assertRaises(Exception) as error:
            self.my_student.leave_course('Biology')
        self.assertEqual(str(error.exception), "Cannot remove course. Course not found.")

    def test_leave_course(self):
        self.assertEqual(self.my_student.leave_course('Maths'), "Course has been removed")
        self.assertEqual(self.my_student.courses, {})