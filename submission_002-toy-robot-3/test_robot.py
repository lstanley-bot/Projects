import unittest
from unittest.mock import patch
import robot
from robot import (do_forward, do_back, do_sprint,
do_left_turn, do_right_turn, do_help, robot_history, robot_replay)
import sys
from io import StringIO
unittest.util._MAX_LENGTH = 2000

class test_robot(unittest.TestCase):
    
    def test_help(self):
        self.assertEqual(do_help(), (True, "I can understand these commands:\nOFF  - Shut down robot\nHELP - provide information about commands\nFORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'\nBACK - move backward by specified number of steps, e.g. 'BACK 10'\nRIGHT - turn right by 90 degrees\nLEFT - turn left by 90 degrees\nSPRINT - sprint forward according to a formula\n"))


    def test_forward(self):
        self.assertEqual(do_forward("ROB", 5), (True, ' > ROB moved forward by 5 steps.'), (True, 'ROB: Sorry, I cannot go outside my safe zone.'))


    def test_back(self):
        self.assertEqual(do_back("ROB", 5), (True, ' > ROB moved back by 5 steps.'), (True, 'ROB: Sorry, I cannot go outside my safe zone.'))


    def test_left(self): 
        self.assertEqual(do_left_turn("ROB"), (True, ' > ROB turned left.'))


    def test_right(self):
        self.assertEqual(do_right_turn("ROB"), (True, ' > ROB turned right.'))


    def test_sprint(self):
        self.assertEqual(do_sprint("ROB",5), (do_sprint('ROB', 5 - 1)))


    def test_history(self):
        self.assertEqual(robot_history("forward 10"), ("forward 10"))


    @patch("sys.stdin", StringIO("ROB\nforward 10\nright\nforward 10\nreplay\noff"))
    def test_replay(self):
        sys.stdout = StringIO()

        robot.robot_start()

        self.assertEqual(sys.stdout.getvalue(), '''What do you want to name your robot? ROB: Hello kiddo!
ROB: What must I do next?  > ROB moved forward by 10 steps.
 > ROB now at position (0,10).
ROB: What must I do next?  > ROB turned right.
 > ROB now at position (0,10).
ROB: What must I do next?  > ROB moved forward by 10 steps.
 > ROB now at position (10,10).
ROB: What must I do next?  > ROB moved forward by 10 steps.
 > ROB now at position (20,10).
 > ROB turned right.
 > ROB now at position (20,10).
 > ROB moved forward by 10 steps.
 > ROB now at position (20,0).
 > ROB replayed 3 commands.
 > ROB now at position (20,0).
ROB: What must I do next? ROB: Shutting down..
''')


    @patch("sys.stdin", StringIO("ROB\nforward 10\nright\nforward 10\nreplay 2\noff"))
    def test_replay_range(self):
        sys.stdout = StringIO()

        robot.robot_start()

        self.assertEqual(sys.stdout.getvalue(), '''What do you want to name your robot? ROB: Hello kiddo!
ROB: What must I do next?  > ROB moved forward by 10 steps.
 > ROB now at position (0,10).
ROB: What must I do next?  > ROB turned right.
 > ROB now at position (0,10).
ROB: What must I do next?  > ROB moved forward by 10 steps.
 > ROB now at position (10,10).
ROB: What must I do next?  > ROB turned right.
 > ROB now at position (10,10).
 > ROB moved forward by 10 steps.
 > ROB now at position (10,0).
 > ROB replayed 2 commands.
 > ROB now at position (10,0).
ROB: What must I do next? ROB: Shutting down..
''')


    @patch("sys.stdin", StringIO("ROB\nforward 10\nright\nforward 10\nback 20\nreplay 3-1\noff"))
    def test_replay_range_full(self):
        sys.stdout = StringIO()

        robot.robot_start()

        self.assertEqual(sys.stdout.getvalue(), '''What do you want to name your robot? ROB: Hello kiddo!
ROB: What must I do next?  > ROB moved forward by 10 steps.
 > ROB now at position (0,10).
ROB: What must I do next?  > ROB turned right.
 > ROB now at position (0,10).
ROB: What must I do next?  > ROB moved forward by 10 steps.
 > ROB now at position (10,10).
ROB: What must I do next?  > ROB moved back by 20 steps.
 > ROB now at position (-10,10).
ROB: What must I do next?  > ROB turned right.
 > ROB now at position (-10,10).
 > ROB moved forward by 10 steps.
 > ROB now at position (-10,0).
 > ROB replayed 2 commands.
 > ROB now at position (-10,0).
ROB: What must I do next? ROB: Shutting down..
''')


    @patch("sys.stdin", StringIO("ROB\nforward 10\nright\nforward 10\nreplay silent\noff"))
    def test_replay_silent(self):
        sys.stdout = StringIO()

        robot.robot_start()

        self.assertEqual(sys.stdout.getvalue(), '''What do you want to name your robot? ROB: Hello kiddo!
ROB: What must I do next?  > ROB moved forward by 10 steps.
 > ROB now at position (0,10).
ROB: What must I do next?  > ROB turned right.
 > ROB now at position (0,10).
ROB: What must I do next?  > ROB moved forward by 10 steps.
 > ROB now at position (10,10).
ROB: What must I do next?  > ROB replayed 3 commands silently.
 > ROB now at position (20,0).
ROB: What must I do next? ROB: Shutting down..
''')


    @patch("sys.stdin", StringIO("ROB\nforward 10\nright\nforward 10\nreplay silent 2\noff"))
    def test_replay_silent_range(self):
        sys.stdout = StringIO()

        robot.robot_start()

        self.assertEqual(sys.stdout.getvalue(),'''What do you want to name your robot? ROB: Hello kiddo!
ROB: What must I do next?  > ROB moved forward by 10 steps.
 > ROB now at position (0,10).
ROB: What must I do next?  > ROB turned right.
 > ROB now at position (0,10).
ROB: What must I do next?  > ROB moved forward by 10 steps.
 > ROB now at position (10,10).
ROB: What must I do next?  > ROB replayed 2 commands silently.
 > ROB now at position (10,0).
ROB: What must I do next? ROB: Shutting down..
''')


    @patch("sys.stdin", StringIO("ROB\nforward 10\nright\nforward 10\nback 20\nreplay silent 3-1\noff"))
    def test_replay_silent_full(self):
        sys.stdout = StringIO()

        robot.robot_start()

        self.assertEqual(sys.stdout.getvalue(),'''What do you want to name your robot? ROB: Hello kiddo!
ROB: What must I do next?  > ROB moved forward by 10 steps.
 > ROB now at position (0,10).
ROB: What must I do next?  > ROB turned right.
 > ROB now at position (0,10).
ROB: What must I do next?  > ROB moved forward by 10 steps.
 > ROB now at position (10,10).
ROB: What must I do next?  > ROB moved back by 20 steps.
 > ROB now at position (-10,10).
ROB: What must I do next?  > ROB replayed 2 commands silently.
 > ROB now at position (-10,0).
ROB: What must I do next? ROB: Shutting down..
''')


    @patch("sys.stdin", StringIO("ROB\nforward 10\nright\nforward 10\nreplay reversed\noff"))
    def test_replay_reversed(self):
        sys.stdout = StringIO()

        robot.robot_start()

        self.assertEqual(sys.stdout.getvalue(), '''What do you want to name your robot? ROB: Hello kiddo!
ROB: What must I do next?  > ROB moved forward by 10 steps.
 > ROB now at position (0,10).
ROB: What must I do next?  > ROB turned right.
 > ROB now at position (0,10).
ROB: What must I do next?  > ROB moved forward by 10 steps.
 > ROB now at position (10,10).
ROB: What must I do next?  > ROB moved forward by 10 steps.
 > ROB now at position (20,10).
 > ROB turned right.
 > ROB now at position (20,10).
 > ROB moved forward by 10 steps.
 > ROB now at position (20,0).
 > ROB replayed 3 commands in reverse.
 > ROB now at position (20,0).
ROB: What must I do next? ROB: Shutting down..
''')


    @patch("sys.stdin", StringIO("ROB\nforward 10\nright\nforward 10\nreplay reversed 2\noff"))
    def test_replay_reversed_range(self):
        sys.stdout = StringIO()

        robot.robot_start()

        self.assertEqual(sys.stdout.getvalue(),'''What do you want to name your robot? ROB: Hello kiddo!
ROB: What must I do next?  > ROB moved forward by 10 steps.
 > ROB now at position (0,10).
ROB: What must I do next?  > ROB turned right.
 > ROB now at position (0,10).
ROB: What must I do next?  > ROB moved forward by 10 steps.
 > ROB now at position (10,10).
ROB: What must I do next?  > ROB turned right.
 > ROB now at position (10,10).
 > ROB moved forward by 10 steps.
 > ROB now at position (10,0).
 > ROB replayed 2 commands in reverse.
 > ROB now at position (10,0).
ROB: What must I do next? ROB: Shutting down..
''')


    @patch("sys.stdin", StringIO("ROB\nforward 10\nright\nforward 10\nback 20\nreplay reversed 3-1\noff"))
    def test_replay_reversed_full(self):
        sys.stdout = StringIO()

        robot.robot_start()

        self.assertEqual(sys.stdout.getvalue(), '''What do you want to name your robot? ROB: Hello kiddo!
ROB: What must I do next?  > ROB moved forward by 10 steps.
 > ROB now at position (0,10).
ROB: What must I do next?  > ROB turned right.
 > ROB now at position (0,10).
ROB: What must I do next?  > ROB moved forward by 10 steps.
 > ROB now at position (10,10).
ROB: What must I do next?  > ROB moved back by 20 steps.
 > ROB now at position (-10,10).
ROB: What must I do next?  > ROB moved forward by 10 steps.
 > ROB now at position (0,10).
 > ROB replayed 2 commands in reverse.
 > ROB now at position (0,10).
ROB: What must I do next? ROB: Shutting down..
''')


    @patch("sys.stdin", StringIO("ROB\nforward 10\nright\nforward 10\nreplay reversed silent\noff"))
    def test_replay_reversed_silent(self):
        sys.stdout = StringIO()

        robot.robot_start()

        self.assertEqual(sys.stdout.getvalue(), '''What do you want to name your robot? ROB: Hello kiddo!
ROB: What must I do next?  > ROB moved forward by 10 steps.
 > ROB now at position (0,10).
ROB: What must I do next?  > ROB turned right.
 > ROB now at position (0,10).
ROB: What must I do next?  > ROB moved forward by 10 steps.
 > ROB now at position (10,10).
ROB: What must I do next?  > ROB replayed 3 commands in reverse silently.
 > ROB now at position (20,0).
ROB: What must I do next? ROB: Shutting down..
''')


    @patch("sys.stdin", StringIO("ROB\nforward 10\nright\nforward 10\nreplay reversed silent 2\noff"))
    def test_replay_reversed_silent_range(self):
        sys.stdout = StringIO()

        robot.robot_start()

        self.assertEqual(sys.stdout.getvalue(), '''What do you want to name your robot? ROB: Hello kiddo!
ROB: What must I do next?  > ROB moved forward by 10 steps.
 > ROB now at position (0,10).
ROB: What must I do next?  > ROB turned right.
 > ROB now at position (0,10).
ROB: What must I do next?  > ROB moved forward by 10 steps.
 > ROB now at position (10,10).
ROB: What must I do next?  > ROB replayed 2 commands in reverse silently.
 > ROB now at position (10,0).
ROB: What must I do next? ROB: Shutting down..
''')


    @patch("sys.stdin", StringIO("ROB\nforward 10\nright\nforward 10\nback 20\nreplay reversed silent 3-1\noff"))
    def test_replay_reversed_silent_full(self):
        sys.stdout = StringIO()

        robot.robot_start()

        self.assertEqual(sys.stdout.getvalue(), '''What do you want to name your robot? ROB: Hello kiddo!
ROB: What must I do next?  > ROB moved forward by 10 steps.
 > ROB now at position (0,10).
ROB: What must I do next?  > ROB turned right.
 > ROB now at position (0,10).
ROB: What must I do next?  > ROB moved forward by 10 steps.
 > ROB now at position (10,10).
ROB: What must I do next?  > ROB moved back by 20 steps.
 > ROB now at position (-10,10).
ROB: What must I do next?  > ROB replayed 2 commands in reverse silently.
 > ROB now at position (0,10).
ROB: What must I do next? ROB: Shutting down..
''')


if __name__ == "__main__":
    unittest.main()