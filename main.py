#REQUIRED LIBRARY for this project

from apiclient.discovery import build
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from string import punctuation #punctutaion are . , all this
from string import punctuation  # punctutaion are . , all this

from apiclient.discovery import build
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.collocations import BigramCollocationFinder
import nltk
nltk.download('stopwords')

api_key = 'AIzaSyAC7dHcAjttc5nhOYr9ohf9eeNZrCwtwOg'

#bandeya song url
video_url = 'https://www.youtube.com/watch?v=Wj8C_bpnkTY'

#creating the fuction for ertarcting commnets


def video_comments(api_key, video_url):
    video_id = video_url.split(sep='=')[1]

    # creating youtube resource object
    youtube = build('youtube', 'v3',
                    developerKey=api_key)

    # retrieve youtube video results
    video = youtube.commentThreads().list(
        part='snippet,replies',
        videoId=video_id).execute()
    x = video_response(video)
    return x


def video_response(video):
    replies = []
    comments = []
    for i in video['items']:
        # Extracting comments
        comment = i['snippet']['topLevelComment']['snippet']['textDisplay']

        # counting number of reply of comment
        replycount = i['snippet']['totalReplyCount']
        # if reply is there
        if replycount > 0:

            # iterate through all reply
            for reply in i['replies']['comments']:
                # Extract reply
                reply = reply['snippet']['textDisplay']

                # Store reply is list
                replies.append(reply)

        # print comment with list of reply
        # print(comment, replies, end = '\n\n')
        comments.append(comment)

    return comments


comm= video_comments(api_key,video_url)
print(comm)

#CLEANING OF DATA WITH THE HELP OF NLTK PACKAGE...

#using word_tonization for cleaning of word from the text...

s = ''
for i in comm:
     s = i + s
text = word_tokenize(s)
print(text)

text = sent_tokenize(s)
print(text)

#removing the stopwords from the commnets
print(punctuation)
custom_list = set(stopwords.words('english')+list(punctuation))
word_list = [word for word in word_tokenize(s) if  not word  in custom_list]
#print(word_list)
print(custom_list)

























