# https://moran-shemesh-abuser-streamlit-app-oyisjd.streamlit.app/
# https://www.datacamp.com/tutorial/streamlit
import streamlit as st
import time
import googletrans
from googletrans import Translator
import openai
import wandb
from pathlib import Path
import pandas as pd
import numpy as np
import json
from tqdm import tqdm
from io import StringIO
from decouple import config
from PIL import Image

#OPENAI_API_KEY = config('KEY') #take the key from the .env file
#translator = Translator()

st.caption(" © Violence Prediction by Moran Shemesh")

"""

def GPT_Completion(texts):
  openai.api_key = OPENAI_API_KEY
  response = openai.Completion.create(
  engine="gpt-3.5-turbo-0301",#text-davinci-003",
  prompt =  texts,
  temperature = 0,
  top_p = 1,
  max_tokens = 100,
  frequency_penalty = 0,
  presence_penalty = 0
  )
  return (response.choices[0].text)

def GPT_Completion1(texts):
    openai.api_key = OPENAI_API_KEY
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=texts,
    max_tokens=7,
    temperature=0
    )
    return (response.choices[0].text)





def is_violence_heb(text, language):
  
  if language == 'Hebrew':
    translated_text = translator.translate(text, src='hebrew', dest='en').text
    que = "is following correspondence contains domestic violence - give a  score for domestic violence level from 0 to 10, and explain why there is domestic violence. \n\nScore: \nExplaination: \n." + translated_text + "."
    ans_eng = GPT_Completion(que)
    ans_heb = translator.translate(ans_eng, src='en', dest='hebrew').text
    st.success(ans_heb)
  else:
    que = "is following correspondence contains domestic violence - give a  score for domestic violence level from 0 to 10, and explain why there is domestic violence. \n\nScore: \nExplaination: \n." + text + "."
    #ans_heb = translator.translate(ans_eng, src='en', dest='hebrew')
    ans_eng = GPT_Completion(que)
    st.info(ans_eng)

st.title ("ABUser") 
st.markdown("**Look out for signs of domestic violence in your correspondence with your partner**")


language = st.radio('Prefered language',['Hebrew', 'English'])
#textrank_summary_size = 0
#if model_type=="RankText":
#  textrank_summary_size = st.slider('How long would you like the summary to be? (Percentage of full text)', 5,50)
string_data1 = "רון: איפה את? \n  דנה:  אצל חברה\nרון: עוד הפעם עם החברות האלה? יאללה מתי את חוזרת"
string_data = "6/21/19, 09:27 - איתמר: במקום שהכסף ילך על הוצאות לתינוק חדש הוא הולך על בילויים ומותרות שלך ושל החברות שלך \n 6/21/19, 09:28 - איתמר: למה כל דבר את מנסה להסתיר ממני?!\n6/21/19, 09:28 - איתמר: נמאס לי כבר\n6/21/19, 09:29 - איתמר: מה לא ברור לך?!\n6/21/19, 09:30 - איתמר: את צריכה פחות להתעסק בבילוים ויותר במשפחה"

uploaded_file = st.file_uploader('You can upload a txt file, enter or paste a correspondence with your partner')
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
#   st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
#    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
#    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    dataframe = dataframe.replace("{'text:'",'')
    st.write(dataframe)

user_text = st.text_area("", value=string_data, placeholder="Enter or paste your text here")

start = st.button('Start')

if start:
  start = False
  
  with st.spinner("Please wait..."):
    is_violence_heb(user_text, language)
"""
