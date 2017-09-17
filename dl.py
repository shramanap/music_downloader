import sqlite3
import shutil
import os
import sys
import json

homeDir = os.environ['HOME']
desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') +'/res'
path=homeDir +'/.config/google-chrome/Default/History'
shutil.copy2(path, desktop)
conn = sqlite3.connect(desktop+'/History')

cursor = conn.execute("select url from urls where url like '%www.youtube.com/%' and title not like 'YouTube'")

files=desktop+'/res.txt'
sys.stdout=open(files,"w")

#for row in cursor:
#   print (row[0])


conn.close()


import requests

url = 'http://convert2mp3.net/en/'
payload = {'convertForm' : 'https://www.youtube.com/watch?v=3AtDnEC4zak'}

r = requests.post(url,data=json.dumps(payload))
print (r.text)