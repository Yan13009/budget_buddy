import mysql.connector

class Server:
    
    def __init__(self):
        self.db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'root',
            'database': 'budget_buddy'
        }
        self.mydb = mysql.connector.connect(**self.db_config)
    
    def create_account(self, id_compte, nom, prenom, email, mot_de_passe):
        cursor = self.mydb.cursor()
        cursor.execute("""
            INSERT INTO compte (id_compte, nom, prenom, email, mot_de_passe)
            VALUES (%s, %s, %s, %s, %s)
        """, (id_compte, nom, prenom, email, mot_de_passe))
        self.mydb.commit()
    
    def read_account(self):
        cursor = self.mydb.cursor()
        cursor.execute("SELECT * FROM compte")
        for (id_compte, nom, prenom, email, mot_de_passe) in cursor:
            print(f"ID: {id_compte}, NOM: {nom}, PRENOM: {prenom}, email: {email}, mot_de_passe: {mot_de_passe}")
    
    def update_account(self, id_compte, nom, prenom, email, mot_de_passe):
        cursor = self.mydb.cursor()
        cursor.execute("""
            UPDATE compte 
            SET nom = %s,
            prenom = %s,
            email = %s,
            mot_de_passe = %s
            WHERE id_compte = %s
            """, (nom, prenom, email, mot_de_passe, id_compte))
        self.mydb.commit()
        
    def delete_account(self, id_compte):
        cursor = self.mydb.cursor()
        cursor.execute("""
            DELETE FROM compte
            WHERE id_compte = %s
        """, (id_compte,))
        self.mydb.commit()