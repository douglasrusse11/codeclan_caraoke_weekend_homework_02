import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestSetup(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Barry", 10)
        self.guest2 = Guest("Belinda", 15)
        self.room1 = Room(2, 5)
        self.song1 = Song("Shoe Box Money", "Benny Sings")
        self.song2 = Song("Baleine", "Purl")