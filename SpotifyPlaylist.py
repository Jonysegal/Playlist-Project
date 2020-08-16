import requests
import urllib.parse
import json

class Runner: 
    api_token = 'BQB3beJKtsOCWFVP8EgSsyiFOMJ6NyY1pE-Rz4Ff0zdtFOkuKzqITF3WcshWygOriyoVpDexXGA-WjqC5OIaH6m8reZHtg8rXGxRdPb6RTmGmfTDpKiTDfHItujwHMbO-4cIZf20zSaLERy-xVNNPqJNxEgrPwGkdEAVtaLVQxCiNlzcGrDvLzeELd6s-LduSA9X54actrPk7gxxKj6Q1dn088_hpVCQO1YoJxz7XlCHYGjcwQCXPX9oGo69kGFC1XsRtaPLVqAwEb46kN7STKe2B6oXQ3OUMEQt'
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
    def print_playlists(self):
        url = "https://api.spotify.com/v1/me/playlists"
        response = requests.get(
            url,
            headers={"Authorization": f"Bearer {self.api_token}"
                }
            )
        print("printing playlists")
        for x in response.json().get('items'):
            print(x.get('name') + " " + x.get('id'))
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(response.json().get('items')[10].get('name'))
        return response.json().get('items')[10].get('id')
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
               
        
        
            
print("Not feeling great, I wish I was more important/ special to her")

runner1 = Runner();
runner1.make_new_playlist_called("YIZZLE IN THE TIZZLE")
#runner1.search_song('Peter Gabriel', 'Modern Love')
#runner1.add_song_to_playlist(runner1.search_song('Glass Animals', 'Life Itself'), '6hghRBZ4RJYyE5U7Pp4Ga5')
#runner1.read_playlist(runner1.print_playlists())
