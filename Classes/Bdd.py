# CRUD operation
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
    
    def create_transaction(self, id_transaction, nom, description, montant, date, type_transaction):
        cursor = self.mydb.cursor()
        cursor.execute("""
            INSERT INTO transaction (id_transaction, nom, description, montant, date, type_transaction)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (id_transaction, nom, description, montant, date, type_transaction))
        self.mydb.commit()
    
    def read_transactions(self):
        cursor = self.mydb.cursor()
        cursor.execute("SELECT * FROM transaction")
        for (id_transaction, nom, description, montant, date, type_transaction) in cursor:
            print(f"ID Transaction: {id_transaction}, Nom: {nom}, Description: {description}, Montant: {montant}, Date: {date}, Type de Transaction: {type_transaction}")
    
    def update_transaction(self, id_transaction, nom, description, montant, date, type_transaction):
        cursor = self.mydb.cursor()
        cursor.execute("""
            UPDATE transaction 
            SET nom = %s,
            description = %s,
            montant = %s,
            date = %s,
            type_transaction = %s
            WHERE id_transaction = %s
            """, (nom, description, montant, date, type_transaction, id_transaction))
        self.mydb.commit()
        
    def delete_transaction(self, id_transaction):
        cursor = self.mydb.cursor()
        cursor.execute("""
            DELETE FROM transaction
            WHERE id_transaction = %s
        """, (id_transaction,))
        self.mydb.commit()