import settings
import tweepy
import dataset
from textblob import TextBlob
from sqlalchemy.exc import ProgrammingError
import json
import time
import dumpcsv
import dumpjson
import atexit


#atexit.register(dumpcsv.dumpcsv)
atexit.register(dumpjson.dumpjson)

db = dataset.connect(settings.CONNECTION_STRING)

shows=settings.TRACK_TERMS

print shows[0]
for show in shows:
	print show

day = time.localtime(time.time())[7]
hour = time.localtime(time.time())[3]
minute = time.localtime(time.time())[4]
fulltime = str(day) + '-' + str(hour) + '-'+ str(minute)
print fulltime

#global filename
#filename = 'tweets' + fulltime + '.csv'
#target = open(filename, 'w')



class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        #if status.retweeted:
        #    return
	
	
        #description = status.user.description
        loc = status.user.location
        text = status.text
        coords = status.coordinates
        #geo = status.geo Twitter API says this field is deprecated and to use coordinates instead
	lang = status.lang
        #name = status.user.screen_name
        #user_created = status.user.created_at
        #followers = status.user.followers_count
        #id_str = status.id_str
        #created = status.created_at
        #retweets = status.retweet_count
        #bg_color = status.user.profile_background_color
        #blob = TextBlob(text)
        #sent = blob.sentiment

        if coords is not None:
            coords = json.dumps(coords)
		
	shows = settings.TRACK_TERMS
	for show in shows:
		if text.lower().find(show.lower()) != -1 and lang == 'en':
			print "Found a good tweet"
			
			#delimiter = "|~|"
			#print text, delimiter, loc, delimiter, coords
			#target = open(filename, 'w')	
			#target.write(text+delimiter+loc+delimiter+coords)			
			#target.close()

			table = db[settings.TABLE_NAME]
	
        		try:
				table.insert(dict(
					#user_description=description,
					user_location=loc,
					coordinates=coords,
					text=text,
					#geo=geo,
					#user_name=name,
					#user_created=user_created,
					#user_followers=followers,
					#id_str=id_str,
					#created=created,
					#retweet_count=retweets,
					#user_bg_color=bg_color,
					#polarity=sent.polarity,
					#subjectivity=sent.subjectivity,
					))
			except ProgrammingError as err:
				print(err)
		else:
			print "Full show name not in tweet, or not in english"
			

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False



CONSUMER_KEY = 'iFtEL4v7OPKQOYFdtKk4FYR5Q'
CONSUMER_SECRET = 'ec3rJwGb8yrUe76f5evnYf9c3hohecLARHWgTVuJWl4N7QCyJS'
ACCESS_TOKEN = '826083922685657089-jkLYZ5lUMcNqnDBWRdRNyUSm0uCisaI'
ACCESS_TOKEN_SECRET = 'QXp9RorcwvDwzOiyxqQmB5RTsM1yClHHgaGFbZVECaUco'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
#statusupdate = "Testing!5"
#api.update_status(status=statusupdate)

stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(track=settings.TRACK_TERMS)
