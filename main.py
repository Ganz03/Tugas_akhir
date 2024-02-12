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

"""-Dataset"""

# #Load dataset
# from google.colab import files
# uploded = files.upload()

#dataset

path_dataset = st.secrets.path_configuration.path_dataset
st.text(path_dataset)
# filename = "Twitter_Data.csv"
# twitter = pd.DataFrame(f"{path_dataset}{filename}")


# """-Clean  text"""

# def cleanTxt(text):
#     if isinstance(text, str):
#         # Remove mentions
#         text = re.sub(r'@[A-Za-z0-9_]+', '', text)
#         # Remove special characters and numbers
#         text = re.sub(r'[^a-zA-Z]', ' ', text)
#         # Remove single characters
#         text = re.sub(r'\s+[a-zA-Z]\s+', ' ', text)
#         # Remove multiple spaces
#         text = re.sub(r'\s+', ' ', text)
#         return text.strip()
#     else:
#         return text  # Return non-string values unchanged

# # Assuming twitter is your DataFrame
# twitter['text'] = twitter['text'].apply(cleanTxt)

# # Display the modified DataFrame
# display(twitter)

# def getSubjectivity(text):
#     if isinstance(text, str):
#         return TextBlob(text).sentiment.subjectivity
#     else:
#         return None

# def getPolarity(text):
#     if isinstance(text, str):
#         return TextBlob(text).sentiment.polarity
#     else:
#         return None

# twitter['Subjectivity'] = twitter['text'].apply(getSubjectivity)
# twitter['polarity'] = twitter['text'].apply(getPolarity)

# display(twitter)

# """-Word CLoud"""

# allwords = ''.join([str(twts) for twts in twitter['text'] if isinstance(twts, str)])

# wordcloud = WordCloud(width=500, height=300, random_state=21, max_font_size=119).generate(allwords)

# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis('off')

# """-Subjectivity and Polarity"""

# def getAnalysis(score):
#   if score <0:
#     return 'Negative'
#   elif score == 0:
#     return 'Netral'
#   else:
#     return 'positive'

# twitter['analysis'] = twitter['polarity'].apply(getAnalysis)

# display(twitter)

# """-Positive Statement"""

# j = 1
# sortedTwitter = twitter.sort_values(by=['polarity'])

# for i in range(0, sortedTwitter.shape[0]):
#     if sortedTwitter['polarity'][i] > 0:  # Mengecek apakah sentimen positif
#         print(str(j) + ') ' + sortedTwitter['text'][i])
#         print()
#         j = j + 1

# """

# -Negative Statement

# """

# j = 1
# sortedTwitter = twitter.sort_values(by=['polarity'])

# for i in range(0, sortedTwitter.shape[0]):
#     if sortedTwitter['polarity'][i] < 0:  # Mengecek apakah sentimen positif
#         print(str(j) + ') ' + sortedTwitter['text'][i])
#         print()
#         j = j + 1

# """-Sentiment analisis"""

# twitter['analysis'].value_counts()

# plt.title('sentiment Analysis')
# plt.xlabel('sentiment')
# plt.ylabel('counts')
# twitter['analysis'].value_counts().plot(kind='bar')
# plt.show()