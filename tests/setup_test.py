import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestSetup(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Shoe Box Money", "Benny Sings")
        self.song2 = Song("Bounding", "Ice Choir")
        self.guest1 = Guest("Barry", 10, self.song1)
        self.guest2 = Guest("Belinda", 15, self.song2)
        self.guest3 = Guest("Bill", 2, self.song2)
        self.guest4 = Guest("Bobette", 7, self.song1)
        self.room1 = Room(2, 5)
        