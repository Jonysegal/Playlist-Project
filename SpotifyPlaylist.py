import requests
import urllib.parse
import json
from track import Track

class Runner: 
    api_token = 'BQDPB27u3CPIESrR4mOYw2sJ1X6B0A3N-KcKr5omWOQ335DM0nGqauZShWvwg4Xwa4NrYKEh51loyEmSEQbXTxx2RLdPFIaGwoIjnM3Sqd_DfDv1kZau5d_7c-1DH8EdPSeFm96zgVobgQUpjHJDObZ2PINwqoPVk5kAlydnhel-SKLTWb6SIH_jX-XwRVux4E_E-Bgpj_BKCeCD7zzgVDtUp3ms6cztqNEtbQLzyJZl_wd7oXZtTVs7UyOS3ZTUKC2Ev80FNGErT2BwI7_CLAyZnvgU_FgdZXt8'
    user_id = 'ol0ys8y3412mh7tfh9n0lbprc'
    def search_song(self, artist, track):

        query = urllib.parse.quote(f'{artist} {track}')
        url = f"https://api.spotify.com/v1/search?q={query}&type=track"
        
        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_token}"
                }
            )
        response_json = response.json()
        
        if 'tracks' not in response_json:
            print("no tracks dum dum")
            print(response_json)
       
        results = response_json['tracks']['items']
        
        if results:
        
            print("succeeded")
            return results[0]['id']
            addUrl = "https://api.spotify.com/v1/me/tracks";
            print(addUrl)
            response2 = requests.put(addUrl, 
                json={"ids": [id]},
                headers={"Content-Type": "application/json",
                    "Authorization": f"Bearer {self.api_token}"
                    }
                )
            print(response2.ok)
        else:
            print("fuck")  

    def add_song_to_playlist(self, trackId, playlistId):
        url = "https://api.spotify.com/v1/playlists/" + playlistId + "/tracks?uris=spotify:track:" + trackId
        
        response = requests.post(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_token}"
                }
            )
        if not response.ok:
            print("adding song to playlist failed FUCK")
            print(response.json())
    def get_playlists(self):
        url = "https://api.spotify.com/v1/me/playlists"
        response = requests.get(
            url,
            headers={"Authorization": f"Bearer {self.api_token}"
                }
            )
        if not response.ok:
            print("couldn't get playlists")
            print(response.json())
        return response.json().get('items')
    def get_tracks_in_playlist(self, playlist):
        #note: can only get max of 100 items, but allowed to give an offset
        #therefore can iterate over full playlist by just popping up 100 in the offset until full thing is read
        #obviously will have to contain it or whatever
        toReturn = []
        playlist_id = playlist.get('id')
        url = "https://api.spotify.com/v1/playlists/{}/tracks".format(playlist_id)
        offset = 0
        playlistCount = playlist.get('tracks').get('total')
        while offset < playlistCount:
            offsetUrl = url + "?offset={}".format(offset)
            response = requests.get(
                offsetUrl,
                headers={"Authorization": f"Bearer {self.api_token}"
                    }
                )
            if not response.ok:
                print("somethign went wrong reading stuff")
            else:
                for track in response.json().get('items'):
                    print("just added {}".format(track.get('track').get('name')))
                    toReturn.append(Track(track.get('track').get('id'), track.get('track').get('name')))
                    
            offset += 100
        return toReturn
        
    def make_new_playlist_called(self, name):
        url= "https://api.spotify.com/v1/users/{}/playlists".format(self.user_id)
        request_body = json.dumps({
            "name": name
            })
        response = requests.post(
            url, 
            headers={"Authorization": f"Bearer {self.api_token}"
                },
            data=request_body           
            )
        if not response.ok:
            print("couldn't make playlist called {}".format(name))
            print(response.json())
               