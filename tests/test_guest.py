import unittest

from classes.guest import Guest
from classes.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Last Night", "Morgan Wallen")
        self.song_2 = Song("Fast Car", "Luke Combs")
        self.song_3 = Song("Vampire", "Olivia Rodrigo")

        self.songs = [self.song_1, self.song_2, self.song_3]

        song = Song("Vampire", "Oliwia")
        self.guest = Guest("Ewelina", 50, song)

    def test_guest_has_name(self):
        self.assertEqual("Ewelina", self.guest.name)

    def test_guest_has_cash(self):
        self.assertEqual(50, self.guest.cash)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Vampire", self.guest.favourite_song.title)

    def test_guest_can_change_favourite_song(self):
        song = Song("Calm Down", "Rema")
        self.guest.favourite_song = song
        self.assertEqual("Calm Down", self.guest.favourite_song.title)

    def test_guest_can_afford_10(self):
        self.assertEqual(True, self.guest.can_afford(10))

    def test_guest_can_afford_20(self):
        self.assertEqual(True, self.guest.can_afford(20))

    def test_guest_cannot_afford_60(self):
        self.assertEqual(False, self.guest.can_afford(60))

    def test_guest_can_pay_amount(self):
        self.guest.pay(10)
        self.assertEqual(40, self.guest.cash)

    def test_guest_cheers_when_fave_song_in_list(self):
        result = self.guest.cheer(self.songs)
        self.assertEqual("Whoo Hoo!", result)

    def test_guest_does_not_cheers_when_fave_song_not_in_list(self):
        song = Song("Flowers", "Miley Cyrus")
        guest = Guest("Marta", 2, song)
        self.assertEqual(None, guest.cheer(self.songs))

if __name__ == '__main__':
    unittest.main()
