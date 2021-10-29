class Guest:
    def __init__(self, name, wallet, favourite_song):
        self.name = name
        self.wallet = wallet
        self.favourite_song = favourite_song

    def can_afford_entry_fee(self, fee):
        return self.wallet >= fee

    def cheer(self, songs):
        return "Whoo!"