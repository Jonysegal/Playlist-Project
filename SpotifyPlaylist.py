import requests
import urllib.parse
import json

class Runner: 
    api_token = 'BQBoow3WkJs7TLb8xR_NVG6lWzny9Jx-Zl3BcIl255tiWlnZwYARMKqgOTjUOKqiN6JxxaKqx8w0-COEHlN2ocKrTzaBBrfhTHfQ5WLk16K4rRkKVWDTErGwuaAXXxw1IFV9l1lxa_zeWi4Wf1_PkPkTZywI8z1QAZxqDlaiqZl63ZiArBvIkxxx78yYdkjYyNvsPwFHD5OCTPrnzyEMp7Uiz62s9ulAwaKTX9tXGBBz6cEs31HnVFUNYVoTloHBMsWi6GgHo7ZiGVIts5NGSVhioZKgj41hjKT6'
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
        return response.json().get('items')
    def read_playlist(self, playlist_id):
        #note: can only get max of 100 items, but allowed to give an offset
        #therefore can iterate over full playlist by just popping up 100 in the offset until full thing is read
        #obviously will have to contain it or whatever
        url = "https://api.spotify.com/v1/playlists/{}/tracks".format(playlist_id)
        print("url is " + url)
        response = requests.get(
            url,
            headers={"Authorization": f"Bearer {self.api_token}"
                }
            )
        
        for x in response.json().get('items'):
            print(x.get('track').get('name'))
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
               