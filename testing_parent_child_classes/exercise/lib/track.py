# File: lib/track.py

class Track:
    def __init__(self, title, artist):
        self._title = title
        self._artist = artist
        pass

    def matches(self, keyword):
        # keyword is a string
        # Returns true if the keyword matches either the title or artist
        if keyword in self._title or keyword in self._artist:
            return True
        else:
            return False