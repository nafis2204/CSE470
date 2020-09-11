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

#preprocessing train set for primary models
dataset=pd.read_csv('bank.csv')
df=dataset

df=df.drop(["duration","job","contact","month","poutcome"],axis=1)
df.head()
df.columns
df["marital"] = [0 if each== "single" else 1 for each in df.marital]
df["default"] = [0 if each== "no" else 1 for each in df.default]
df["housing"] = [0 if each== "no" else 1 for each in df.housing]
df["loan"] = [0 if each== "no" else 1 for each in df.loan]
df["y"] = [0 if each== "no" else 1 for each in df.y]
for each in df.education:
    if each == "unknown" or each=="primary":
        df["education"] = 0
    elif each =="seondary":
        df["education"] = 1
    else:
        df["education"]=2

#preprocessing test set for secondary pipeline (this will go initially through trained primary
#models(9) and will act as the test case for the final model)
dataset1=pd.read_csv('bank-full.csv')
df1=dataset1
df1=df1.drop(["job","education","contact","month","poutcome"],axis=1)
df1["marital"] = [0 if each== "single" else 1 for each in df1.marital]
df1["default"] = [0 if each== "no" else 1 for each in df1.default]
df1["housing"] = [0 if each== "no" else 1 for each in df1.housing]
df1["loan"] = [0 if each== "no" else 1 for each in df1.loan]
df1["y"] = [0 if each== "no" else 1 for each in df1.y]
x1 = df.iloc[:, 0:11].values
y1 = df.iloc[:,11].values

# Splitting the dataset into the Training set and Test set
X = df.iloc[:, 0:11].values
y = df.iloc[:,11].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)


# Feature Scaling
sc = StandardScaler()
X=sc.fit_transform(X)
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
x1=sc.fit_transform(x1)


newdata=[]

#using 9 ML model to create a secondary dataset


knn = KNeighborsClassifier(n_neighbors = 10)  # n_neighbors means k
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)
file_knn1 = 'file_knn1.sav'
pickle.dump(knn, open(file_knn1, 'wb'))



RF = RandomForestClassifier(n_estimators=100, criterion='entropy', random_state=0)  
RF.fit(X_train, y_train)
y_pred_RF = RF.predict(X_test)
file_rf1 = 'file_rf1.sav'
pickle.dump(RF, open(file_rf1, 'wb'))





dtclassifier= DecisionTreeClassifier(criterion='entropy')
dtclassifier.fit(X_train,y_train)
y_pred_DT = dtclassifier.predict(X_test)
file_dt1 = 'file_dt1.sav'
pickle.dump(dtclassifier, open(file_dt1, 'wb'))





nbclassifier=GaussianNB()
nbclassifier.fit(X_train, y_train)
nb_y_pred = nbclassifier.predict(X_test)
file_nb1 = 'file_nb1.sav'
pickle.dump(nbclassifier, open(file_nb1, 'wb'))




svmkclassifier =SVC(kernel ='rbf',random_state=0,gamma='auto')
svmkclassifier.fit(X_train, y_train)
y_pred_SVMK = svmkclassifier.predict(X_test)
file_svm1 = 'file_svm1.sav'
pickle.dump(svmkclassifier, open(file_svm1, 'wb'))






bg=BaggingClassifier(base_estimator=DecisionTreeClassifier(), n_estimators=100, random_state=15)
bg.fit(X_train, y_train)
y_pred_bg = bg.predict(X_test)
file_bg1 = 'file_bg1.sav'
pickle.dump(bg, open(file_bg1, 'wb'))





et=ExtraTreesClassifier(n_estimators=100, max_features=4)
et.fit(X_train, y_train)
y_pred_et = et.predict(X_test)
file_et1 = 'file_et1.sav'
pickle.dump(et, open(file_et1, 'wb'))





adb=AdaBoostClassifier(n_estimators=50, random_state=4)
adb.fit(X_train, y_train)
y_pred_adb = adb.predict(X_test)
file_adb1 = 'file_adb1.sav'
pickle.dump(adb, open(file_adb1, 'wb'))





gb=GradientBoostingClassifier(n_estimators=1000, random_state=4)
gb.fit(X_train, y_train)
y_pred_gb = gb.predict(X_test)
file_gb1 = 'file_gb1.sav'
pickle.dump(gb, open(file_gb1, 'wb'))




#creation of secondary dataset using the primary dataset
newdata=pd.DataFrame({"knn":y_pred_knn,"rf":y_pred_RF,"DT":y_pred_DT,"nb":nb_y_pred,"SVM":y_pred_SVMK,"BG":y_pred_bg,"ET":y_pred_et,"ADB":y_pred_adb,"GB":y_pred_gb})



#secondary model prep
x_test=X_test.reshape(1131,11,1)
x_train=X_train.reshape(3390,11,1)


# In[ ]:


X_train, X_test, y_train, y_test = train_test_split(newdata, y_test, test_size = 0.1, random_state = 0)



from sklearn.naive_bayes import GaussianNB
nbclassifier2=GaussianNB()
nbclassifier2.fit(X_train, y_train)
file_final = 'file_final.sav'
pickle.dump(nbclassifier2, open(file_final, 'wb'))


