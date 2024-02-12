import streamlit as st
import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

st.set_page_config(
    page_title="Twitter Statement Analysis",
    layout= "wide"
)

#title
with st.container(border=True):
    st.title("Analisis Statement di Twitter Mengenai Pemilihan anggota parlemen di India")
    st.subheader("oleh Ilham azrinargana Pulungan")

# #Load dataset
# from google.colab import files
# uploded = files.upload()

#dataset

# path_dataset = st.secrets.path_configuration.path_dataset
# st.text(path_dataset)
with st.container(border=True):
    st.write("Dataset", align='center')
filename = "Twitter_Data.csv"
twitter = pd.read_csv(filename)
twitter.rename(columns={'clean_text': 'text'}, inplace=True)
twitter.drop(labels=['category'],axis=1,inplace=True)
st.dataframe(twitter,
             use_container_width=True,
             hide_index=True
             )

def cleanTxt(text):
    if isinstance(text, str):
        # Remove mentions
        text = re.sub(r'@[A-Za-z0-9_]+', '', text)
        # Remove special characters and numbers
        text = re.sub(r'[^a-zA-Z]', ' ', text)
        # Remove single characters
        text = re.sub(r'\s+[a-zA-Z]\s+', ' ', text)
        # Remove multiple spaces
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
    else:
        return text  # Return non-string values unchanged

# Assuming twitter is your DataFrame
twitter['text'] = twitter['text'].apply(cleanTxt)

with st.container(border=True):
    st.write("Subjectivity and polarity", align='center')

def getSubjectivity(text):
    if isinstance(text, str):
        return TextBlob(text).sentiment.subjectivity
    else:
        return None

def getPolarity(text):
    if isinstance(text, str):
        return TextBlob(text).sentiment.polarity
    else:
        return None

twitter['Subjectivity'] = twitter['text'].apply(getSubjectivity)
twitter['polarity'] = twitter['text'].apply(getPolarity)
st.dataframe(twitter,
             use_container_width=True,
             hide_index=True
             )

with st.container(border=True):
    st.write("WordCloud", align='center')

allwords = ''.join([str(twts) for twts in twitter['text'] if isinstance(twts, str)])

wordcloud = WordCloud(width=500, height=300, random_state=21, max_font_size=119).generate(allwords)

st.image(wordcloud.to_array(), caption='WordCloud')

with st.container(border=True):
    st.write("Analysis", align='center')
def getAnalysis(score):
  if score <0:
    return 'Negative'
  elif score == 0:
    return 'Netral'
  else:
    return 'positive'

twitter['analysis'] = twitter['polarity'].apply(getAnalysis)

st.dataframe(twitter,
             use_container_width=True,
             hide_index=True
             )

with st.container(border=True):
    st.write("Positive Statement", align='center')

j = 1
sortedTwitter = twitter.sort_values(by=['polarity'])

for i in range(0, sortedTwitter.shape[0]):
    if sortedTwitter['polarity'][i] > 0 and j <= 10:  # Mengecek apakah sentimen positif
        st.write(str(j) + ') ' + sortedTwitter['text'][i])
        st.write()
        j = j + 1

with st.container(border=True):
    st.write("Negative Statement", align='center')

j = 1
sortedTwitter = twitter.sort_values(by=['polarity'])

for i in range(0, sortedTwitter.shape[0]):
    if sortedTwitter['polarity'][i] < 0 and j <= 10:  # Mengecek apakah sentimen positif
        st.write(str(j) + ') ' + sortedTwitter['text'][i])
        st.write()
        j = j + 1

with st.container(border=True):
    st.write("Sentiment analysis Result", align='center')

twitter['analysis'].value_counts()
plt.figure(figsize=(10, 6))
plt.title('sentiment Analysis')
plt.xlabel('sentiment')
plt.ylabel('counts')
st.bar_chart(twitter['analysis'].value_counts())
