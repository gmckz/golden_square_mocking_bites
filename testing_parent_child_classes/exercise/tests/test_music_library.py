from unittest.mock import Mock
from lib.music_library import *

"""
Given no instance of Track
tracks property returns empty list
"""
def test_no_track_instance_tracks_is_empty_list():
    music_library = MusicLibrary()
    assert music_library.tracks == []

"""
Given mock tracks added
tracks returns list of mock tracks
"""
def test_mock_tracks_added_returns_list_of_mock_tracks():
    music_library = MusicLibrary()
    fake_track_1 = Mock()
    fake_track_2 = Mock()
    music_library.add(fake_track_1)
    music_library.add(fake_track_2)
    music_library.tracks == [fake_track_1, fake_track_2]

"""
Given a keyword matching title or artist
#search returns list of tracks containing keyword
"""
def test_keyword_in_title_returns_list_of_tracks():
    music_library = MusicLibrary()

    fake_track_1 = Mock()
    fake_track_1.matches("Title").return_value = True

    fake_track_2 = Mock()
    fake_track_2.matches("Title").return_value = False

    fake_track_3 = Mock()
    fake_track_3.matches("Title").return_value = True

    music_library.search("Title") == [fake_track_1, fake_track_3]
    