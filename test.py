import unittest
from unittest.mock import AsyncMock, patch
import discord
import os
from dotenv import load_dotenv
from main import MyClient  # Adjust this import based on the actual location of your MyClient class


class TestSupperBot(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        load_dotenv()  # Load environment variables from .env file

    def setUp(self):
        self.token = os.getenv('DISCORD_TOKEN')
        self.invalid_token = os.getenv('INVALID_TOKEN')

    @patch('discord.Client.login', new_callable=AsyncMock)
    @patch('discord.Client.connect', new_callable=AsyncMock)
    def test_bot_login_success(self, mock_connect, mock_login):
        """Test bot login with a valid token."""
        client = MyClient(intents=discord.Intents.default())

        # Mock the run method to avoid actual connection attempt
        with patch.object(client, 'run', return_value=None):
            client.run(self.token)

        # Verify that login was attempted with the correct token
        mock_login.assert_called_with(self.token)
        mock_connect.assert_called_once()




if __name__ == "__main__":
    unittest.main()