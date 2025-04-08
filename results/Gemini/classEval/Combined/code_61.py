import random

class MusicPlayer:
    """
    A music player class that manages a playlist, current song, and volume.
    """

    def __init__(self):
        """
        Initializes the music player with an empty playlist, no current song, and a default volume of 50.
        """
        self.playlist = []
        self.current_song = None
        self.volume = 50
        self.current_index = None

    def add_song(self, song):
        """Adds a song to the playlist."""
        self.playlist.append(song)

    def remove_song(self, song):
        """Removes a song from the playlist if it exists."""
        if song in self.playlist:
            self.playlist.remove(song)
            if self.current_song == song:
                self.current_song = None
                self.current_index = None
            elif self.current_index is not None:
                self.current_index = min(self.current_index, len(self.playlist) - 1)


    def play(self):
        """Plays the current song.  If no song is selected it plays the first song."""
        if not self.playlist:
            return False

        if self.current_song is None:
            self.current_song = self.playlist[0]
            self.current_index = 0
            return self.current_song

        if self.current_song not in self.playlist:
            self.current_song = self.playlist[0]
            self.current_index = 0
            return self.current_song

        return self.current_song


    def stop(self):
        """Stops the current song."""
        if self.current_song:
            self.current_song = None
            self.current_index = None
            return True
        return False

    def switch_song(self):
        """Switches to the next song in the playlist."""
        if not self.playlist or self.current_song is None:
            return False

        if self.current_index is None:
            return False

        if self.current_index < len(self.playlist) - 1:
            self.current_index += 1
            self.current_song = self.playlist[self.current_index]
            return True
        return False


    def previous_song(self):
        """Switches to the previous song in the playlist."""
        if not self.playlist or self.current_song is None:
            return False

        if self.current_index is None:
            return False

        if self.current_index > 0:
            self.current_index -= 1
            self.current_song = self.playlist[self.current_index]
            return True
        return False

    def set_volume(self, volume):
        """Sets the volume if it's within the valid range (0-100)."""
        if 0 <= volume <= 100:
            self.volume = volume
            return None
        return False

    def shuffle(self):
        """Shuffles the playlist."""
        if self.playlist:
            random.shuffle(self.playlist)
            if self.current_song:
                try:
                    self.current_index = self.playlist.index(self.current_song)
                except ValueError:
                    self.current_index = None
                    self.current_song = None
            return True
        return False