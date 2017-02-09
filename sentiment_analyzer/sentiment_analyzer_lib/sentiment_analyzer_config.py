import os

TWEET_TEXT_COLUMN = 0
TWEET_STATE_COLUMN = 1

SENTIMENT_DICTIONARY_NAME = "dictionary_final.csv"
SENTIMENT_DICTIONARY_DIR = "sentiment_analyzer_lib"

SENTIMENT_DICTIONARY = os.path.join(SENTIMENT_DICTIONARY_DIR,SENTIMENT_DICTIONARY_NAME)

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