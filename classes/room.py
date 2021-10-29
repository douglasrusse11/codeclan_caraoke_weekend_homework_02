import random

class Room:
    def __init__(self, capacity, fee):
        """Initialise Room object"""
        self.guests = []
        self.songs = []
        self.capacity = capacity
        self.fee = fee
        self.till = 0
        self.favourite_songs = {}
        self.playlist = {}

    def check_in_guest(self, guest):
        """Adds guest to Room
        
        If guest can afford the room's entry fee and the room is not at capacity,
        adds guest to List guests, increments the room's till, decrements the guests
        wallet, adds the guest's favourite song to favourite_songs, and returns "Whoo!"
        if the guest's favourite song is in List songs.
        """
        if guest.can_afford_entry_fee(self.fee) and not self.is_at_capacity():
            self.guests.append(guest)
            self.charge_fee()
            guest.pay_fee(self.fee)
            self.add_favourite_song(guest)
            return guest.cheer(self.songs)

    def check_out_guest(self, guest):
        """Removes guest from self.guests"""
        self.guests.remove(guest)
        self.remove_favourite_song(guest)

    def add_song(self, song):
        """Adds song to List self.songs"""
        self.songs.append(song)

    def is_at_capacity(self):
        """Returns True if number of guests is equal to capacity"""
        return len(self.guests) == self.capacity

    def add_favourite_song(self, guest):
        """Appends guest to guests in song:guests key:value pair, adds key to Dict if not in keys"""
        if guest.favourite_song not in self.favourite_songs:
            self.favourite_songs[guest.favourite_song] = []
        self.favourite_songs[guest.favourite_song].append(guest)

    def remove_favourite_song(self,guest):
        """Removes guest from guests in song:guests key:value pair, removes key if guests is empty"""
        self.favourite_songs[guest.favourite_song].remove(guest)   
        if self.favourite_songs[guest.favourite_song] == []:
            del self.favourite_songs[guest.favourite_song]

    def generate_playlist(self):
        """Sets playlist to a Dict of Song:Guest key:value pairs where each Song is the favourite song of a Guest"""
        self.playlist = {song:self.song_lottery(song) for song in self.songs if song in self.favourite_songs}

    def song_lottery(self, song):
        """Returns random Guest from List guests in song:guests key:value pair"""
        return self.favourite_songs[song][random.randint(0, len(self.favourite_songs[song]) - 1)]

    def charge_fee(self):
        """Increments till by fee"""
        self.till += self.fee