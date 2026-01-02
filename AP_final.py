# This program takes a users score and recomends a song based off of of the score
# Ts was supposed to play the songs but i couldnt figure that out in a weekend lol
#  *Property of Mr.Swag @iJimmy500 on Github**
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


client_id = 'USER_CLIENTID'
client_secret = 'USER_CLIENTSECRET'

print("Ever wondered what song you should listen to based off of your grades? Use this program to find out!")
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def recommend_song(score):
    if score >= 90: #Passing Score
        return "The One (Just got my degree)" + "YT"
    elif 70 <= score < 89: #Normal Score
        return "Congratulations" + "Post Malone"
    else: #Low Score
        return "Bury Me" + "Pinkpantheress"

def search_track(query):
    result = sp.search(q=query, limit=1)
    if result['tracks']['items']:
        track = result['tracks']['items'][0]
        return track['name'] + " by " + track['artists'][0]['name']
    else:
        return "No song found"

def main():
    score = int(input("Enter the score you got (0-100): "))
    recommended_song = recommend_song(score)

    if recommended_song == "Try Again":
        print(recommended_song)
    else:
        print("Recommended Song:", recommended_song)

        # Search for recommended song on Spotify
        recommended_song_name = recommended_song.split(' by ')[0]
        print("Searching for your song on Spotify...")
        spotify_song = search_track(recommended_song_name)
        print("Try this song out!:", spotify_song)

if __name__ == "__main__":
    main()
