"""
Module for playlist
"""
class UnknownSinger(Exception):
    pass
class UnknownTrack(Exception):
    pass

class Playlist:

    """playlist class"""
    def __init__(self) -> None:
        self.playlist = []
        self.artist = ''
        self.song = ''
        self.play_song = None

    def __str__(self) -> str:
        """info about playlist"""
        if self.playlist:
            return f'{self.artist} - {self.song} is playing now.'
        return 'You are not listening to anything in favourites playlist.'

    def add_song(self, artist, song):
        """add song"""
        self.artist = artist
        self.song = song
        self.playlist.append((artist, song))

    def view_playlist(self):
        """return playlist"""
        return self.playlist

    def view_singer(self, singer):
        """return playlist"""
        result = []
        for i in self.playlist:
            if i[0] == singer:
                result.append(i[1])
        if result:
            return result
        else:
            raise UnknownSinger(f'{singer} was not found in this playlist.')

    def delete(self, artist, song):
        """delete artist"""
        self.playlist.remove((artist, song))

    def play(self, artist_name, song_name):
        """playing playlist"""
        if (artist_name, song_name) not in self.playlist:
            raise UnknownTrack(f'{artist_name} - {song_name} was not found in this playlist.')
        self.play_song = (artist_name, song_name)

    def __hash__(self) -> int:
        """
        Function for hash
        """
        return id(str(self))

class SpecialPlaylist(Playlist):
    """class for our own playlists"""

    playlist_count = 0

    def __init__(self, playlist_name, creator=None) -> None:
        super().__init__()
        self._playlist_name = playlist_name
        self.__creator = creator
        SpecialPlaylist.playlist_count += 1

    def set_name(self, name):
        """set"""
        self._playlist_name = name

    def get_name(self):
        """get"""
        return self._playlist_name

    def __str__(self) -> str:
        """info about playlist"""
        if self.play_song:
            return f'{self.play_song[0]} - {self.play_song[1]} is playing now.'
        return f'You are not listening to anything in "{self._playlist_name}" playlist.'

    def get_playlist_description(self):
        """description of playlist"""
        if self.__creator is None:
            return 'You can not access this playlist creator.'
        right_pos = 'tracks'
        if len(self.playlist) == 1:
            right_pos = 'track'
        return f'"{self._playlist_name}" was created by {self.__creator}.\
\nIt has {len(self.playlist)} {right_pos}.'

    playlist_name = property(get_name, set_name)
