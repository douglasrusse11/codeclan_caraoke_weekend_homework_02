import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestSetup(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Barry")
        self.guest2 = Guest("Belinda")
        self.room1 = Room()
        self.song1 = Song("Shoe Box Money", "Benny Sings")