class Room:
    def __init__(self):
        self.guests = []
        self.songs = []

    def check_in_guest(self, guest):
        self.guests = [guest]