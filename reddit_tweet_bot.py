#! usr/bin/env python3
import praw
import tweepy as ty
import time
from datetime import datetime


############################################################################################
#
#              This is a sample api key entry. Entries given here are just gibberish.
#
#           Input the correct values from the respective sites, to get authenticated.
#
#                               "BELOW ENTRIES WONT WORK!!!"  
#                    
#############################################################################################

#Reddit secret
client_id='XxUlhuz8Ig'
client_secret='dgpJDhfghfgu6gsdRHtMMU'
user_agent='testscript'
username='yourusername'
password='ghj6242rfsdfsdg'


#twitter secret
consumer_key='p2AgS4GHjsdhf77hUld0'
consumer_secret='Q0D1S6u3PCj5alHhE4Dfkj982347AXk1dLQ8sWKWrOf7uA3tq016'
access_token='100895838062968013uhfIKHhwe5dDROraddUjo2NrXmC'
access_token_secret='sQKbHLKnKfQsdfsdfJJUADi7wedwNbdMv2jxxiu'

##################################################################################################




#Authentication for Reddit API
def setRedditAuth():
        reddit_api = praw.Reddit(client_id=client_id,client_secret=client_secret,user_agent=user_agent,
                                                         username=username,password=password)
        print(str(datetime.now()) + " Reddit Authenticated")
        return reddit_api

#Authentication for Twitter API
def setTwitterAuth():
        auth = ty.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        twitter_api = ty.API(auth)
        print(str(datetime.now()) +" Twitter Authenticated ")
        return twitter_api

#As the function name says "Sends out the tweet"
def tweetout(twitter_api,tweet):
        try:
                twitter_api.update_status(tweet)
                print(str(datetime.now())+" Tweeted")
        except:
         pass

#Collects Top 100 entries from the Subreddit 'Showerthoughts'
def getShowerThoughts(reddit_api):
        temp_list = []
        for submission in reddit_api.subreddit('Showerthoughts').top('all'):
                if not submission.stickied:
                        temp_list.append(submission.title)
        return temp_list

if __name__ == "__main__":
        while True:
                count = 0
                twitter_api = setTwitterAuth()
                reddit_api = setRedditAuth()
                tweet_list= getShowerThoughts(reddit_api)

                #Runs once in 15 mins interval.
                while count < 94:
                        count += 1
                        tweetout(twitter_api,tweet_list[count])
                        time.sleep(900)
