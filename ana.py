import pandas as pd
import jieba
import numpy as np
import importlib,sys
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba.analyse
train_x = pd.read_csv("getapp_x.txt",sep='\n')
train_y = pd.read_csv("getapp_y1.csv")
#test_x = pd.read_csv("test_x.csv")

stdi, stdo, stde = sys.stdin, sys.stdout, sys.stderr
sys.stdin, sys.stdout, sys.stderr = stdi, stdo, stde
h=train_x.head()
print(h)
cutted = []
for row in train_x.values:
    try:
        raw_words = (" ".join(jieba.cut(row[0])))
        cutted.append(raw_words)
    except AttributeError:
        print(row[0])
        cutted.append(u"还行 一般吧")

cutted_array = np.array(cutted)
data_cutted = pd.DataFrame({
    'description': cutted_array
})
print(data_cutted.head())

print(train_y.head())
wc = WordCloud()
wc.generate(''.join(data_cutted['description'][train_y['category'] == 1]))
plt.imshow(wc)
plt.show()

keywords_pos = jieba.analyse.extract_tags(''.join(data_cutted['description'][train_y['category'] == 0]), topK=20)
for item in keywords_pos:
    print(item)
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_score
train_x, test_x, train_y, test_y = train_test_split(data_cutted['description'].ravel().astype('U'), train_y['category'].ravel(),
                                                        test_size=0.2, random_state=4)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(0.98, ngram_range=(1, 3)).fit(list(train_x))
array_trainx = vectorizer.transform(list(train_x))
array_trainy = train_y
from sklearn.svm import SVC
from sklearn.externals import  joblib
model = SVC(kernel='linear', gamma=10 ** -5, C=1).fit(array_trainx, array_trainy)
list_text = list(test_x)
array_testx = vectorizer.transform(list_text)
array_predict = model.predict(array_testx)
with open("model","wb") as f:
    joblib.dump(model,f)
with open("vecmodel", "wb") as f:
    joblib.dump(vectorizer, f)
array_predict[1:10]
test_y[1:10]
from sklearn import metrics
print(metrics.classification_report(test_y, array_predict))