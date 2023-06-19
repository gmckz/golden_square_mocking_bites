from lib.track import Track

"""
Initialising track sets instance variables title and artist
"""

def test_initialising_track_sets_title_and_artist():
    track = Track("My Title", "My Artist")
    assert track._title == "My Title"
    assert track._artist == "My Artist"

"""
Given keyword "My Title" 
#matches returns True
"""
def test_keyword_my_title_returns_true():
    track = Track("My Title", "My Artist")
    assert track.matches("My Title") == True

"""
Given keyword same as artist 
#matches returns True
"""
def test_keyword_my_artist_returns_true():
    track = Track("My Title", "My Artist")
    assert track.matches("My Artist") == True

"""
Given keyword "fake"
#matches returns False
"""
def test_matches_returns_False_with_fake_title():
    track = Track("My Title", "My Artist")
    assert track.matches("Fake") == False
