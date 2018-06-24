from sklearn.externals import  joblib
import pandas as pd
import pandas as pd
import sqlite3
import jieba
import numpy as np
import importlib,sys
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba.analyse
from jieba import analyse

#train_x = pd.read_csv("getapp_x.txt",sep='\n')
#train_y = pd.read_csv("getapp_y.csv")
#test_x = pd.read_csv("test_x.csv")
tfidf = analyse.extract_tags
with open("getapp_x.txt","rb") as f:
    train_x=f.readlines()

for text in train_x:
    cut=(" ".join(jieba.cut(text)))
    keywords=tfidf(text)
    tags=""
    if (len(keywords) > 2):
        tags=keywords[0] + " " + keywords[1]
        print(tags)