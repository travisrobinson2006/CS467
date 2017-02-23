-- drop table testdb.tweets_alldata

CREATE EXTERNAL TABLE IF NOT EXISTS testdb.tweets-2-15 (
content_name String COMMENT 'name of the show/movie/book/etc',
user_location String COMMENT 'abbreviated state',
score Double COMMENT 'sentiment score'
)
--TBLPROPERTIES ("skip.header.line.count"="1")
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde' WITH SERDEPROPERTIES ( "separatorChar" = "\t" )
LOCATION '/user/rohangokhale/databases';
