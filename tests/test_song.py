import unittest

from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Last Night", "Morgan Wallen")

    def test_song_has_title(self):
        self.assertEqual("Last Night", self.song.title)

    def test_song_has_artist(self):
        song = Song("Last Night", "Morgan Wallen")
        self.assertEqual("Morgan Wallen", self.song.artist)

    def test_equals_returns_true(self):
        song = Song("Last Night", "Morgan Wallen")
        result = self.song.equals(song)
        self.assertEqual(True, result)

    def test_equals_title_different_returns_false(self):
        song = Song("Kill Bill", "SZA")
        result = self.song.equals(song)
        self.assertEqual(False, result)

    def test_equals_artist_different_returns_false(self):
        song = Song("Last Night", "SZA")
        result = self.song.equals(song)
        self.assertEqual(False, result)

    def test_equals_song_different_returns_false(self):
        song = Song("Vampire", "Rema")
        result = self.song.equals(song)
        self.assertEqual(False, result)

if __name__ == '__main__':
    unittest.main()
