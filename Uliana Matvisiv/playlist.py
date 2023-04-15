class UnknownSinger(Exception):
    """Class for unknown
    singer error"""
    pass
class UnknownTrack(Exception):
    """Class for unknown
    track error"""
    pass
class Playlist:
    """Class for working with playlist"""
    def __init__(self):
        """Method to initialize the object's attributes"""
        self.playlist = []
        self.playlist1 = {}
        self.artist = None
        self.song = None
        self.play_song = False
    def view_singer(self, artist):
        """Method to view songs of certain artist"""
        if artist in self.playlist1:
            return self.playlist1[artist]
        else:
            raise UnknownSinger(f'{artist} was not found in this playlist.')
    def add_song(self, artist, song):
        """Method to add song to playlist"""
        self.playlist.append((artist, song))
        if artist in self.playlist1:
            self.playlist1[artist] += [song]
        else:
            self.playlist1[artist] = [song]
    def view_playlist(self):
        """Method to view playlist"""
        return self.playlist
    def delete(self, artist, song):
        """Method to delete song from playlist"""
        self.playlist.remove((artist, song))
        self.playlist1[artist].remove(song)
    def play(self, artist_name, song_name):
        """Method to play song"""
        if (artist_name, song_name) not in self.playlist:
            raise UnknownTrack(f'{artist_name} - {song_name} was not found in this playlist.')
        self.play_song = True
        self.artist = artist_name
        self.song = song_name
    def __str__(self):
        """Method for string representation."""
        if len(self.playlist) == 0:
            return 'You are not listening to anything in favourites playlist.'
        else:
            return f'{self.playlist[-1][0]} - {self.playlist[-1][1]} is playing now.'
    def __hash__(self) -> int:
        return hash(tuple(self.playlist))
   
class SpecialPlaylist(Playlist):
    """Class to create a special playlist"""
    playlist_count = 0
    def __init__(self, name, creator=None):
        """Method to initialize the object's attributes"""
        super().__init__()
        self._playlist_name = name
        self.__creator = creator
        SpecialPlaylist.playlist_count += 1
    @property
    def playlist_name(self):
        """Returns playlist name"""
        return self._playlist_name
    @playlist_name.setter
    def playlist_name(self, playlist_name):
        """Sets playlist name"""
        self._playlist_name = playlist_name
    def __str__(self):
        """Method for string representation."""
        if self.play_song:
            if self.playlist:
                return f'{self.artist} - {self.song} is playing now.'
        return f'You are not listening to anything in "{self.playlist_name}" playlist.'
    def get_playlist_description(self):
        """Method to describe playlist"""
        track = 'tracks'
        if self.__creator:
            if len(self.playlist) == 1:
                track = "track"
            return f'"{self.playlist_name}" was created by {self.__creator}.\
\nIt has {len(self.playlist)} {track}.'
        return f'You can not access this playlist creator.'
