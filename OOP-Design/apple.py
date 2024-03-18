"""
given an array 
song title: string
song duration : string
date/time stamp of when the song was played : string

[{song title: string,
song duration: string,
date/time stamp: string},{},{}]

date example: "00:00:00 03/16/2024"

12 and 13 index

for the last seven days 
return the 
"""
from datetime import date

class Solution:
  def seven(self, listening_activity):
    song_duration_map = {}

    for i in listening_activity:
      if int(i.date[12:14]) > 9:
        if i.song_title not in song_duration_map:
          song_duration_map[i.song_title] = i.song_duration

        else:
          song_duration_map[i.song_title] += i.song_duration

    print(song_duration_map)

    top_three_songs = song_duration_map.items()

    print(top_three_songs)

    top_three_songs = sorted(top_three_songs, key=lambda x: x[1], reverse=True)[:3]

    print(top_three_songs)

    return top_three_songs

      