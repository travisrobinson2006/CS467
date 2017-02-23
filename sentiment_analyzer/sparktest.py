from pyspark.context import SparkContext
from pyspark.sql import functions as functions
from pyspark.sql import SQLContext as sqlContext
from pyspark.sql import SparkSession as SparkSession

sc = SparkContext()
#spark = SparkSession.builder()
tweets = sc.textFile("textblobScores.txt")

print("Total Tweets: ")
print tweets.count()
hfTweets = tweets.filter(lambda x: "hidden figures" in x)
print("Tweets about hidden figures: ")
print hfTweets.count()

#hfdataframe = sqlContext.createDataFrame(hfTweets)
#print("Average score: ")
#print functions.sum(hfTweets[2])
