import csv, sqlite3

con = sqlite3.connect("testdb.db")
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS t (id INTEGER PRIMARY KEY AUTOINCREMENT, Country TEXT, City TEXT, CityId INTEGER)''')

with open('full_city_list.csv','r') as fin: 
    dr = csv.reader(fin, delimiter=';')
    for row in dr:
        cur.execute('INSERT INTO t (Country, City, CityId) VALUES(?, ?, ?)',(row[0], row[1], row[2]))
        con.commit()

def supdate(City):
    cur.execute(f'UPDATE t SET City="Kropyvnytskyi" WHERE City="{City}"')
    con.commit()

supdate('Currie')
con.commit()
con.close()