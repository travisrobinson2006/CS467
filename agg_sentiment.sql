DROP TABLE IF EXISTS test.agg_sentiment;

CREATE TABLE test.agg_sentiment
(
  ShowName VARCHAR(256) NOT NULL,
  State VARCHAR(256) NOT NULL,
  Sentiment INT NOT NULL
);

INSERT INTO test.agg_sentiment (ShowName, State, Sentiment) VALUES
("Modern Family", "WA", 4),
("Modern Family", "WA", 2),
("Modern Family", "WA", -3),
("TWD", "CA", 5),
("TWD", "CA", 3),
("TWD", "CA", 1),
("TWD", "WA", -1),
("TWD", "WA", 0),a
("Modern Family", "CA", -2)
("GOT", "WA", 2);

SELECT ShowName, State, avg(Sentiment)
FROM test.agg_sentiment
WHERE State='WA'
GROUP BY ShowName;