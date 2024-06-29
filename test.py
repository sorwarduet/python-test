import unittest
from unittest.mock import AsyncMock, patch
import discord
import os
class TestSupperBot(unittest.TestCase):

    def setUp(self):
        self.token = os.getenv('DISCORD_TOKEN')
        self.invalid_token = os.getenv('INVALID_TOKEN')



if __name__ == "__main__":
    unittest.main()