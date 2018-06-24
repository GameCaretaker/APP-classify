#coding=utf-8
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

dic={'0': '图形图像\n', '1': '学习工具\n', '2': '影音媒体\n', '3': '聊天交友\n', '4': '桌面美化\n', '5': '生活实用\n', '6': 'category\n', '7': '电子阅读\n', '8': '商务办公\n', '9': '游戏工具\n', '10': '安全杀毒\n', '11': '健康医疗\n', '12': '理财购物\n', '13': '交通出行\n', '14': '通信增强\n', '15': '拍照摄影\n', '16': '网络浏览\n', '17': '系统工具\n'}
conn = sqlite3.connect('app.db',check_same_thread=False)
cursor=conn.cursor()

with open("vecmodel", "rb") as f:
    vectorizer = joblib.load(f)
with open("model", "rb") as f:
    model = joblib.load(f)
tfidf = analyse.extract_tags

def analyse(name,text):
    cut=(" ".join(jieba.cut(text)))
    keywords = tfidf(text)
    print(keywords)
    tags=""
    if (len(keywords) > 2):
        tags=keywords[0] + " " + keywords[1]
    #ss=" select info,tags from app where name='%s' "%name
    #cursor.execute(ss)
    #results=[]
    #results = cursor.fetchall()
    #if(len(results)>0):
     #   return "%s"%results[0][0], results[0][1]
    list_text = [cut]
    print(list_text)
    array_testx = vectorizer.transform(list_text)
    print(array_testx)
    array_predict = model.predict(array_testx)
    print(array_predict)
    return dic["%d"%array_predict], tags
