import unittest
from classes.guest import Guest
from classes.song import Song
from classes.room import Room

class TestGuest(unittest.TestCase):

    def setUp(self,guest):
        self.guest = Guest("Ewelina")
        

def test_guest_has_name(self):
    
    expected = "Ewelina"
    actual = self.guest.name
    self.assertEqual(expected, actual)