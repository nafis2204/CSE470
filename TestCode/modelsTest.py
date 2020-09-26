import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir)))
from model.models import Models




class ModelsTest(unittest.TestCase):
    
    classifier=Models(test=True)
    accuracy=classifier.model_builder()
    
    def test_model_builder(self):

        
        self.assertTrue(self.accuracy>75)
    
if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()