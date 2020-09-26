import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir)))
from model.input_model_comparator import Input_model_comparator



class Input_model_comparatorTest(unittest.TestCase):
    
    def test_model_checker(self):
        
        control=Input_model_comparator()
        
        output=control.model_checker([0,1,2,0,26,0,0,35,3,5,3])
        self.assertTrue(output==0 or output==1)
        
if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()

