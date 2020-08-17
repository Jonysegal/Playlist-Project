from SpotifyPlaylist import Runner
class UserController:
    def __init__(self):
        self.runner = Runner()
    def get_playlist_choice(self):
        playlists = self.runner.get_playlists()
        playlistCount = len(playlists)
        if playlistCount == 0:
            print("No playlists found rip")
            return
        i = 0
        for x in playlists:
            i+=1
            print("{}: {}".format(i, x.get('name')))
        index = input("Type the number of the intended playlist: ")
        if not index.isdigit():
            print("plz enter number")
            self.get_playlist_choice()
            return
        index = int(index)
        if index == 0 or index > playlistCount:
            print("index too high or too low idk")
            self.get_playlist_choice()
            return
        print("inex is {}".format(index))
        
        