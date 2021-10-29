import unittest
from tests.setup_test import TestSetup

class TestGuest(TestSetup):
    def test_guest_has_name(self):
        self.assertEqual("Barry", self.guest1.name)

    def test_guest_wallet(self):
        self.assertEqual(10, self.guest1.wallet)

    def test_guest_has_favourite_song(self):
        self.assertEqual(self.song1, self.guest1.favourite_song)

    def test_guest_can_afford_entry_fee(self):
        self.fee = 5
        self.assertTrue(self.guest2.can_afford_entry_fee(self.fee))

    def test_guest_cannot_afford_entry_fee(self):
        self.fee = 15
        self.assertFalse(self.guest1.can_afford_entry_fee(self.fee))

    def test_guest_cheer(self):
        songs = [self.song1, self.song2]
        self.assertEqual("Whoo!", self.guest1.cheer(songs))

    def test_guest_cheer_song_not_in_room(self):
        songs =[self.song1]
        self.assertEqual(None, self.guest2.cheer(songs))