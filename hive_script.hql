use testdb;
INSERT OVERWRITE LOCAL DIRECTORY '/home/robitrav/${hiveconf:dir}'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
SELECT content_name, user_location, avg(score) FROM tweets_2_15 GROUP BY content_name, user_location;
