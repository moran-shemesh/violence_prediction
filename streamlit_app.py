# https://moran-shemesh-abuser-streamlit-app-oyisjd.streamlit.app/
# https://www.datacamp.com/tutorial/streamlit
import streamlit as st
import pytube
# import nltk

#from pytube import YouTube
#from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import pandas as pd
from pandas import DataFrame
import numpy as np
import os
from google.colab import drive
drive.mount('/content/drive', force_remount=True)
#OPENAI_API_KEY = config('KEY') #take the key from the .env file
#translator = Translator()

st.caption(" © Violence Prediction by Moran Shemesh")

user_link = st.text_area("", placeholder="Add here a youTube link to a video")

def download(link, video_path):
  print("1")
  youtubeObject = YouTube(link)
  print("2")
  youtubeObject = youtubeObject.streams.get_highest_resolution()
  print("3")
  name = "video"
  print(name)
  try:
      youtubeObject.download(output_path= video_path, filename=name)
  except:
      print("An error has occurred")
  print("Download is completed successfully")


