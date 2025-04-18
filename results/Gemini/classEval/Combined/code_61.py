import random

class MusicPlayer:
    """
    This is a class as a music player that provides to play, stop, add songs, remove songs, set volume, shuffle, and switch to the next or previous song.
    """

    def __init__(self):
        """
        Initializes the music player with an empty playlist, no current song, and a default volume of 50.
        """
        self.playlist = []
        self.current_song = None
        self.volume = 50
        self.current_song_index = None

    def add_song(self, song):
        """
        Adds a song to the playlist.
        :param song: The song to add to the playlist, str.
        """
        self.playlist.append(song)

    def remove_song(self, song):
        """
        Removes a song from the playlist.
        :param song: The song to remove from the playlist, str.
        """
        if song in self.playlist:
            self.playlist.remove(song)
            if self.current_song == song:
                self.current_song = None
                self.current_song_index = None
            elif self.current_song_index is not None:
                if song in self.playlist:
                    pass
                else:
                    self.current_song_index = None
                    self.current_song = None

    def play(self):
        """
        Plays the current song in the playlist.
        :return: The current song in the playlist, or False if there is no current song.
        """
        if self.current_song:
            return self.current_song
        elif self.playlist:
            if self.current_song is None:
                if len(self.playlist) > 0:
                    return False
        else:
            return None

    def stop(self):
        """
        Stops the current song in the playlist.
        :return: True if the current song was stopped, False if there was no current song.
        """
        if self.current_song:
            self.current_song = None
            self.current_song_index = None
            return True
        else:
            return False

    def switch_song(self):
        """
        Switches to the next song in the playlist.
        :return: True if the next song was switched to, False if there was no next song.
        """
        if not self.playlist:
            return False

        if self.current_song is None and self.playlist:
            return False

        if self.current_song_index is None and self.current_song is not None:
            try:
                self.current_song_index = self.playlist.index(self.current_song)
            except ValueError:
                return False

        if self.current_song_index is None and self.current_song is None:
            return False

        if self.current_song_index is not None:
            if self.current_song_index < len(self.playlist) - 1:
                self.current_song_index += 1
                self.current_song = self.playlist[self.current_song_index]
                return True
            else:
                return False
        else:
            return False

    def previous_song(self):
        """
        Switches to the previous song in the playlist.
        :return: True if the previous song was switched to, False if there was no previous song.
        """
        if not self.playlist:
            return False

        if self.current_song is None and self.playlist:
            return False

        if self.current_song_index is None and self.current_song is not None:
            try:
                self.current_song_index = self.playlist.index(self.current_song)
            except ValueError:
                return False

        if self.current_song_index is None and self.current_song is None:
            return False

        if self.current_song_index is not None:
            if self.current_song_index > 0:
                self.current_song_index -= 1
                self.current_song = self.playlist[self.current_song_index]
                return True
            else:
                return False
        else:
            return False

    def set_volume(self, volume):
        """
        Sets the volume of the music player,ifthe volume is between 0 and 100 is valid.
        :param volume: The volume to set the music player to,int.
        :return: True if the volume was set, False if the volume was invalid.
        """
        if 0 <= volume <= 100:
            self.volume = volume
        else:
            return False

    def shuffle(self):
        """
        Shuffles the playlist.
        :return: True if the playlist was shuffled, False if the playlist was empty.
        """
        if self.playlist:
            random.shuffle(self.playlist)
            if self.current_song:
                try:
                    self.current_song_index = self.playlist.index(self.current_song)
                except ValueError:
                    self.current_song = None
                    self.current_song_index = None
            return True
        else:
            return False