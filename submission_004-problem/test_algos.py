import unittest
import super_algos

class test_SuperAlgos(unittest.TestCase):

    def test_min(self):

        self.assertEqual(super_algos.find_min([3,6,8,9,2,11]), 2)   
        self.assertEqual(super_algos.find_min([3,6,8,"a",2,11]), -1)
        self.assertEqual(super_algos.find_min([3,6,8,"",2,11]), -1) 

    def test_sum(self):

        self.assertEqual(super_algos.sum_all([3,6,8,9,2,11]), 39)   
        self.assertEqual(super_algos.sum_all([3,6,8,"a",2,11]), -1)
        self.assertEqual(super_algos.sum_all([3,6,8,"",2,11]), -1)  

    def test_possibleStrings(self):
        
        self.assertEqual(super_algos.find_possible_strings(["a","b"],2),["aa","ab","ba","bb"])
        self.assertEqual(super_algos.find_possible_strings(["x","y"],3),["xxx","xxy","xyx","xyy","yxx","yxy","yyx","yyy"])


if __name__ == '__main__':
    unittest.main()