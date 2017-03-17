use testdb;
INSERT OVERWRITE LOCAL DIRECTORY '${hiveconf:cwd}/${hiveconf:dir}'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
SELECT content_name, user_location, avg(score) FROM nbscores GROUP BY content_name, user_location;