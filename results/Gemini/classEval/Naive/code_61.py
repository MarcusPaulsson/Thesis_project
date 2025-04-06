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
        if isinstance(song, str):
            self.playlist.append(song)

    def remove_song(self, song):
        """
        Removes a song from the playlist.
        :param song: The song to remove from the playlist, str.
        """
        if isinstance(song, str) and song in self.playlist:
            self.playlist.remove(song)
            if self.current_song == song:
                self.current_song = None
                self.current_song_index = None
            elif self.current_song_index is not None and self.playlist and self.current_song_index >= len(self.playlist):
                 self.current_song_index = len(self.playlist) - 1
                 self.current_song = self.playlist[self.current_song_index]

    def play(self):
        """
        Plays the current song in the playlist.
        :return: The current song in the playlist, or False if there is no current song.
        """
        if self.playlist:
            if self.current_song is None:
                self.current_song = self.playlist[0]
                self.current_song_index = 0
            return self.current_song
        return False

    def stop(self):
        """
        Stops the current song in the playlist.
        :return: True if the current song was stopped, False if there was no current song.
        """
        if self.current_song:
            self.current_song = None
            self.current_song_index = None
            return True
        return False

    def switch_song(self):
        """
        Switches to the next song in the playlist.
        :return: True if the next song was switched to, False if there was no next song.
        """
        if self.playlist:
            if self.current_song_index is None:
                self.current_song_index = 0
                self.current_song = self.playlist[0]
                return True
            else:
                next_index = (self.current_song_index + 1) % len(self.playlist)
                self.current_song_index = next_index
                self.current_song = self.playlist[next_index]
                return True
        return False

    def previous_song(self):
        """
        Switches to the previous song in the playlist.
        :return: True if the previous song was switched to, False if there was no previous song.
        """
        if self.playlist:
            if self.current_song_index is None:
                self.current_song_index = 0
                self.current_song = self.playlist[0]
                return True
            else:
                previous_index = (self.current_song_index - 1) % len(self.playlist)
                self.current_song_index = previous_index
                self.current_song = self.playlist[previous_index]
                return True
        return False

    def set_volume(self, volume):
        """
        Sets the volume of the music player,ifthe volume is between 0 and 100 is valid.
        :param volume: The volume to set the music player to,int.
        :return: True if the volume was set, False if the volume was invalid.
        """
        if isinstance(volume, int) and 0 <= volume <= 100:
            self.volume = volume
            return True
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
                    self.current_song_index = None
                    self.current_song = None
            return True
        return False