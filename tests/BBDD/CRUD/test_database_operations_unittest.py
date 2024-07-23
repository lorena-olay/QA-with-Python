import unittest
from unittest.mock import patch, MagicMock
from database_operations import create_user, read_user, update_user, delete_user

class TestDatabaseOperations(unittest.TestCase):

    @patch('mysql.connector.connect')
    def test_create_user(self, mock_connect):
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor

        create_user('test_user', 'test_pass')

        mock_cursor.execute.assert_called_once_with('INSERT INTO users (username, password) VALUES (%s, %s)', ('test_user', 'test_pass'))
        mock_connection.commit.assert_called_once()
        mock_cursor.close.assert_called_once()
        mock_connection.close.assert_called_once()

    @patch('mysql.connector.connect')
    def test_read_user(self, mock_connect):
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = ('test_user', 'test_pass')

        result = read_user('test_user')

        mock_cursor.execute.assert_called_once_with('SELECT * FROM users WHERE username = %s', ('test_user',))
        self.assertEqual(result, ('test_user', 'test_pass'))
        mock_cursor.close.assert_called_once()
        mock_connection.close.assert_called_once()

    @patch('mysql.connector.connect')
    def test_update_user(self, mock_connect):
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor

        update_user('test_user', 'new_pass')

        mock_cursor.execute.assert_called_once_with('UPDATE users SET password = %s WHERE username = %s', ('new_pass', 'test_user'))
        mock_connection.commit.assert_called_once()
        mock_cursor.close.assert_called_once()
        mock_connection.close.assert_called_once()

    @patch('mysql.connector.connect')
    def test_delete_user(self, mock_connect):
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor

        delete_user('test_user')

        mock_cursor.execute.assert_called_once_with('DELETE FROM users WHERE username = %s', ('test_user',))
        mock_connection.commit.assert_called_once()
        mock_cursor.close.assert_called_once()
        mock_connection.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()
