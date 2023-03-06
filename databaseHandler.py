import sqlite3


def init_entreprise_db(path):
    con = sqlite3.connect(path)

    cur = con.cursor()

    cur.execute("CREATE TABLE entreprise(name, tresorerie)")

    return cur


cur = init_entreprise_db("db/entreprise.db")

cur.execute("""
    INSERT INTO entreprise VALUES
        ('sephora', 2000)
""")

res = cur.execute("SELECT name FROM entreprise")
print(res.fetchone())