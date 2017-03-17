use testdb;
DROP TABLE IF EXISTS testdb.nbScores;
CREATE EXTERNAL TABLE IF NOT EXISTS testdb.nbScores ( content_name String COMMENT 'name of the show/movie/book/etc', user_location String COMMENT 'abbreviated state', score Double COMMENT 'sentiment score' ) 
--TBLPROPERTIES ("skip.header.line.count"="1") 
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde' WITH SERDEPROPERTIES ( "separatorChar" = "\t" ) 
LOCATION '/database';
