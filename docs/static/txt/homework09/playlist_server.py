#!/usr/bin/env python3

import json
import logging
import sys

from vial import Vial

# Constants

try:
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
except IndexError:
    print(f'Usage: {sys.argv[0]} HOST PORT', file=sys.stderr)
    sys.exit(1)

# Globals

App = Vial(HOST, PORT)
Playlists: dict[int, dict] = {}

# Handlers

@App.route('/')
def index(request):
    return '''
METHOD  ENDPOINT                        DESCRIPTION

POST    /playlist                       Create Playlist

        -> {"name": str}
        <- {"id": int}

DELETE  /playlist/{playlist_id}         Remove Playlist

GET     /playlist/{playlist_id}         Get Playlist

        <- {"id": int, "name": str, "items": {"total": int, "items": [{"title": str, "url": str}, ...]}}

GET     /playlists/{playlist_id}/items  Get Playlist Items

        <- {"total": int, "items": [{"title": str, "url": str}, ...]}

POST    /playlists/{playlist_id}/items  Add Items to Playlist

        -> {"items": [{"title": str, "url": str}, ...], "position": int}
        <- {"total": int}

DELETE  /playlists/{playlist_id}/items  Remove Items from Playlist

        -> {"items": [{"title": str, "url": str}]}
        <- {"total": int}
'''

@App.route('/playlist', methods=['POST'])
def create_playlist(request):
    ''' Create playlist.

    Return 400 if name is not in form data.  Otherwise, create a new playlist:

    1. Generate new playlist id based on length of Playlists.

    2. Add playlist dictionary to global Playlists with the given name.

    @params {"name": str}
    @return {"id": int}
    '''
    # TODO
    pass

@App.route('') # TODO
def remove_playlist(request, playlist_id):
    ''' Remove playlist specified by playlist_id.

    Return 404 if playlist_id is invalid.  Otherwise, remove the specified
    playlist by setting the corresponding playlist to an empty dictionary.
    '''
    # TODO
    pass

@App.route('') # TODO
def get_playlist(request, playlist_id):
    ''' Get playlist specified by playlist_id.

    Return 404 if playlist_id is invalid.  Otherwise, return the specified
    playlist information.

    @return     {"id": int, "name": str,
                 "items": {"total": int, "items": [{"title": str, "url": str}, ...]}}
    '''
    # TODO
    pass

@App.route('') # TODO
def get_playlist_items(request, playlist_id):
    ''' Get playlist items specified by playlist_id.

    Return 404 if playlist_id is invalid.  Otherwise, return the specified
    playlist items.

    @return {"total": int, "items": [{"title": str, "url": str}, ...]}
    '''
    # TODO
    pass

@App.route('') # TODO
def add_playlist_items(request, playlist_id):
    ''' Add items to playlist specified by playlist_id.

    Return 404 if playlist_id is invalid.  Otherwise, add the specified items
    in the form data to the existing playlist at the specified position and
    then return the new total number of items.

    @params {"items": [{"title": str, "url": str}, ...], "position": int}
    @return {"total": int}
    '''
    # TODO
    pass

@App.route('') # TODO
def remove_playlist_items(request, playlist_id):
    ''' Delete items from playlist specified by playlist_id.

    Return 404 if playlist_id is invalid.  Otherwise, remove the specified
    items in the form data from the existing playlist and then return the new
    total number of items.

    @params {"items": [{"url": str}, ...]}
    @return {"total": int}
    '''
    # TODO
    pass

# Main Execution

if __name__ == '__main__':
    App.run()
