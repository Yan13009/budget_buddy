import unittest
from Server import Server
class TestCRUD(unittest.TestCase,Server):
    def setUp(self):
        self.server = Server()

    def test_create_read_delete(self):
        self.server.create_account(1, "John", "Doe", "john@example.com", "password")
        self.server.read_account()
        self.server.delete_account(1)
        self.server.read_account()  # Vérifier si le compte a été supprimé
        self.server.create_transaction(1, "John", "Doe", "john@example.com", "password")
        self.server.read_transactions()
        self.server.delete_transaction(1)
        self.server.read_transactions()  # Vérifier si le compte a été supprimé

if __name__ == '__main__':
    unittest.main()