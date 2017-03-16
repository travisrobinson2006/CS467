--drop if exists
drop table test.locationdata;
drop table test.showdata;

CREATE TABLE test.ShowData
(
  ShowID INT NOT NULL,
  ShowName VARCHAR(256) NOT NULL,
  PRIMARY KEY (ShowID)
);

--create tables
CREATE TABLE test.LocationData
(
  Latitude FLOAT,
  Country VARCHAR(256) ,
  State VARCHAR(256) ,
  County VARCHAR(256) ,
  Longitude FLOAT ,
  TweetText VARCHAR(512),
  UserID INT NOT NULL,
  TweetID INT NOT NULL,
  Sentiment INT ,
  ShowID INT NOT NULL,
  PRIMARY KEY (UserID, TweetID),
  FOREIGN KEY (ShowID) REFERENCES ShowData(ShowID)
);

--Testing queries
SELECT * FROM test.LocationData;
SELECT * FROM test.ShowData;

SELECT * from test.LocationData ld
INNER JOIN test.ShowData sd on sd.ShowID=ld.ShowID
ORDER BY sd.ShowID;

SELECT ShowName FROM test.ShowData
WHERE ShowID=100;

SELECT count(*) FROM test.LocationData ld
INNER JOIN test.ShowData sa on sa.ShowID=ld.ShowID
WHERE Country="USA";