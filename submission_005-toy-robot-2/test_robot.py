import unittest
from unittest.mock import patch
from robot import name_robot, command, off_command, forward_movements, back_movements, sprint_movements, left_movements, right_movements, get_help
import sys
from io import StringIO

class test_robot(unittest.TestCase):

    def test_off(self):
        self.assertEqual(off_command("ROB", "off"), "ROB: Shutting down..")
    
    def test_help(self):
        self.assertEqual(get_help(), "I can understand these commands:\nOFF  - Shut down robot\nHELP - provide information about commands\n")

    def test_move(self):
        self.assertEqual(forward_movements("ROB","forward 5",0,0,"starting point"),(0,5))
        

    def test_back(self):
        self.assertEqual(back_movements("ROB","back 5",0,0,"starting point"),(0,-5))
   
          
    def test_left(self): 
        self.assertEqual(left_movements("ROB","left", 0,8),(0,8))


    def test_right(self):
        self.assertEqual(right_movements("ROB","right",0,8),(0,8))


    def test_sprint(self):
        self.assertEqual(sprint_movements("ROB","sprint 5",0,0,"starting point"),(0,15))



if __name__ == '__main__':
    unittest.main()