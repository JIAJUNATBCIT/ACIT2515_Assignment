import sqlite3

conn = sqlite3.connect('weapons.sqlite')

c = conn.cursor()
c.execute('''
          CREATE TABLE weapons
          (id INTEGER PRIMARY KEY ASC, 
           name VARCHAR(100) NOT NULL,
           materials VARCHAR(100) NOT NULL,
           is_cold_weapon INTEGER NOT NULL,
           is_inuse INTEGER NOT NULL,
           manufacture_date DATE NOT NULL,
           retired_date DATE,
           sharp FLOAT,
           length FLOAT,
           is_double_edged INTEGER,
           bullets_num INTEGER,
           range FLOAT,
           is_overheat INTEGER,
           type VARCHAR(20) NOT NULL)
          ''')

conn.commit()
conn.close()