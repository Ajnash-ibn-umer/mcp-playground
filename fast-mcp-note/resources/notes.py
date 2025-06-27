
import sqlite3


conn=sqlite3.connect("notes.db")
cursor=conn.cursor()
conn.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, content TEXT)")
def createNote(content:str,title:str=None):
    """create new note with title and content, title is optional"""
    print(title,content)
    cursor.execute("INSERT INTO notes (title,content) VALUES (?,?)",(title,content))
    conn.commit()
    return cursor.lastrowid


def getNotes():
    """get all notes"""
    return cursor.execute("SELECT * FROM notes").fetchall()