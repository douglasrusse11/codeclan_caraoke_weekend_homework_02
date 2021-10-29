class Guest:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def can_afford_entry_fee(self, fee):
        return True