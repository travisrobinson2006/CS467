TRACK_TERMS = ["breaking bad", "big bang theory", 
"games of thrones", 
"the bachelor", 
"law and order SVU", 
"how to get away with murder", 
"modern family", 
"the simpsons", 
"the daily show", 
"the tonight show", 
"la la land", 
"hidden figures",
"big bang theory",
"ncis",
"the walking dead",
"manchester by the sea",
"pretty little liars",
"westworld",
"stranger things",
"the o'reilly factor",
"fox and friends",
"sneaky pete"]
TRACK_TERMS1 = ["trump", "clinton", "sanders", "hillary clinton", "bernie", "donald trump"]
CONNECTION_STRING = "sqlite:///tweets.db"
CSV_NAME = "tweets.csv"
JSON_NAME = "tweets.json"
TABLE_NAME = "election"

try:
    from private import *
except Exception:
    pass
