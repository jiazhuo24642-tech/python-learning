import unittest
from student import Student


class TestStudent(unittest.TestCase):

    def test_grade_a(self):
        s1 = Student("张三", 80)
        s2 = Student("李四", 100)

        self.assertEqual(s1.get_grade(), "A")
        self.assertEqual(s2.get_grade(), "A")

    def test_grade_b(self):
        s1 = Student("张三", 60)
        s2 = Student("李四", 79)

        self.assertEqual(s1.get_grade(), "B")
        self.assertEqual(s2.get_grade(), "B")

    def test_grade_c(self):
        s1 = Student("张三", 0)
        s2 = Student("李四", 59)

        self.assertEqual(s1.get_grade(), "C")
        self.assertEqual(s2.get_grade(), "C")

    def test_invalid_score(self):
        s1 = Student("张三", -1)
        s2 = Student("李四", 101)

        with self.assertRaises(ValueError):
            s1.get_grade()

        with self.assertRaises(ValueError):
            s2.get_grade()


if __name__ == "__main__":
    unittest.main()