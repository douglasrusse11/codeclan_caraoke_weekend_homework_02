class Guest:
    def __init__(self, name, wallet, favourite_song):
        """Initialise Guest object"""
        self.name = name
        self.wallet = wallet
        self.favourite_song = favourite_song

    def can_afford_entry_fee(self, fee):
        """Return True if wallet is greater than or equal to fee, otherwise False"""
        return self.wallet >= fee

    def cheer(self, songs):
        """Return "Whoo!" if favourite_song is in List songs"""
        if self.favourite_song in songs:
            return "Whoo!"

    def pay_fee(self, fee):
        """Decrement wallet by fee"""
        self.wallet -= fee