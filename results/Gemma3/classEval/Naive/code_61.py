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

    def play(self):
        """
        Plays the current song in the playlist.
        :return: The current song in the playlist, or None if there is no current song.
        """
        if self.current_song:
            return self.current_song
        else:
            return None

    def stop(self):
        """
        Stops the current song in the playlist.
        :return: True if the current song was stopped, False if there was no current song.
        """
        if self.current_song:
            self.current_song = None
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

        if self.current_song:
            try:
                current_index = self.playlist.index(self.current_song)
                next_index = (current_index + 1) % len(self.playlist)
                self.current_song = self.playlist[next_index]
                return True
            except ValueError:
                return False
        else:
            if self.playlist:
                self.current_song = self.playlist[0]
                return True
            else:
                return False

    def previous_song(self):
        """
        Switches to the previous song in the playlist.
        :return: True if the previous song was switched to, False if there was no previous song.
        """
        if not self.playlist:
            return False

        if self.current_song:
            try:
                current_index = self.playlist.index(self.current_song)
                previous_index = (current_index - 1) % len(self.playlist)
                self.current_song = self.playlist[previous_index]
                return True
            except ValueError:
                return False
        else:
            if self.playlist:
                self.current_song = self.playlist[-1]
                return True
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
            return True
        else:
            return False

    def shuffle(self):
        """
        Shuffles the playlist.
        :return: True if the playlist was shuffled, False if the playlist was empty.
        """
        if self.playlist:
            random.shuffle(self.playlist)
            return True
        else:
            return False