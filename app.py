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
    cursor = conn.execute("select title,url from urls where url like '%www.youtube.com/%' and url like '%/watch?%'")
    #urls=conn.execute("select url from urls where url like '%www.youtube.com/%' and url like '%/watch?%'")
    result={}

    for row in cursor:
        result[row[0]]='https://www.youtubeinmp3.com/download/?video='+row[1]

    conn.close()
    res = sorted(result.items(), key=operator.itemgetter(1),reverse=True)
    return render_template('rec.html',res=res)

if __name__ == '__main__':
   app.run(debug = True)