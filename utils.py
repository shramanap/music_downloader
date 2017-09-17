import os
import shutil
import sqlite3

CHROME_HISTORY_PATH = '/.config/google-chrome/Default/History'


def _dummy_query(conn):
    conn.execute('select * from table')


def copy_database(path):
    backup_path = path + '.bak'
    shutil.copy2(path, backup_path)
    return backup_path


def get_chrome_db_connection():
    home = os.environ['HOME']
    db_path = home + CHROME_HISTORY_PATH
    conn = sqlite3.connect(db_path)
    try:
        _dummy_query(conn)
    except sqlite3.OperationalError:
        copy = copy_database(db_path)
        conn = sqlite3.connect(copy)
    return conn
