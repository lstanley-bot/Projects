import unittest
from unittest.mock import patch
from io import StringIO
import sys
import mastermind

def get_answer_input():
    return input("Input 4 digit code: ")

class TestFunctions(unittest.TestCase):

    @patch("sys.stdin", StringIO("1234\n"))
    def test_compare(self):
        self.assertEqual(mastermind.get_answer_input(), "1234")

    def test_create_code(self):
        for code in range(100):
            code = mastermind.create_code()

        self.assertNotIn(0, code)
        self.assertNotIn(9, code)
        self.assertEqual(len(code), 4)

    def test_check_correctness(self):

        sys.stdout = StringIO()
        self.assertEqual(mastermind.check_correctness(4, (4, 0)), True)
        self.assertEqual(sys.stdout.getvalue(), "Congratulations! You are a codebreaker!\n")

        sys.stdout = StringIO()
        self.assertEqual(mastermind.check_correctness(3, (3, 0)), False)
        self.assertEqual(sys.stdout.getvalue(), "Turns left: 9\n")

    @patch("sys.stdin", StringIO("5321\n3125\n4781\n5681\n"))
    def test_take_turn(self):
        code = [5,6,8,1]
        test_code = [(2,0),(0,2),(2,0),(4,0)]

        for i in range(4):
            correct = mastermind.take_turn(code)
            self.assertEqual(str(correct), str(test_code[i]))




if __name__ == "__main__":
    unittest.main()
