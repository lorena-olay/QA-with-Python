import unittest
from unittest.mock import patch, MagicMock
import mysql.connector #pip install mysql-connector-python

class TestDatabaseOperations(unittest.TestCase):

    @patch('mysql.connector.connect')
    def test_fetch_data(self, mock_connect):
        # Configurar el mock
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor
        
        # Datos ficticios de retorno
        mock_cursor.fetchall.return_value = [("row1",), ("row2",)]

        # Llamada a la función que usa MySQL
        result = fetch_data_from_db()

        # Verificaciones
        mock_connect.assert_called_once()
        mock_cursor.execute.assert_called_once_with('SELECT * FROM my_table')
        self.assertEqual(result, [("row1",), ("row2",)])

def fetch_data_from_db():
    conn = mysql.connector.connect(user='user', password='passwd', host='127.0.0.1', database='test_db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM my_table')
    return cursor.fetchall()

if __name__ == '__main__':
    unittest.main()
