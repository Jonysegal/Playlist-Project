import requests
import urllib.parse
import json
from track import Track


class Runner:
    api_token = "BQAwBkPt933N2-fCf-mypOmidzYM5h2TJn2jR8FiZzGwNaXTbNb-41XYyAFGW1n1oitu8KWejpSZEGK52hvHaEZONP2nSNRb2tG5FVZ0CtKnPrMv321RyFLfVGR0Aq8rBUZfmdnRz-Djb0PN9XYnngqOUwuu1FeAN58oDylIj8nZlUQjPLpSxXDQNLdHCnZrgUwsbwbDZkz0-TCZXzCj2qKWJuNot-ovtufTDicg6NoSIUdYWjVBxdy1jB4jUayC_Y-aLx9gNFGhBIRRw-wgWcL5Vdqj784fmIE1"
    user_id = "ol0ys8y3412mh7tfh9n0lbprc"

    def search_song(self, artist, track):

        query = urllib.parse.quote(f"{artist} {track}")
        url = f"https://api.spotify.com/v1/search?q={query}&type=track"

        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_token}",
            },
        )
        response_json = response.json()
        if "tracks" not in response_json:
            print("no tracks found for song {} and artist {}".format(artist, track))
            print(response_json)
            return -1

        results = response_json["tracks"]["items"]

        if results:
            trackJson = results[0]
            return Track(trackJson.get("id"), trackJson.get("duration_ms"), trackJson.get("name"))
        else:
            print("no results for some reason")
            return -1

    def get_playlists(self):
        url = "https://api.spotify.com/v1/me/playlists"
        response = requests.get(
            url, headers={"Authorization": f"Bearer {self.api_token}"}
        )
        if not response.ok:
            print("couldn't get playlists")
            print(response.json())
        return response.json().get("items")

    def get_tracks_in_playlist(self, playlist):
        # note: can only get max of 100 items, but allowed to give an offset
        # therefore can iterate over full playlist by just popping up 100 in the offset until full thing is read
        # obviously will have to contain it or whatever
        toReturn = []
        playlist_id = playlist.get("id")
        url = "https://api.spotify.com/v1/playlists/{}/tracks".format(playlist_id)
        offset = 0
        playlistCount = playlist.get("tracks").get("total")
        while offset < playlistCount:
            offsetUrl = url + "?offset={}".format(offset)
            response = requests.get(
                offsetUrl, headers={"Authorization": f"Bearer {self.api_token}"}
            )
            if not response.ok:
                print("somethign went wrong reading stuff")
            else:
                for track in response.json().get("items"):
                    toReturn.append(
                        Track(
                            track.get("track").get("id"),
                            track.get("track").get("duration_ms"),
                            track.get("track").get("name"),
                        )
                    )

            offset += 100
        return toReturn

    def make_new_playlist_with_name_and_description(self, name, description):
        url = "https://api.spotify.com/v1/users/{}/playlists".format(self.user_id)
        request_body = json.dumps({"name": name, "description": description})
        response = requests.post(
            url,
            headers={"Authorization": f"Bearer {self.api_token}"},
            data=request_body,
        )
        if not response.ok:
            print("couldn't make playlist called {}".format(name))
            print(response.json())
        else:
            print("successfully made playlist called {}".format(name))
            return response.json().get('id')

    def add_tracks_to_playlist(self, tracks, playlistId):
        tracklistLength = len(tracks)
        if tracklistLength == 0:
            print("yo not cool no tracks to add yo")
            return
        url = "https://api.spotify.com/v1/playlists/{}/tracks?uris=".format(playlistId)
        index = 0
        for track in tracks:
            url += "spotify:track:"+track.uri
            index += 1
            if index < tracklistLength:
                url += ","
        response = requests.post(
            url,
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {self.api_token}"},
        )
        if not response.ok:
            print("couldn't modify playlist")
            print(response.json())
        else:
            print("succesfully added tracks to playlist")
