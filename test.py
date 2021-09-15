import tweepy


#tweepy can be broken down two several functionalities


# Authentication of user
# the tweepy.0authhandler

auth = tweepy.OAuthHandler("mUvYELvn0YT8oYj6lSoOH1wlA", "SciAd2zLST9N2Pdtr897ZPlYleliYQKB3pVd9EmsncwPd0Kbkx")
auth.set_access_token("1437722243040219138-f295c215RCy6zVsrAqQ6lvdPm5QooV", "MBsxfhASuHi0TOnDPREoZABA8RZlO0SI74RrEWA6t7KmF")


# the creation of a twitter object
# tweepy.AP1
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("ok")

except:
    print("error during authenitication")



# the api has several objects which we are going to explore below


# method for user timelines
# reading tweets from user timelines, your timeline or any other timeline


timeline = api.home_timeline()
for tweet in timeline:
    print(f"{tweet.user.name} tweeted"
          f" {tweet.text}")


# method for handling tweets, reading,

# we can define an object inside an object

user = api.get_user("symon_kipkemei")
print("user details")
print(user.name)
print(user.description)
print(user.location)

print(f"\n{user.name} Last 20 followers")
for follower in user.followers():
    print(follower.name)


# the highlight from this discourse is that the user-Id that
# identifies and distinguishes one account from the other is the
# is the @ tag




# get most recent tweets
tweets = api.home_timeline(count=1)
tweet = tweets[0]

print(f"Liking tweet{tweet.id} of {tweet.author.name}")
api.create_favorite(tweet.id)
