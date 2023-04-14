'''
1 class implemented
* class TestPlaylist, inherited from unittest.TestCase
'''
import unittest
from playlist import UnknownSinger, UnknownTrack, Playlist, SpecialPlaylist

class TestPlaylist(unittest.TestCase):
    '''
    class TestPlaylist, inherited from unittest.TestCase
    '''
    def setUp(self):
        '''
        sets up variables
        '''
        self.playlist = Playlist()
        self.relax_playlist = SpecialPlaylist("Relax")
        self.sport_playlist = SpecialPlaylist("Sport", "Max")
        self.spotify = set()

    def test_playlist(self):
        '''
        tests class Playlist
        '''
        self.playlist.add_song("Taylor Swift", "Enchanted")
        self.assertEqual(self.playlist.view_playlist(), [("Taylor Swift", "Enchanted")])
        self.assertEqual(self.playlist.view_singer("Taylor Swift"), ["Enchanted"])
        self.playlist.delete("Taylor Swift", "Enchanted")
        self.assertEqual(self.playlist.view_playlist(), [])
        self.assertEqual(str(self.playlist), \
'You are not listening to anything in favourites playlist.')

    def test_special_playlist_set(self):
        '''
        tests class Special Playlist and tests set
        '''
        self.assertEqual(self.relax_playlist.playlist_name, "Relax")
        self.assertTrue(self.relax_playlist, SpecialPlaylist)
        self.assertTrue(self.relax_playlist, Playlist)
        self.relax_playlist.playlist_name = "Calming music"
        self.assertEqual(self.relax_playlist.playlist_name, "Calming music")
        self.relax_playlist.add_song("Lana Del Rey", "Cinnamon Girl")
        self.relax_playlist.add_song("Lana Del Rey", "Radio")
        self.assertEqual(self.relax_playlist.view_playlist(), \
[("Lana Del Rey", "Cinnamon Girl"), ("Lana Del Rey", "Radio")])
        self.assertEqual(self.relax_playlist.view_singer("Lana Del Rey"),
["Cinnamon Girl", "Radio"])
        self.relax_playlist.delete("Lana Del Rey", "Cinnamon Girl")
        self.assertEqual(self.relax_playlist.view_playlist(), [("Lana Del Rey", "Radio")])
        self.assertEqual(str(self.relax_playlist), \
'You are not listening to anything in "Calming music" playlist.')
        self.assertEqual(self.relax_playlist.get_playlist_description(),
'You can not access this playlist creator.')
        self.sport_playlist = SpecialPlaylist("Sport", "Max")
        self.assertEqual(self.sport_playlist._SpecialPlaylist__creator, "Max")
        self.assertEqual(self.sport_playlist.get_playlist_description(),
'"Sport" was created by Max.\nIt has 0 track.')
        self.relax_playlist.play("Lana Del Rey", "Radio")
        self.assertEqual(str(self.relax_playlist), 'Lana Del Rey - Radio is playing now.')
        try:
            self.relax_playlist.view_singer("Taylor Swift")
        except UnknownSinger as error:
            assert str(error) == 'Taylor Swift was not found in this playlist.'

        try:
            self.relax_playlist.play("Taylor Swift", "Enchanted")
        except UnknownTrack as error:
            assert str(error) == 'Taylor Swift - Enchanted was not found in this playlist.'

        self.assertNotIn(self.playlist, self.spotify)
        self.spotify.add(self.playlist)
        self.assertIn(self.playlist, self.spotify)
        self.spotify.add(self.relax_playlist)
        self.assertIn(self.relax_playlist, self.spotify)

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
