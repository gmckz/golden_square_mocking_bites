from lib.music_library import *
from lib.track import *

"""
Given 2 tracks added
tracks returns list of the 2 tracks
"""
def test_2_tracks_added_tracks_returns_list():
    music_library = MusicLibrary()
    track1 = Track("Title 1", "Artist 1")
    track2 = Track("Title 2", "Artist 2")
    music_library.add(track1)
    music_library.add(track2)
    assert music_library.tracks == [track1, track2]

"""
Given a keyword,
#search returns list of instances of track containing keyword
"""
def test_search_returns_tracks_containing_keyword():
    music_library = MusicLibrary()
    track1 = Track("Title 1", "Artist 1")
    track2 = Track("Title 2", "Artist 2")
    music_library.add(track1)
    music_library.add(track2)
    assert music_library.search("Title 1") == [track1]
    assert music_library.search("Title") == [track1, track2]
    assert music_library.search("Artist") == [track1, track2]
    assert music_library.search("Artist 2") == [track2]


