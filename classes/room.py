class Room:
    def __init__(self, capacity, fee):
        self.guests = []
        self.songs = []
        self.capacity = capacity
        self.fee = fee

    def check_in_guest(self, guest):
        self.guests.append(guest)

    def check_out_guest(self, guest):
        self.guests.remove(guest)

    def add_song(self, song):
        self.songs.append(song)