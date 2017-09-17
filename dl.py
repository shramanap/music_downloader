#importing required libraries and modules
import sys
from flask import Flask,render_template,jsonify,request, make_response
import sqlite3
import shutil
import os
import sys
import operator

app = Flask(__name__)

@app.route('/')
def index():
    homeDir = os.environ['HOME']
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') +'/res'
    path=homeDir +'/.config/google-chrome/Default/History'
    shutil.copy2(path, desktop)
    conn = sqlite3.connect(desktop+'/History')
    cursor = conn.execute("select title from urls where url like '%www.youtube.com/%' and url like '%/watch?%'")
    urls=conn.execute("select url from urls where url like '%www.youtube.com/%' and url like '%/watch?%'")
    result={}
    name=[]
    i=0
    for row in cursor:
        name.append(row[0])
    for row in urls:
        result[name[i]]='https://www.youtubeinmp3.com/download/?video='+row[0]
        i=i+1
    conn.close()
    res = sorted(result.items(), key=operator.itemgetter(1))
    return render_template('rec.html',res=res)

if __name__ == '__main__':
   app.run(debug = True)
