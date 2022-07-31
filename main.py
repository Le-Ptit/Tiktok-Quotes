from msilib import text
import requests
import json
import datetime
import os
import random
from moviepy.editor import *

"""
HAVE TO INCLUDE THIS IN VIDEO DESCRIPTION :  

The Inspiration by Keys of Moon | https://soundcloud.com/keysofmoon
Attribution 4.0 International (CC BY 4.0)
https://creativecommons.org/licenses/by/4.0/
Music promoted by https://www.chosic.com/free-music/all/
"""

url_request = "https://api.quotable.io/random"
basics_directory = "\\basics"
music_directory = "audio.mp3"
video_directory = "video.mp4"

def load_ids_file(file_url):
    with open(file_url) as file:
        file_content = json.load(file)
    
    return file_content

def get_random_quote(method="GET", url="https://api.quotable.io/random"):
    response = requests.request(method=method, url=url)

    return response.json()

def check_quote_in_dict(id_quote, dict):
    if id_quote in dict.keys():
        return True
    else:
        return False

def get_random_file_from_directory():
    return os.getcwd()+basics_directory+"\\"+str(random.choice(os.listdir(os.getcwd()+basics_directory)))

def get_video_from_directory(directory):
    return VideoFileClip(directory)

if __name__ == '__main__':
    # Code
    already_quote = True

    while already_quote == True:
        quote = get_random_quote()

        id_quote = quote['_id']

        for id_added in load_ids_file('ids.json')['ids']:
            if not (check_quote_in_dict(id_quote, id_added)):
                already_quote = False
    
    # QUOTE IS NOW NEW AT 100% SUR

    main_video = VideoFileClip(video_directory)
    audio_clip = AudioFileClip(music_directory)

    new_audio = CompositeAudioClip([audio_clip])
    main_video.audio = new_audio

    text_clip = TextClip("Wisdom is the supreme part of happiness.", fontsize=50, color='black')

    text_clip = text_clip.set_position('center').set_duration(40)

    new_video = CompositeVideoClip([main_video, text_clip])

    new_video.write_videofile("new_episode.mp4", fps=30)
