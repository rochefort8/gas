from sklearn.model_selection import train_test_split
from sklearn import datasets, svm ,metrics
from sklearn.metrics import accuracy_score
 
digits = datasets.load_digits()

x = digits.images

y = digits.target
x = x.reshape((-1,64))

print(y)

x_train, x_test, y_train,y_test = train_test_split(x,y,test_size = 0.2)

from sklearn.externals import joblib
model = joblib.load('digits.pkl')

#clf = svm.LinearSVC()
#clf.fit(x_train, y_train)

result = model.score(x_test,y_test)
print (result)

#y_pred = clf.predict(x_test)
#print(accuracy_score(y_test,y_pred))
 
#from sklearn.externals import joblib
#joblib.dump(clf, 'digits.pkl')
