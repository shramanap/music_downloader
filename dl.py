# importing required libraries and modules
import operator

from flask import Flask, render_template

from utils import get_chrome_db_connection

DB_QUERY = "select title,url from urls where url like '%www.youtube.com/%' and url like '%/watch?%'"

app = Flask(__name__)


@app.route('/')
def index():
    conn = get_chrome_db_connection()
    cursor = conn.execute(DB_QUERY)
    result = dict()
    import pdb; pdb.set_trace()
    for row in cursor:
        result[row[0]] = 'https://www.youtubeinmp3.com/download/?video=' + row[1]
    conn.close()
    res = sorted(result.items(), key=operator.itemgetter(1), reverse=True)
    return render_template('rec.html', res=res)


if __name__ == '__main__':
    app.run(debug=True)
