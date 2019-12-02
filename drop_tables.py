import sqlite3

conn = sqlite3.connect('weapons.sqlite')

c = conn.cursor()
c.execute('''
          DROP TABLE weapons
          ''')

conn.commit()
conn.close()