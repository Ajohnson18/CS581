#   Author: Alex Johnson

#  This program accesses data from a twitter user site

#  To run in a terminal window:   python3  twitter_data.py


import tweepy

### PUT AUTHENTICATOIN KEYS HERE ###
CONSUMER_KEY = "Wxzpv4hM6YobyQ0qwaoLEcEYb"
CONSUMER_KEY_SECRET = "OhyOLnHk44SLgC2bY1OtaeXTu9FVZpKxqd1yDQIBK7UW8lZ4kU"
ACCESS_TOKEN = "935546766451130368-MWuXAkcVIqxpb5BiirFYljiXwwImfqS"
ACCESS_TOKEN_SECRET = "phKrqNo984ZWHQShJzA3c8Sqcs9kkZSqKDyajP0IbKznS"

# Authentication

authenticate = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
authenticate.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#  use wait_on_rate_limit to avoid going over Twitter's rate limits
api = tweepy.API(authenticate, wait_on_rate_limit=True, 
                 wait_on_rate_limit_notify=True)

def getUserInfo(username):
	twitter_user = api.get_user(username)
	print("=============================")
	print("	  User Info")
	print("=============================")
	print("User: ", twitter_user.name)
	print("Screen Name: ", twitter_user.screen_name)
	print("User ID: ", twitter_user.id)
	print("Description: ", twitter_user.description)
	print("# of Followers: ", twitter_user.followers_count)	# # find and print all the users info
	print("")
	print("=============================")
	print("	 Recent Tweets")
	print("=============================")

	# Creating a Cursor to get tweets from a user
	try:
		tweets = tweepy.Cursor(api.user_timeline, screen_name=twitter_user.screen_name)

		# Get and print 1 tweet
		for tweet in tweets.items(1):
			print(twitter_user.name, ": ", tweet.text)
			print("Published: ",tweet.created_at)
	except:
		print("No tweets found")	# print if no tweets found

	print("")
	print("=============================")
	print("	  Followers")
	print("=============================")

	#create a cursor for finding top 10 followers
	try:
		followers = tweepy.Cursor(api.followers, screen_name=twitter_user.screen_name)
		#print top 10 follows from cursor
		for follower in followers.items(10):
			print(follower.name)
	except:
		print("No followers found")

# infinite loop to prompt user for username
while True:
	print("")
	username = input("Twitter Username: ")
	print("")
	if username.upper() == "STOP":	# if stop end program
		break
	else:
		try:
			getUserInfo(username)	# run function if user found
		except:
			print("Error: User not found") 	# if user not found report error
			continue