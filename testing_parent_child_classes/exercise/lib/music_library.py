# File: lib/music_library.py

class MusicLibrary:
    # Public properties:
    #   tracks: a list of instances of Track

    def __init__(self):
        self.tracks = []

    def add(self, track):
        
        self.tracks.append(track)

    def search(self, keyword):
        # keyword is a string
        # Returns a list of instances of track that match the keyword
        matching_tracks = []
        for track in self.tracks:
            if track.matches(keyword) == True:
                matching_tracks.append(track)
        return matching_tracks