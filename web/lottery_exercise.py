# 支持服务访问
# 需要web框架
# 安装Flask

from flask import Flask, render_template
from random import randint

app = Flask(__name__)
flist = open('lottery/m_list','r')
members=flist.readlines()
m_list = []
for m in members:
    m = m.replace('\n','')
    m_list.append(m)
flist.close()

@app.route('/index')
def index():
    return render_template('index.html',hero = m_list)
@app.route('/choose')
def choose():
    num = randint(0,len(m_list))
    return render_template('index.html',hero = m_list, h = m_list[num])

app.run(debug=True)