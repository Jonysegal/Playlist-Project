from SpotifyPlaylist import Runner
class UserController:
    def __init__(self):
        self.runner = Runner()
    def get_requested_playlist(self):
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
        self.requestedPlaylist = playlists[index-1]
        print("aight boyo u selected {}".format(self.requestedPlaylist.get('name')))
        
    def get_requested_time(self):
        hours = input("how many hours u want it?")
        if not hours.isnumeric():
            print("not a number :(")
            self.get_requested_time()
            return
        hours = int(hours)
        
        minutes = input("how many minutes u want it?")
        if not minutes.isnumeric():
            print("not a number :(")
            self.get_requested_time()
            return
        minutes = int(minutes)
        
        seconds = input("how many seconds u want it?")
        if not seconds.isnumeric():
            print("not a number :(")
            self.get_requested_time()
            return
        seconds = int(seconds)
        
        self.requestedTime = self.milliseconds_from_hours_minutes_seconds(hours, minutes, seconds)
        
    def milliseconds_from_hours_minutes_seconds(self, hours, minutes, seconds):
        return ((((hours * 60) + minutes) * 60) + seconds) * 1000
        
    def get_total_tracks_length(self, tracks):
        length = 0
        for track in tracks:
            length += track.time
        return length
        

    def main_sequence(self):
        self.get_requested_playlist()
        self.get_requested_time()
        tracks = self.runner.get_tracks_in_playlist(self.requestedPlaylist)
        playlistLength = self.get_total_tracks_length(tracks)
        if self.requestedTime > playlistLength:
            tooLongOk = input("Your playlist isn't long enough to make a playlist of that length. Is that cool? (y/n)")
            if tooLongOk.lower() == "n":
                self.main_sequence()
                return
        print("proceeding with {}".format(self.requestedPlaylist.get('name')))
        
            
                
            
        
    
        
    