import unittest
from tests.setup_test import TestSetup

class TestRoom(TestSetup):
    @unittest.skip('')
    def test_room_has_no_guests(self):
        self.assertEqual([], self.room1.guests)

    @unittest.skip('')
    def test_room_hass_no_songs(self):
        self.assertEqual([], self.room1.songs)