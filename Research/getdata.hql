INSERT OVERWRITE LOCAL DIRECTORY '/home/rohangokhale/TwitterSentimentAnalysis/CS467/Research/Results'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
SELECT content_name, user_location, avg(score) FROM testdb.nbscores GROUP BY content_name, user_location;
