import random

class MusicPlayer:
    """
    A simple music player class with basic functionalities.
    """

    def __init__(self):
        """
        Initializes the music player with an empty playlist, no current song, and a default volume of 50.
        """
        self.playlist = []
        self.current_song = None
        self.volume = 50
        self.is_playing = False

    def add_song(self, song):
        """
        Adds a song to the playlist.

        Args:
            song (str): The song to add.
        """
        if isinstance(song, str) and song:
            self.playlist.append(song)

    def remove_song(self, song):
        """
        Removes a song from the playlist.

        Args:
            song (str): The song to remove.
        """
        if isinstance(song, str) and song in self.playlist:
            self.playlist.remove(song)
            if self.current_song == song:
                self.current_song = None
                self.is_playing = False

    def play(self):
        """
        Plays the current song. If no song is currently selected, plays the first song in the playlist.

        Returns:
            str: The song being played, or None if the playlist is empty.
        """
        if not self.playlist:
            return None

        if self.current_song is None:
            self.current_song = self.playlist[0]

        self.is_playing = True
        return self.current_song

    def stop(self):
        """
        Stops the currently playing song.

        Returns:
            bool: True if a song was stopped, False otherwise.
        """
        if self.is_playing:
            self.is_playing = False
            return True
        return False

    def switch_song(self):
        """
        Switches to the next song in the playlist.

        Returns:
            bool: True if successfully switched to the next song, False otherwise.
        """
        if not self.playlist:
            return False

        if self.current_song is None:
            return False

        try:
            current_index = self.playlist.index(self.current_song)
            next_index = (current_index + 1) % len(self.playlist)
            self.current_song = self.playlist[next_index]
            self.is_playing = True
            return True
        except ValueError:
            return False

    def previous_song(self):
        """
        Switches to the previous song in the playlist.

        Returns:
            bool: True if successfully switched to the previous song, False otherwise.
        """
        if not self.playlist:
            return False

        if self.current_song is None:
            return False

        try:
            current_index = self.playlist.index(self.current_song)
            previous_index = (current_index - 1) % len(self.playlist)
            self.current_song = self.playlist[previous_index]
            self.is_playing = True
            return True
        except ValueError:
            return False

    def set_volume(self, volume):
        """
        Sets the volume of the music player.

        Args:
            volume (int): The desired volume (0-100).

        Returns:
            None
        """
        if isinstance(volume, int) and 0 <= volume <= 100:
            self.volume = volume
        else:
            return False

    def shuffle(self):
        """
        Shuffles the playlist.

        Returns:
            bool: True if the playlist was shuffled, False if the playlist was empty.
        """
        if self.playlist:
            random.shuffle(self.playlist)
            return True
        return False