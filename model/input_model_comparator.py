import numpy as np
import pickle
import os
curdir=os.path.abspath(os.path.join(os.getcwd(),os.path.pardir,'model'))


class Input_model_comparator:

    
    
    
    def model_checker(self,list1):
        
        
        
        finals=np.array(list1)
        
        listx=self.data_model_builder(finals)
        listx=np.array(listx)
        listx=listx.reshape(1,9)
        file_final_loc=os.path.join(curdir,'file_final.sav')
        loaded_model=pickle.load(open(file_final_loc, 'rb'))
        result = loaded_model.predict(listx)
        return int(result[0])
            
            
            
    def data_model_builder(self,listx):
        final_list=[]
        listx=listx.reshape(1,11)
        
        #saved_knn_model
        file_knn1_loc=os.path.join(curdir,'file_knn1.sav')
        loaded_model1=pickle.load(open(file_knn1_loc, 'rb'))
        final_list.append(loaded_model1.predict(listx)) 
        #saved model random forest
        file_rf1_loc=os.path.join(curdir,'file_rf1.sav')
        loaded_model2=pickle.load(open(file_rf1_loc, 'rb'))
        final_list.append(loaded_model2.predict(listx))
        #saved decision tree
        file_dt1_loc=os.path.join(curdir,'file_dt1.sav')
        loaded_model3=pickle.load(open(file_dt1_loc, 'rb'))
        final_list.append(loaded_model3.predict(listx))
        #saved naive bayes
        file_nb1_loc=os.path.join(curdir,'file_nb1.sav')
        loaded_model4=pickle.load(open(file_nb1_loc, 'rb'))
        final_list.append(loaded_model4.predict(listx))    
        #saved support vector machine
        file_svm1_loc=os.path.join(curdir,'file_svm1.sav')
        loaded_model5=pickle.load(open(file_svm1_loc, 'rb'))
        final_list.append(loaded_model5.predict(listx))
        #saved bagging
        file_bg1_loc=os.path.join(curdir,'file_bg1.sav')
        loaded_model6=pickle.load(open(file_bg1_loc, 'rb'))
        final_list.append(loaded_model6.predict(listx))
        #saved extra tree
        file_et1_loc=os.path.join(curdir,'file_et1.sav')
        loaded_model7=pickle.load(open(file_et1_loc, 'rb'))
        final_list.append(loaded_model7.predict(listx))
        #saved ada boost
        file_abd1_loc=os.path.join(curdir,'file_adb1.sav')
        loaded_model8=pickle.load(open(file_abd1_loc, 'rb'))
        final_list.append(loaded_model8.predict(listx))    
        #saved gradient boost
        file_gb1_loc=os.path.join(curdir,'file_gb1.sav')
        loaded_model9=pickle.load(open(file_gb1_loc, 'rb'))
        final_list.append(loaded_model9.predict(listx))
        
        return final_list
