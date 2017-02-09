#Travis Robinson
#Centaurus
#CS467
#Oregon State University

BASE_FILE_NAME_UNCLEAN = "tweets"
UNCLEANED_TWEETS_DIRECTORY = "acquire_tweets/unclean_tweets"

BASE_FILE_NAME_CLEAN = "tweets_ready_for_use"
CLEANED_TWEETS_DIRECTORY = "clean_tweets"

LIST_OF_CLEANED_TWEET_FILES = "list_of_cleaned_tweet_files"

SYMBOLS_TO_DROP = '@#'

STATE_ABBREVIATIONS = {#will convert location to value, allows for multiple ways user may put in location in other words states may have multiple abbreviations so we use value for standardization
	'ALABAMA':'AL',
	'ALASKA':'AK',
	'ARIZONE':'AZ',
	'ARKANSAS':'AR',
	'CALIFORNIA':'CA',
	'COLORADA':'CO',
	'CONNECTICUT':'CT',
	'DELAWARE':'DE',
	'DISTRICT OF COLUMBIA':'DC',
	'FLORIDA':'FL',
	'GEORGIA':'GA',
	'HAWAII':'HI',
	'IDAHO':'ID',
	'ILLINOIS':'IL',
	'INDIANA':'IN',
	'IOWA':'IA',
	'KANSAS':'KS',
	'KENTUCKY':'KY',
	'LOUISIANA':'LA',
	'MAINE':'ME',
	'MARYLAND':'MD',
	'MASSACHUTTES':'MA',
	'MICHIGAN':'MI',
	'MINNESOTA':'MN',
	'MISSISSIPPI':'MS',
	'MISSOURI':'MO',
	'MONTANA':'MT',
	'NEBRASKA':'NE',
	'NEVADA':'NV',
	'NEW HAMPSHIRE':'NH',
	'NEW JERSEY':'NJ',
	'NEW MEXICO':'NM',
	'NEW YORK':'NY',
	'NORTH CAROLINA':'NC',
	'N CAROLINA':'NC',
	'NORTH DAKOTA':'ND',
	'N DAKOTA':'ND',
	'OHIO':'OH',
	'OKLAHOMA':'OK',
	'OREGON':'OR',
	'PENNSYLVANIA':'PA',
	'RHODE ISLAND':'RI',
	'SOUTH CAROLINA':'SC',
	'S CAROLINA':'SC',
	'SOUTH DAKOTA':'SD',
	'S DAKOTA':'SD',
	'TENNESSEE':'TN',
	'TEXAS':'TX',
	'UTAH':'UT',
	'VERMONT':'VT',
	'VIRGINIA':'VA',
	'WASHINGTON':'WA',
	'WEST VIRGINIA':'WV',
	'W VIRGINIA':'WV',
	'WISCONSIN':'WI',
	'WYOMING':'WY'
}

COUNTRY_ABBREVIATIONS = {
	'UNITED STATES':'US',
	'UNITED SATES OF AMERICA':'US',
	'USA':'US',
}

TRACK_TERMS = ["breaking bad", "big bang theory", 
"games of thrones", 
"the bachelor", 
"law and order SVU", 
"how to get away with murder", 
"modern family", 
"simpsons", 
"daily show", 
"tonight show", 
"la la land", 
"hidden figures",
"big bang theory",
"ncis",
"walking dead",
"manchester by the sea",
"pretty little liars",
"westworld",
"stranger things",
"o'reilly factor",
"fox and friends",
"sneaky pete"]