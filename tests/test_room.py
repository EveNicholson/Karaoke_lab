import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Last Night", "Morgan Wallen")
        self.song_2 = Song("Fast Car", "Luke Combs")
        self.song_3 = Song("Vampire", "Olivia Rodrigo")

        self.songs = [self.song_1, self.song_2, self.song_3]

        self.ewelina = Guest("Ewelina", 20, self.song_1)
        self.philip = Guest("Philip", 15, self.song_2)
        self.dorota = Guest("Dorota", 100, self.song_3)

        self.guests = [self.ewelina, self.philip, self.dorota]

        self.jarek = Guest("Jarek", 10, self.song_2)
        self.room = Room("Music room", 3, 10)

    def test_room_has_name(self):
        self.assertEqual("Music room", self.room.name)

    def test_room_has_no_guests_at_start(self):
        self.assertEqual(0, self.room.number_of_guests())

    def test_room_has_no_songs_at_start(self):
        self.assertEqual(0, self.room.number_of_songs())

    def test_room_has_capacity(self):
        self.assertEqual(3, self.room.get_capacity())

    def test_room_till_starts_empty(self):
        self.assertEqual(0, self.room.till)

    def test_can_add_to_till(self):
        self.room.add_to_till(10)
        self.assertEqual(10, self.room.till)

    def test_can_check_in_guest(self):
        self.room.check_in_guest(self.philip)
        self.assertEqual(1, self.room.number_of_guests())

    def test_can_check_in_multiple_guests(self):
        self.room.check_in_guests(self.guests)
        self.assertEqual(3, self.room.number_of_guests())

    def test_can_check_guest_out(self):
        self.room.check_in_guest(self.philip)
        self.room.check_out_guest(self.philip)
        self.assertEqual(0, self.room.number_of_guests())

    def test_can_add_song_to_room(self):
        song = Song("Cruel Summer", "Taylor Swift")
        self.room.add_song(song)
        self.assertEqual(1, self.room.number_of_songs())

    def test_can_add_multiple_songs_to_room(self):
        self.room.add_songs(self.songs)
        self.assertEqual(3, self.room.number_of_songs())

    def test_room_has_free_spaces_equal_to_capacity_at_start(self):
        self.assertEqual(3, self.room.free_spaces())

    def test_free_spaces_goes_down_when_guest_checked_in(self):
        self.room.check_in_guest(self.philip)
        self.assertEqual(2, self.room.free_spaces())

    def test_cannot_check_in_guest_if_room_is_full(self):
        self.room.check_in_guests(self.guests)
        self.room.check_in_guest(self.jarek)
        self.assertEqual(3, self.room.number_of_guests())

    def test_cannot_check_in_multiple_guest_if_not_enough_free_space(self):
        self.room.check_in_guest(self.jarek)
        self.room.check_in_guests(self.guests)
        self.assertEqual(1, self.room.number_of_guests())

    def test_room_has_fee(self):
        self.assertEqual(10, self.room.fee)

    def test_can_check_guest_if_cannot_afford_it(self):
        self.room.check_in_guest(self.jarek)
        self.assertEqual(1, self.room.number_of_guests())
        self.assertEqual(10, self.room.till)
        self.assertEqual(0, self.jarek.cash)

    def test_cannot_check_guest_in_if_cannot_afford_it(self):
        marta = Guest("Marta", 2, self.song_1)
        self.room.check_in_guest(marta)

        self.assertEqual(0, self.room.number_of_guests())
        self.assertEqual(0, self.room.till)
        self.assertEqual(2, marta.cash)

    def test_cheers_for_guests_fave_song(self):
        self.room.check_in_guest(self.jarek)
        songs = self.songs
        self.assertEqual("Whoo Hoo!", self.room.guests[0].cheer(songs))


if __name__ == '__main__':
    unittest.main()
