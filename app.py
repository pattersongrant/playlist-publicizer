import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "playlist-read-private playlist-read-collaborative playlist-modify-private playlist-modify-public"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id="25ce207f670f461fad8166716fd46836", client_secret="*****", redirect_uri="http://localhost/"))

for x in range(10):
    results = sp.current_user_playlists(limit=50, offset=50*x)
    for idx, item in enumerate(results['items']):
        #print(str((50*x)+idx+1) + "." + item['name'])
        sp.playlist_change_details(item['id'], public=False)
        print(str((50*x)+idx+1) + "." + item['name'] + " " + str(not item['public']))
