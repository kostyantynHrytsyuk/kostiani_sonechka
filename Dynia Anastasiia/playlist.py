'''
4 implemented classes
* class UnknownSinger, inherited from Exception
* class UnknownTrack, inherited from Exception
* class Playlist
* class SpecialPlaylist, inherited from Playlist
'''

class UnknownSinger(Exception):
    '''
    class UnknownSinger, inherited from Exception
    '''

class UnknownTrack(Exception):
    '''
    class UnknownTrack, inherited from Exception
    '''

class Playlist:
    '''
    class Playlist
    '''
    def __init__(self, lst=None) -> None:
        '''
        Lets the class initialize the object's attributes
        '''
        self.singer = None
        self.song = None
        self.playing = False
        self.lst = lst if lst is not None else []

    def add_song(self, singer_name, track_name):
        '''
        Adds song
        '''
        self.lst.append((singer_name, track_name))

    def view_playlist(self):
        '''
        Allows you to view playlist
        '''
        return self.lst

    def view_singer(self, name):
        '''
        Allows you to view singer
        '''
        lst_of_songs = []
        for i in self.lst:
            if i[0] == name:
                lst_of_songs.append(i[1])
        if len(lst_of_songs) == 0:
            raise UnknownSinger(f'{name} was not found in this playlist.')
        return lst_of_songs

    def delete(self, singer_name, track_name):
        '''
        Deletes singer and his/her track
        '''
        self.lst.remove((singer_name, track_name))

    def play(self, singer, song):
        '''
        Allows to play song
        '''
        if (singer, song) not in self.lst:
            raise UnknownTrack(f'{singer} - {song} was not found in this playlist.')
        self.singer = singer
        self.song = song
        self.playing = True

    def __str__(self):
        '''
        Returns string
        '''
        if not self.lst:
            return 'You are not listening to anything in favourites playlist.'
        return f'{self.singer} - {self.song} is playing now.'

    def __hash__(self) -> int:
        '''
        Hashes the object
        '''
        return hash(tuple(self.lst))

class SpecialPlaylist(Playlist):
    '''
    class SpecialPlaylist, inherited from Playlist
    '''
    playlist_count = 0
    def __init__(self, playlist_name, name=None, lst=None):
        '''
        Lets the class initialize the object's attributes
        '''
        super().__init__(lst)
        self.__creator = name
        SpecialPlaylist.playlist_count += 1
        self._playlist_name = playlist_name

    @property
    def playlist_name(self):
        '''
        Returns self._playlist_name
        '''
        return self._playlist_name

    @playlist_name.setter
    def playlist_name(self, playlist_name):
        '''
        Sets self._playlist_name
        '''
        self._playlist_name = playlist_name

    def __str__(self):
        '''
        Returns string
        '''
        if self.playing is False:
            return f'You are not listening to anything in "{self._playlist_name}" playlist.'
        return f'{self.singer} - {self.song} is playing now.'

    def get_playlist_description(self):
        '''
        Allows you to get a playlist description
        '''
        if self.__creator is None:
            return 'You can not access this playlist creator.'
        return f'"{self.playlist_name}" was created by \
{self.__creator}.\nIt has {len(self.lst)} tracks.' if len(self.lst) > 1\
else f'"{self.playlist_name}" was created by \
{self.__creator}.\nIt has {len(self.lst)} track.'
