"""Importing modules"""
import unittest
from playlist import *

class TestPlaylist(unittest.TestCase):
    """Class for testing"""
    def setUp(self):
        """Setting up"""
        self.playlist = Playlist()
        self.party_playlist = SpecialPlaylist("Party")
        self.travel_playlist = SpecialPlaylist("Travel", "Sam")
        self.spotify = set()
    def test_playlist(self):
        """Testing simple playlist"""
        self.playlist.add_song("The Academic", "Not your summer")
        self.assertEqual(self.playlist.view_playlist(), [("The Academic", "Not your summer")])
        self.playlist.add_song("Half*alive", "Did I Make You Up")
        self.assertEqual(self.playlist.view_playlist(), [("The Academic", "Not your summer"),
                                                         ("Half*alive", "Did I Make You Up")])
        self.assertEqual(self.playlist.view_singer("The Academic"), ["Not your summer"])
        self.playlist.delete("Half*alive", "Did I Make You Up")
        self.assertEqual(self.playlist.view_playlist(), [("The Academic", "Not your summer")])
        self.assertEqual(str(self.playlist), 'The Academic - Not your summer is playing now.')
        self.playlist.delete("The Academic", "Not your summer")
        self.assertEqual(str(self.playlist),
                         'You are not listening to anything in favourites playlist.')
        self.playlist.add_song("The Academic", "Not your summer")
        self.playlist.add_song('The Academic', 'My Very Best')
        self.assertEqual(self.playlist.view_playlist(),
                         [("The Academic", "Not your summer"), ('The Academic', 'My Very Best')])
    def test_special_playlist(self):
        """Testing special playlists"""
        self.assertEqual(self.party_playlist.playlist_name, "Party")
        self.assertTrue(self.party_playlist, SpecialPlaylist)
        self.assertTrue(self.party_playlist, Playlist)
        self.party_playlist.add_song("Twenty one pilots", "Saturday")
        self.party_playlist.play("Twenty one pilots", "Saturday")
        self.assertEqual(str(self.party_playlist), "Twenty one pilots - Saturday is playing now.")
        self.party_playlist.playlist_name = "Fun"
        self.assertEqual(self.party_playlist.playlist_name, "Fun")
        self.party_playlist.add_song("Melanie Martinez", "Carousel")
        self.assertEqual(self.party_playlist.view_playlist(),
                         [("Twenty one pilots", "Saturday"), ("Melanie Martinez", "Carousel")])
        self.assertEqual(self.party_playlist.view_singer("Melanie Martinez"), ["Carousel"])
        self.party_playlist.delete("Twenty one pilots", "Saturday")
        self.party_playlist.delete("Melanie Martinez", "Carousel")
        self.assertEqual(str(self.party_playlist),
                         'You are not listening to anything in "Fun" playlist.')
        self.assertEqual(self.party_playlist.get_playlist_description(),
                         'You can not access this playlist creator.')
        self.assertEqual(self.travel_playlist.get_playlist_description(),
                         '"Travel" was created by Sam.\nIt has 0 tracks.')
        self.assertEqual(self.travel_playlist._SpecialPlaylist__creator, "Sam")
        self.travel_playlist.add_song("Twenty one pilots", "Car radio")
        self.assertEqual(self.travel_playlist.get_playlist_description(),
                         '"Travel" was created by Sam.\nIt has 1 track.')
        try:
            self.travel_playlist.view_singer("Portugal.The Man")
        except UnknownSinger as error:
            self.assertEqual(str(error), 'Portugal.The Man was not found in this playlist.')
        try:
            self.party_playlist.play("Fun", "Some nights")
        except UnknownTrack as error:
            self.assertEqual(str(error), 'Fun - Some nights was not found in this playlist.')
    def test_spotify(self):
        """Testing spotify platform"""
        self.assertNotIn(self.playlist, self.spotify)
        self.spotify.add(self.playlist)
        self.spotify.add(self.party_playlist)
        self.assertIn(self.playlist, self.spotify)
        self.assertIn(self.party_playlist, self.spotify)
        self.assertNotIn(self.travel_playlist, self.spotify)

if __name__ == '__main__':
    unittest.main()
