import unittest
from tests.setup_test import TestSetup

class TestGuest(TestSetup):
    def test_guest_has_name(self):
        self.assertEqual("Barry", self.guest1.name)

    def test_guest_wallet(self):
        self.assertEqual(10, self.guest1.wallet)
