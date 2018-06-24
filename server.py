#coding=utf-8
from analyse import analyse
from flask import Flask, request, render_template
from flask import make_response,Response

app = Flask(__name__,static_url_path='')


@app.route('/',methods=['GET'])
def hello_world():
    name = request.args.get('cd-name')
    text = request.args.get('cd-textarea')
    if(name==None and text==None):
        return render_template('index.html')
    else:
        kind,tags=analyse(name,text)
        return render_template('index.html',kind="类别："+kind,tags="标签："+tags)

@app.route('/login',methods=['GET'])
def search():
    passwd=request.args.get('passwd')
    return analyse(passwd)

if __name__ == '__main__':
    app.run()