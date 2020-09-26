import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir)))



from model.input_model_comparator import Input_model_comparator


class Input_output_handler:
 
    def input_handler(self, input_list):
        
        list1=[]
        
        #entry1
        try:
            each= int(input_list[0])
            list1.append(each)
        except ValueError:
            return "You should have entered number only"
        
        #entry2
        try:
            each= input_list[1].lower().strip()
            if each=='single':
                list1.append(int(0))
            elif each=='married':
                list1.append(int(1))
            else:
                raise Exception
        
        except Exception:
            return "Enter a valid marital status"
        
        #entry3
        try:
            each=input_list[2].lower().strip()
            if each == "unknown" or each=="primary":
                list1.append(int(0))
            elif each =="seondary":
                list1.append(int(1))
            elif each=="tertiary":
                list1.append(int(2))
            else:
                raise Exception
        except Exception:
            return "Enter a valid educational status"   
      
        #entry4
        try:
            each=input_list[3].lower().strip()
            if each=='yes':
                list1.append(int(0))
            elif each=='no':
                list1.append(int(1))
            else:
                raise Exception
        except Exception:
            return "Enter a valid input"      
        
        #entry5
        try:
            each= int(input_list[4])
            list1.append(each)
        except ValueError:
            return "You should have entered number only"   
            
            
        #entry6
        try:
            each=input_list[5].lower().strip()
            if each=='yes':
                list1.append(int(0))
            elif each=='no':
                list1.append(int(1))
            else:
                raise Exception
        except Exception:
            return "Enter a valid input"        
    
        
        #entry7
        try:
            each=input_list[6].lower().strip()
            if each=='yes':
                list1.append(int(0))
            elif each=='no':
                list1.append(int(1))
            else:
                raise Exception
        except Exception:
            return "Enter a valid input"        
    
        
        #entry8
        try:
            each= int(input_list[7])
            list1.append(each)
        except ValueError:
            return "You should have entered number only" 
    
    
    
        #entry9
        try:
            each= int(input_list[8])
            list1.append(each)
        except ValueError:
            return "You should have entered number only"
    
    
    
        #entry10
        try:
            each= int(input_list[9])
            list1.append(each)
        except ValueError:
            return "You should have entered number only" 
    
    
        #entry11
        try:
            each= int(input_list[10])
            list1.append(each)
        except ValueError:
            return "You should have entered number only"
        
        return self.control_model_interface(list1)
    
    

        
    
    def control_model_interface(self, list1):
        
        interface = Input_model_comparator()
        output=interface.model_checker(list1)
        return output
    
    
    
    
