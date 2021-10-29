import unittest
from tests.setup_test import TestSetup

class TestRoom(TestSetup):
    def test_room_has_no_guests(self):
        self.assertEqual([], self.room1.guests)

    def test_room_has_no_songs(self):
        self.assertEqual([], self.room1.songs)

    def test_room_has_capacity(self):
        self.assertEqual(2, self.room1.capacity)

    def test_room_has_fee(self):
        self.assertEqual(5, self.room1.fee)

    def test_room_has_empty_till(self):
        self.assertEqual(0, self.room1.till)

    def test_room_has_no_favourite_songs(self):
        self.assertEqual({}, self.room1.favourite_songs)

    def test_room_has_no_playlist(self):
        self.assertEqual({}, self.room1.playlist)

    def test_check_in_guest(self):
        self.room1.check_in_guest(self.guest1)
        self.assertEqual(1, len(self.room1.guests))

    def test_check_in_multiple_guests(self):
        self.room1.check_in_guest(self.guest1)
        self.room1.check_in_guest(self.guest2)
        self.assertEqual(2, len(self.room1.guests))

    def test_check_out_guest(self):
        self.room1.check_in_guest(self.guest1)
        self.room1.check_out_guest(self.guest1)
        self.assertEqual([], self.room1.guests)

    def test_check_out_correct_guest(self):
        self.room1.check_in_guest(self.guest1)
        self.room1.check_in_guest(self.guest2)
        self.room1.check_out_guest(self.guest1)
        self.assertEqual(1, len(self.room1.guests))
        self.assertTrue(self.guest2 in self.room1.guests)
        self.assertFalse(self.guest1 in self.room1.guests)

    def test_add_song(self):
        self.room1.add_song(self.song1)
        self.assertEqual(1, len(self.room1.songs))

    def test_add_multiple_songs(self):
        self.room1.add_song(self.song1)
        self.room1.add_song(self.song2)
        self.assertEqual(2, len(self.room1.songs))

    def test_add_correct_songs(self):
        self.room1.add_song(self.song1)
        self.room1.add_song(self.song2)
        self.assertTrue(self.song1 in self.room1.songs)
        self.assertTrue(self.song2 in self.room1.songs)
        
    def test_room_is_at_capacity(self):
        self.room1.check_in_guest(self.guest1)
        self.room1.check_in_guest(self.guest2)
        self.assertTrue(self.room1.is_at_capacity())

    def test_room_is_not_at_capacity(self):
        self.room1.check_in_guest(self.guest1)
        self.assertFalse(self.room1.is_at_capacity())

    def test_empty_room_is_not_at_capacity(self):
        self.assertFalse(self.room1.is_at_capacity())

    def test_add_favourite_song(self):
        result = {self.song1: [self.guest1]}
        self.room1.add_favourite_song(self.guest1)
        self.assertEqual(result, self.room1.favourite_songs)

    def test_add_favourite_song_multiple_guests_same_song(self):
        result = {self.song1: [self.guest1, self.guest4]}
        self.room1.add_favourite_song(self.guest1)
        self.room1.add_favourite_song(self.guest4)
        self.assertEqual(result, self.room1.favourite_songs)

    def test_add_favourite_song_multiple_guests_multiple_songs(self):
        result = {self.song1: [self.guest1, self.guest4], self.song2: [self.guest2]}
        self.room1.add_favourite_song(self.guest1)
        self.room1.add_favourite_song(self.guest2)
        self.room1.add_favourite_song(self.guest4)
        self.assertEqual(result, self.room1.favourite_songs)

    def test_generate_playlist(self):
        self.room1.add_song(self.song1)
        self.room1.add_song(self.song2)
        self.room1.add_favourite_song(self.guest1)
        self.room1.add_favourite_song(self.guest2)
        self.room1.add_favourite_song(self.guest3)
        self.room1.add_favourite_song(self.guest4)
        self.room1.generate_playlist()
        self.assertTrue(self.room1.playlist[self.song1] in [self.guest1, self.guest4])
        self.assertTrue(self.room1.playlist[self.song2] in [self.guest2, self.guest3])

    def test_generate_playlist_song_not_in_favourites(self):
        self.room1.add_song(self.song1)
        self.room1.add_song(self.song2)
        self.room1.add_song(self.song3)
        self.room1.add_favourite_song(self.guest1)
        self.room1.add_favourite_song(self.guest2)
        self.room1.add_favourite_song(self.guest3)
        self.room1.add_favourite_song(self.guest4)
        self.room1.generate_playlist()
        self.assertFalse(self.song3 in self.room1.playlist)
        
    def test_song_lottery(self):
        self.room1.add_favourite_song(self.guest1)
        self.room1.add_favourite_song(self.guest2)
        self.room1.add_favourite_song(self.guest3)
        self.room1.add_favourite_song(self.guest4)
        self.assertTrue(self.room1.song_lottery(self.song1) in [self.guest1, self.guest4])
        self.assertTrue(self.room1.song_lottery(self.song2) in [self.guest2, self.guest3])
    
    # Integration tests
    def test_room_refuses_entry_if_guest_cannot_afford_entry_fee(self):
        self.room1.check_in_guest(self.guest3)
        self.assertEqual([], self.room1.guests)

    def test_room_refuses_entry_if_room_is_at_capacity(self):
        self.room1.check_in_guest(self.guest1)
        self.room1.check_in_guest(self.guest2)
        self.room1.check_in_guest(self.guest4)
        self.assertEqual(2, len(self.room1.guests))
        self.assertTrue(self.guest1 in self.room1.guests)
        self.assertTrue(self.guest2 in self.room1.guests)
        self.assertFalse(self.guest4 in self.room1.guests)

    @unittest.skip('')
    def test_room_entry_fee_is_charged(self):
        self.room1.check_in_guest(self.guest1)
        self.assertEqual(5, self.room1.till)
        self.assertEqual(5, self.guest1.wallet)

    @unittest.skip('')
    def test_room_entry_fee_is_charged_at_capacity(self):
        self.room1.check_in_guest(self.guest1)
        self.room1.check_in_guest(self.guest2)
        self.room1.check_in_guest(self.guest4)
        self.assertEqual(10, self.room1.till)
    
    @unittest.skip('')
    def test_room_entry_fee_is_charged_check_outs(self):
        self.room1.check_in_guest(self.guest1)
        self.room1.check_in_guest(self.guest2)
        self.room1.check_out_guest(self.guest1)
        self.room1.check_in_guest(self.guest4)
        self.assertEqual(15, self.room1.till)
        

    

