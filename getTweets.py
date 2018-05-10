# This script downloads the last 3240 tweets from a Twitter user's account

import tweepy

# Enter your access tokens here
auth = tweepy.OAuthHandler('', '')
auth.set_access_token('', '')

api = tweepy.API(auth)

alltweets = []

new_tweets = api.user_timeline(screen_name=screen_name, count=200)

alltweets.extend(new_tweets)

oldest = alltweets[-1].id - 1

while len(new_tweets) > 0:
    new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)

    alltweets.extend(new_tweets)

    oldest = alltweets[-1].id - 1

# write to JSON
file = open('tweet.json', 'wb')
print "Writing teet objects to JSON..."
for status in alltweets:
    json.dump(status._json, file, sort_keys=True, indent=4)

    print "Done"
    file.close()

if __name__ == '__main__':
    get_all_tweets("@POTUS") # insert Twitter account name
