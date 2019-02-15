from hashlib import blake2b
import sqlite3
from sqlite3 import Error


def save(url,hash):
    conn = sqlite3.connect("urls.db")
    c = conn.cursor()
    c.execute("INSERT INTO url_shortcuts(code,real) VALUES (?,?)" , [hash,url] )
    conn.commit()
    conn.close()

def read(hash):
    conn = sqlite3.connect("urls.db")
    c = conn.cursor()
    temp = c.execute('SELECT code,real FROM url_shortcuts WHERE code = \'%s\'' % hash).fetchone()
    conn.close()
    print(temp)
    return temp[1]

def readAll():
    conn = sqlite3.connect("urls.db")
    c = conn.cursor()
    c.execute("SELECT code,real FROM url_shortcuts")
    data = c.fetchall()
    conn.close()
    return data

def getHash(text):
    h = blake2b(digest_size=8)
    h.update(bytes(text, 'utf8'))
    code = h.hexdigest()
    return code


#initialize()
print(readAll())
