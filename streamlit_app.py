# https://moran-shemesh-abuser-streamlit-app-oyisjd.streamlit.app/
# https://www.datacamp.com/tutorial/streamlit
import streamlit as st
#from pytube import YouTube
#from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import pandas as pd
from pandas import DataFrame
import numpy as np
import os

#OPENAI_API_KEY = config('KEY') #take the key from the .env file
#translator = Translator()

st.caption(" © Violence Prediction by Moran Shemesh")

user_link = st.text_area("", placeholder="Add here a youTube link to a video")


def download1(link, video_path, file_num):
  name = str(file_num)
  try:
    !yt-dlp -f "bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" $link -o "/content/drive/MyDrive/HIT/whatsapp_analyze/data_03_07_2023/mp4/%(title)s"
  except:
    print("An error has occurred")
  print("Download is completed successfully")

