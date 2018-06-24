from sklearn.svm import SVC
from sklearn.externals import  joblib
import pandas as pd
test_x = pd.read_csv("test_x.csv")
with open("vecmodel", "wb") as f:
    vectorizer=joblib.load(f)
list_text = list(test_x)
array_testx = vectorizer.transform(list_text)
with open("model","wb") as f:
    model=joblib.dump(f)
array_predict = model.predict(array_testx)
