import unittest
from tests.setup_test import TestSetup

class TestRoom(TestSetup):
    def test_room_has_no_guests(self):
        self.assertEqual([], self.room1.guests)

    def test_room_hass_no_songs(self):
        self.assertEqual([], self.room1.songs)

    @unittest.skip('')
    def test_check_in_guest(self):
        self.room1.check_in_guest(self.guest1)
        self.assertEqual(1, len(self.room1.guests))

    @unittest.skip('')
    def test_check_in_multiple_guests(self):
        self.room1.check_in_guest(self.guest1)
        self.room1.check_in_guest(self.guest2)
        self.assertEqual(2, len(self.room1.guests))