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
TRACK_TERMS1 = ["trump", "clinton", "sanders", "hillary clinton", "bernie", "donald trump"]
CONNECTION_STRING = "sqlite:///tweets.db"
TEMP_CONNECTION_STRING = "sqlite:///temp.db"
CSV_NAME = "tweets.csv"
JSON_NAME = "tweets.json"
TABLE_NAME = "election"
TEMP_TABLE_NAME = "temp_table"

try:
    from private import *
except Exception:
    pass
