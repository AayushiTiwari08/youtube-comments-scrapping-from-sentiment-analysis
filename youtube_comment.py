#!/usr/bin/env python
# coding: utf-8

# # Topic of the project : Sentiment analysis
# 

# In this we are going to write the code for how to extract comments form youtube

# # From pip install the libaray google-api-python-client
# 

# In[1]:


import googleapiclient
from googleapiclient.errors import HttpError
import os


# # writting the code for extracting youtube comments.

# In[ ]:


from googleapiclient.discovery import build
  
api_key = 'AIzaSyAC7dHcAjttc5nhOYr9ohf9eeNZrCwtwOg'
  
def video_comments(video_id):
    # empty list for storing reply
    replies = []
  
    # creating youtube resource object
    youtube = build('youtube', 'v3',
                    developerKey=api_key)
  
    # retrieve youtube video results
    video_response=youtube.commentThreads().list(
    part='snippet,replies',
    videoId=video_id).execute()
  
    # iterate video response
    while video_response:
        
        # extracting required info
        # from each result object 
        for item in video_response['items']:
            
            # Extracting comments
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
              
            # counting number of reply of comment
            replycount = item['snippet']['totalReplyCount']
  
            # if reply is there
            if replycount>0:
                
                # iterate through all reply
                for reply in item['replies']['comments']:
                    
                    # Extract reply
                    reply = reply['snippet']['textDisplay']
                      
                    # Store reply is list
                    replies.append(reply)
  
            # print comment with list of reply
            print(comment, replies, end = '\n\n')
  
            # empty reply list
            replies = []
  
        # Again repeat
        if 'nextPageToken' in video_response:
            video_response = youtube.commentThreads().list(
                    part = 'snippet,replies',
                    videoId = video_id
                ).execute()
        else:
            break
  
# Enter video id
video_id = "Mzj3_FjuDuI"
  
# Call function
video_comments(video_id)


# In[ ]:




