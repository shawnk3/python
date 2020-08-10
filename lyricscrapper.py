
GENIUS_API_TOKEN='4930jLaEwEJJEukP4bHUGA1TkBfP8ecjJj6RPb2mft37WLB0Anoc3ARUlam6UDua'

import requests
from bs4 import BeautifulSoup
import os
import re


#get artist object from Genius API
def request_artist_info(artist_name,page):
    base_url = "https://api.genius.com"
    headers = {'Authorization': 'Bearer ' + GENIUS_API_TOKEN}
    search_url = base_url + '/search?per_page=10&page' + str(page)
    data = {'q':artist_name}
    response = requests.get(search_url,data = data,headers = headers)
    return response

#get genius.com
def request_song_url(artist_name,song_cap):
    page = 1
    songs = []
    
    while True:
        response = request_artist_info(artist_name, page)
        json = response.json()
        
        
        #collect up to the song cap for the artist
        song_info = []
        for hit in json['response']['hits']:
            if artist_name.lower() in hit['result']['primary_artist']['name'].lower():
                song_info.append(hit)
            #print(hit)
        
        #collect song urls
        for song in song_info:
            if(len(song) < song_cap):
                url =  song['result']['url']
                songs.append(url)
        if(len(songs) == song_cap):
            break
        else:
            page+=1
            
            
            
request_song_url("Kanye", 2)
