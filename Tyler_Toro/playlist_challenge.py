# Music playlist challenge!
# In this challenge, you'll have to both work on this script, and the accompanying script playlist_functions.py
# All of your functions should be in the other script (playlist_functions.py)
# But, you'll run your functions here

# 1 Import all the functions in playlist_functions.py
import numpy
from playlist_functions import *
# This code initializes your playlist as an empty list. no songs in it yet!
my_playlist = []



# 2 Check what is in your playlist using the display_playlist() function
# HINT: the display_playlist() function in playlist_functions.py to figure out how to use it
print('Question 2')
print("using function from other file, playlist_function, to check\n".upper())
display_playlist(my_playlist)
print()
# 3 Add a song to my_playlist using the add_song() function
# The song that you add should be a dictionary, with the following key-value pairs
# 'artist' (string)
# 'title' (string)

'''
example_song = {'artist': 'Lauryn Hill', 'title': 'Everything Is Everything'}
'''
add_song(my_playlist, {"artist": "Korn", "title": "Trash"})

# 4 Check that you've added the song by running the display_playlist() function again
print('Question 4')
print("Checking to see if our added song is on the list".upper())
print()
display_playlist(my_playlist)
# 5 Add 2 more songs to my_playlist, then display it again using the display_playlist() function
print()
print('Question 5')
print()

add_song(my_playlist, {"artist": "POD", "title": "Youth of the Nation"})
add_song(my_playlist, {"artist": "Return to Forever", "title": "Shadow of Lo"})
display_playlist(my_playlist)
print()
# 6 In playlist_functions.py, define a function called get_playlist_length()
# See playlist_functions.py for details on how to define this function
# THEN, call that function in this script to get the length of my_playlist
print('Question 6')
print()

print("The number of songs in my playlist are:".upper())
print(get_playlist_length(my_playlist))
print()
# 7 At the top of this script, import numpy using the usual alias

# 8: Using numpy, calculate the average monthly plays for a song
# TODO: using the mean() function from numpy, calculate the average of monthly_plays
# You don't have to write any functions for this question
print()
print('Question 8')
monthly_plays = [127030, 274920, 232453, 98278, 500301, 235462]
print()
monthly_plays_avg = numpy.mean(monthly_plays)
print("The average monthly plays for song:".upper())
print(int(monthly_plays_avg))
print()

# BONUS In playlist_functions.py, define a new function called play_track()
# See playlist_functions.py for details on how to define this function
# Then play a few tracks, and run display_playlist() again to make sure it works
print('BONUS')
print()
print("Playing youth of a nation by POD once".upper())
print()
play_track(my_playlist, 2)
print()
print("Playing youth of a nation by POD again".upper())
play_track(my_playlist, 2)