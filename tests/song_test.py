import unittest
from tests.setup_test import TestSetup

class TestSong(TestSetup):
    def test_song_has_title(self):
        self.assertEqual("Shoe Box Money", self.song1.title)
    
    @unittest.skip('')
    def test_song_has_artist(self):
        self.assertEqual("Benny Sings", self.song1.artist)