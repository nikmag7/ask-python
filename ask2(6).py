import tweepy
import tweepy.binder
api_key="jRfxloPA5DQgk3e2WK7tZICE8"
api_key_secret="FtUo99vRORjWPBlNWI8MstiYIJgaN954TtHPDqNHzSvoUETAE4"
access_token="1353392616012918784-JphnmyZIWbf5e5WZvjuuUToyJt4Eny"
access_token_secret="7ci8zFkZwI5lR6HeyJggjSssDIbeRhaRmVy5pN9Lku16E"

list1=[input("api_key"),input("api_key_secret"),input("access_token"),input("access_token_secret")]
auth=tweepy.OAuthHandler(list1[0],list1[1])
auth.set_access_token(list1[2],list1[3])
api = tweepy.API(auth)

on=api.get_user(input("Give username"))
list2=[]
def get_last_tweets(username):
    tweets =" "
get_last_tweets(on)
list2.append(tweets)
longest_word =''
for word in list2:
    if len(word) > len(longest_word):
        longest_word = word
print longest_word
