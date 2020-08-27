# This class will contain stuff used to make and mess with playlists.
# SHOULD NOT INTERACT WITH QUERIES AT ALL, ONLY CREATING AND MANAGING LISTS WHICH WILL BE PASSED TO THE API INTERACTOR
import random



class PlaylistManipulator:

    @staticmethod
    def split_tracklist_into_chunks_of_one_hundered(tracks):
        toReturn = []
        tempCollection = []
        index = 0
        for track in tracks:
            if index > 0 and index % 100 == 0:
                toReturn.append(tempCollection)
                tempCollection = []
                index = 0
            tempCollection.append(track)
            index += 1
        if len(tempCollection) > 0:
            toReturn.append(tempCollection)
        return toReturn

    def get_track_list_this_long_from_track_list(self, startTracks, time):
        startCount = len(startTracks)
        if startCount == 0:
            print("get_track_list_this_long got 0 starttracks, not cool man")
            return
        toReturn = []
        currentTime = 0
        while currentTime < time:
            temporaryTrackStore = list(startTracks)
            index = 0
            while index < startCount and currentTime < time:
                index += 1
                selection = random.randrange(0, len(temporaryTrackStore))
                toAdd = temporaryTrackStore[selection]
                temporaryTrackStore.remove(toAdd)
                currentTime += toAdd.time
                toReturn.append(toAdd)
        return toReturn
