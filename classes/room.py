class Room:
    def __init__(self, capacity, fee):
        self.guests = []
        self.songs = []
        self.capacity = capacity
        self.fee = fee
        self.till = 0
        self.favourite_songs = {}
        self.playlist = {}

    def check_in_guest(self, guest):
        if guest.can_afford_entry_fee(self.fee) and not self.is_at_capacity():
            self.guests.append(guest)

    def check_out_guest(self, guest):
        self.guests.remove(guest)

    def add_song(self, song):
        self.songs.append(song)

    def is_at_capacity(self):
        return len(self.guests) == self.capacity

    def add_favourite_song(self, guest):
        if guest.favourite_song not in self.favourite_songs:
            self.favourite_songs[guest.favourite_song] = []
        self.favourite_songs[guest.favourite_song].append(guest)