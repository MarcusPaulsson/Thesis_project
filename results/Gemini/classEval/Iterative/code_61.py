import random

class MusicPlayer:
    """
    A class representing a music player.
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
        :param song: The song to add to the playlist (string).
        """
        if isinstance(song, str):
            self.playlist.append(song)
        else:
            raise TypeError("Song must be a string.")

    def remove_song(self, song):
        """
        Removes a song from the playlist.
        :param song: The song to remove from the playlist (string).
        """
        try:
            self.playlist.remove(song)
            if self.current_song == song:
                self.stop()
        except ValueError:
            print(f"Song '{song}' not found in playlist.")

    def play(self, song=None):
        """
        Plays a specific song or resumes the current song.
        :param song: The song to play (string, optional). If None, resumes the current song.
        :return: True if playback started, False otherwise.
        """
        if song:
            if song in self.playlist:
                self.current_song = song
                self.is_playing = True
                return True
            else:
                print(f"Song '{song}' not found in playlist.")
                return False
        elif self.current_song:
            self.is_playing = True
            return True
        else:
            if self.playlist:
                self.current_song = self.playlist[0]
                self.is_playing = True
                return True
            else:
                print("Playlist is empty.")
                return False

    def stop(self):
        """
        Stops the current song.
        :return: True if the song was stopped, False otherwise.
        """
        if self.is_playing:
            self.is_playing = False
            return True
        else:
            return False

    def switch_song(self):
        """
        Switches to the next song in the playlist.
        :return: True if a song was switched to, False otherwise.
        """
        if not self.playlist:
            print("Playlist is empty.")
            return False

        if not self.current_song:
            return self.play()

        try:
            current_index = self.playlist.index(self.current_song)
            next_index = (current_index + 1) % len(self.playlist)
            self.current_song = self.playlist[next_index]
            self.is_playing = True
            return True
        except ValueError:  # Should not happen if current_song is managed correctly
            return self.play()

    def previous_song(self):
        """
        Switches to the previous song in the playlist.
        :return: True if a song was switched to, False otherwise.
        """
        if not self.playlist:
            print("Playlist is empty.")
            return False

        if not self.current_song:
            return self.play()

        try:
            current_index = self.playlist.index(self.current_song)
            previous_index = (current_index - 1) % len(self.playlist)
            self.current_song = self.playlist[previous_index]
            self.is_playing = True
            return True
        except ValueError:  # Should not happen if current_song is managed correctly
            return self.play()

    def set_volume(self, volume):
        """
        Sets the volume of the music player.
        :param volume: The volume to set (integer between 0 and 100).
        :return: True if the volume was set, False otherwise.
        """
        if isinstance(volume, int) and 0 <= volume <= 100:
            self.volume = volume
            return True
        else:
            print("Invalid volume. Volume must be an integer between 0 and 100.")
            return False

    def shuffle(self):
        """
        Shuffles the playlist.
        :return: True if the playlist was shuffled, False otherwise.
        """
        if self.playlist:
            random.shuffle(self.playlist)
            return True
        else:
            print("Playlist is empty.")
            return False

    def get_current_song(self):
        """
        Returns the currently playing song.
        :return: The current song (string) or None if no song is playing.
        """
        return self.current_song

    def get_playlist(self):
        """
        Returns a copy of the current playlist.
        :return: A list of strings representing the playlist.
        """
        return self.playlist[:] # Return a copy to prevent external modification

    def is_currently_playing(self):
        """
        Returns the playing status
        :return: boolean
        """
        return self.is_playing