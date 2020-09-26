import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix 
from sklearn.preprocessing import StandardScaler
import pickle
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

class Models:
    def __init__(self,test):
        if test==True:
            self.test=True
        #preprocessing train set for primary models
        dataset=pd.read_csv('E:/Bracu/semester 8/CSE 470 Software Engineering/Peradayok bank/model/bank.csv')
        self.df=dataset
        self.accuracy=0
 
    def model_builder(self):


        self.df=self.df.drop(["duration","job","contact","month","poutcome"],axis=1)
        self.df.head()
        self.df.columns
        self.df["marital"] = [0 if each== "single" else 1 for each in self.df.marital]
        self.df["default"] = [0 if each== "no" else 1 for each in self.df.default]
        self.df["housing"] = [0 if each== "no" else 1 for each in self.df.housing]
        self.df["loan"] = [0 if each== "no" else 1 for each in self.df.loan]
        self.df["y"] = [0 if each== "no" else 1 for each in self.df.y]
        for each in self.df.education:
            if each == "unknown" or each=="primary":
                self.df["education"] = 0
            elif each =="seondary":
                self.df["education"] = 1
            else:
                self.df["education"]=2
        
        
        # Splitting the dataset into the Training set and Test set
        X = self.df.iloc[:, 0:11].values
        y = self.df.iloc[:,11].values
        
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)
        
        
        # Feature Scaling
        sc = StandardScaler()
        X=sc.fit_transform(X)
        X_train = sc.fit_transform(X_train)
        X_test = sc.transform(X_test)
        
        
        newdata=[]
        
        #using 9 ML model to create a secondary dataset
        
        
        knn = KNeighborsClassifier(n_neighbors = 10)  # n_neighbors means k
        knn.fit(X_train, y_train)
        y_pred_knn = knn.predict(X_test)
        file_knn1 = 'file_knn1.sav'
        if self.test!=True:
            pickle.dump(knn, open(file_knn1, 'wb'))
        
        
        
        RF = RandomForestClassifier(n_estimators=100, criterion='entropy', random_state=0)  
        RF.fit(X_train, y_train)
        y_pred_RF = RF.predict(X_test)
        file_rf1 = 'file_rf1.sav'
        if self.test!=True:
            pickle.dump(RF, open(file_rf1, 'wb'))
        
        
        
        
        
        dtclassifier= DecisionTreeClassifier(criterion='entropy')
        dtclassifier.fit(X_train,y_train)
        y_pred_DT = dtclassifier.predict(X_test)
        file_dt1 = 'file_dt1.sav'
        if self.test!=True:
            pickle.dump(dtclassifier, open(file_dt1, 'wb'))
        
        
        
        
        from sklearn.naive_bayes import GaussianNB
        nbclassifier=GaussianNB()
        nbclassifier.fit(X_train, y_train)
        nb_y_pred = nbclassifier.predict(X_test)
        file_nb1 = 'file_nb1.sav'
        if self.test!=True:
            pickle.dump(nbclassifier, open(file_nb1, 'wb'))
        
        
        
        
        svmkclassifier =SVC(kernel ='rbf',random_state=0,gamma='auto')
        svmkclassifier.fit(X_train, y_train)
        y_pred_SVMK = svmkclassifier.predict(X_test)
        file_svm1 = 'file_svm1.sav'
        if self.test!=True:
            pickle.dump(svmkclassifier, open(file_svm1, 'wb'))
        
        
        
        
        
        
        bg=BaggingClassifier(base_estimator=DecisionTreeClassifier(), n_estimators=100, random_state=15)
        bg.fit(X_train, y_train)
        y_pred_bg = bg.predict(X_test)
        file_bg1 = 'file_bg1.sav'
        if self.test!=True:
            pickle.dump(bg, open(file_bg1, 'wb'))
        
        
        
        
        
        et=ExtraTreesClassifier(n_estimators=100, max_features=4)
        et.fit(X_train, y_train)
        y_pred_et = et.predict(X_test)
        file_et1 = 'file_et1.sav'
        if self.test!=True:
            pickle.dump(et, open(file_et1, 'wb'))
        
        
        
        
        
        adb=AdaBoostClassifier(n_estimators=50, random_state=4)
        adb.fit(X_train, y_train)
        y_pred_adb = adb.predict(X_test)
        file_adb1 = 'file_adb1.sav'
        if self.test!=True:
            pickle.dump(adb, open(file_adb1, 'wb'))
        
        
        
        
        
        gb=GradientBoostingClassifier(n_estimators=1000, random_state=4)
        gb.fit(X_train, y_train)
        y_pred_gb = gb.predict(X_test)
        file_gb1 = 'file_gb1.sav'
        if self.test!=True:
            pickle.dump(gb, open(file_gb1, 'wb'))
        
        
        
        
        #creation of secondary dataset using the primary dataset
        newdata=pd.DataFrame({"knn":y_pred_knn,"rf":y_pred_RF,"DT":y_pred_DT,"nb":nb_y_pred,"SVM":y_pred_SVMK,"BG":y_pred_bg,"ET":y_pred_et,"ADB":y_pred_adb,"GB":y_pred_gb})
        if self.test!=True:
            newdata.to_csv("secondary_dataset.csv")
        
        
        
        # In[ ]:
        
        
        X_train, X_test, y_train, y_test = train_test_split(newdata, y_test, test_size = 0.1, random_state = 0)
        
        
        
        from sklearn.naive_bayes import GaussianNB
        nbclassifier2=GaussianNB()
        nbclassifier2.fit(X_train, y_train)
        nb_y_pred = nbclassifier2.predict(X_test)
        self.accuracy= accuracy_score(y_test, nb_y_pred)*100
        
        
        file_final = 'file_final.sav'
        if self.test!=True:
            pickle.dump(nbclassifier2, open(file_final, 'wb'))
        
        
        return self.accuracy

