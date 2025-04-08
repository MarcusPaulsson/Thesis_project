import random


class MusicPlayer:
    """
    A music player class that provides functionalities to play, stop, add songs, remove songs, 
    set volume, shuffle, and switch to the next or previous song in the playlist.
    """

    def __init__(self):
        """
        Initializes the music player with an empty playlist, no current song, and a default volume of 50.
        """
        self.playlist = []
        self.current_song_index = None
        self.volume = 50

    def add_song(self, song: str):
        """
        Adds a song to the playlist.
        :param song: The song to add to the playlist, str.
        """
        self.playlist.append(song)

    def remove_song(self, song: str):
        """
        Removes a song from the playlist.
        :param song: The song to remove from the playlist, str.
        """
        if song in self.playlist:
            self.playlist.remove(song)
            if self.current_song_index is not None and self.current_song_index >= len(self.playlist):
                self.current_song_index = len(self.playlist) - 1

    def play(self):
        """
        Plays the current song in the playlist.
        :return: The current song in the playlist, or None if there is no current song.
        """
        if self.current_song_index is not None and 0 <= self.current_song_index < len(self.playlist):
            return self.playlist[self.current_song_index]
        return None

    def stop(self):
        """
        Stops the current song in the playlist.
        :return: True if the current song was stopped, False if there was no current song.
        """
        if self.current_song_index is not None:
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
            else:
                self.current_song_index = (self.current_song_index + 1) % len(self.playlist)
            return True
        return False

    def previous_song(self):
        """
        Switches to the previous song in the playlist.
        :return: True if the previous song was switched to, False if there was no previous song.
        """
        if self.playlist:
            if self.current_song_index is None:
                self.current_song_index = len(self.playlist) - 1
            else:
                self.current_song_index = (self.current_song_index - 1) % len(self.playlist)
            return True
        return False

    def set_volume(self, volume: int) -> bool:
        """
        Sets the volume of the music player, if the volume is between 0 and 100 is valid.
        :param volume: The volume to set the music player to, int.
        :return: True if the volume was set, False if the volume was invalid.
        """
        if 0 <= volume <= 100:
            self.volume = volume
            return True
        return False

    def shuffle(self) -> bool:
        """
        Shuffles the playlist.
        :return: True if the playlist was shuffled, False if the playlist was empty.
        """
        if self.playlist:
            random.shuffle(self.playlist)
            return True
        return False