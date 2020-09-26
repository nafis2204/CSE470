import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir)))



from control.input_output_handler import Input_output_handler

class Input_output_handler_Test(unittest.TestCase):
    
    control = Input_output_handler()
    
    def test_input_handler(self):
        
        check_string = self.control.input_handler([25,'lol','','','',''])
        self.assertTrue(check_string=='Enter a valid marital status')
    
    def test_control_model_interface(self):
        
        check_output=self.control.control_model_interface([0,1,2,0,26,0,0,35,3,5,3])
        self.assertTrue(check_output==0 or check_output==1)

if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()