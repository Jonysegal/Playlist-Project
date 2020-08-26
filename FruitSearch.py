#LITTLE SIDE ADVENTURE TO MAKE A FRUIT PLAYLIST FOR NATE
from SpotifyPlaylist import Runner
from PlaylistManipulations import PlaylistManipulator
from track import Track

class FruitPlaylistMaker:
    def __init__(self):
        self.runner = Runner()
        self.playlistManipulator = PlaylistManipulator()

fpm = FruitPlaylistMaker()
fruits = ["Apple", "Apricot", "Banana", "Blackberry", "Blueberry", "Pear", "Crab Apple", "Cherry", "Cranberry", "Date", "Dragonfruit", "Grape", "Grapefruit", "Kiwi", "Kumquat", "Lemon", "Lime", "Mango", "Cantaloupe", "Honeydew", "Watermelon", "Nectarine", "Orange", "Clementine", "Tangerine", "Papaya", "Peach", "Pineapple", "Pomegranate", "Raspberry", "Strawberry"]
tracklist = []
unfindableFruits =[]
findableFruits = []
for fruit in fruits:
    foundSong = fpm.runner.search_song("", fruit)
    if isinstance(foundSong, Track):
        tracklist.append(foundSong)
        findableFruits.append(fruit)
    else:
        unfindableFruits.append(fruit)
if len(findableFruits) == 0:
    print("Couldn't find any fruits :(")
description = "Made a playlist based off of the following keyword" + ("s" if len(findableFruits) > 1 else "") + ": "
for fruit in findableFruits:
    description += fruit + (", " if fruit != findableFruits[-1] else "")
if len(unfindableFruits) != 0:
    description = "\nCould not find a song for the following keyword" + ("s" if len(unfindableFruits) > 1 else "") + ": "
    for noFruit in unfindableFruits:
        description += noFruit + (", " if noFruit != unfindableFruits[-1] else "")
fpm.runner.add_tracks_to_playlist(tracklist, fpm.runner.make_new_playlist_with_name_and_description("A fruity playlist", description))
