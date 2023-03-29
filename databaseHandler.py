import sqlite3


# Initialiser la base de données
def init_db():
    conn = sqlite3.connect('entreprise.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS entreprise (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            tresorerie INTEGER,
            employes INTEGER,
            ressources TEXT,
            prix_produit INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# Ajouter une entreprise à la base de données
def ajouter_entreprise(name, tresorerie=10000, employes=0, ressources=[0, 0], prix_produit=100):
    conn = sqlite3.connect('entreprise.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO entreprise (name, tresorerie, employes, ressources, prix_produit)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, tresorerie, employes, str(ressources), prix_produit))
    conn.commit()
    conn.close()

# Obtenir les informations d'une entreprise par son nom
def obtenir_entreprise(name):
    conn = sqlite3.connect('entreprise.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM entreprise WHERE name=?
    ''', (name,))
    result = cursor.fetchone()
    conn.close()
    if result is not None:
        return {
            'id': result[0],
            'name': result[1],
            'tresorerie': result[2],
            'employes': result[3],
            'ressources': eval(result[4]),
            'prix_produit': result[5]
        }
    else:
        return None
    


def retrieve_data_by_type(db_path, data_type):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT {data_type} FROM entreprise")
    results = cursor.fetchall()
    
    conn.close()
    
    if len(results) == 0:
        return []
    else:
        return results


if __name__ == "__main__":
    init_db()
    ajouter_entreprise("microsoft")
    ajouter_entreprise("channel")
    a = obtenir_entreprise("microsoft")
    b = obtenir_entreprise("channel")
    print(a)
    print(b)