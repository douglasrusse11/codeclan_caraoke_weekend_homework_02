class Room:
    def __init__(self, capacity, fee):
        self.guests = []
        self.songs = []
        self.capacity = capacity
        self.fee = fee
        self.till = 0
        self.favourite_songs = {}

    def check_in_guest(self, guest):
        if guest.can_afford_entry_fee(self.fee) and not self.is_at_capacity():
            self.guests.append(guest)

    def check_out_guest(self, guest):
        self.guests.remove(guest)

    def add_song(self, song):
        self.songs.append(song)

    def is_at_capacity(self):
        return len(self.guests) == self.capacity