<b>To get access to the master node:</b>

1) Open the email to accept the invite to our project (should be from Google Cloud Platform).

2) Create a Google Cloud Platform account, if you do not already have one.

3) Log into Google Cloud Platform. Next to the text "Google Cloud Platform," click and select our project (the name is "hdp-dataproc")

4) Click the "Products and Services" button (looks like three horizontal lines at the top left of the window). Then scroll down and select "Compute Engine."

5) You should now be brought to a page where you can see the VM instances that comprise our cluster (should be at https://console.cloud.google.com/compute/instances?project=hdp-dataproc&authuser=1). The first one will be name 'tweet-cluster-m' (m for master). To the right of the name, under the "Connect" column, click the "SSH" button. This will open a new window and transfer all keys automatically to SSH into the instance.

6) Once the console is brought up, enter "cd .." followed by "ls" to see the directories for each user.

7) Enter "cd robitrav" followed by "cd CS467". This will bring you to a directory that contains our project files (identical to the ones on our GitHub page). (Alternatively, due to permissions set-up, such as when running the below hive script, it may be best
to clone the repository into your own user directory, via git clone https://github.com/travisrobinson2006/CS467.git).

<b>To collect tweets:</b>

1) Navigate into get_tweets directory

2) Run Python script called run_me_to_get_tweets

This will be done from command line via 'python run_me_to_get_tweets.py' (without the quotes)*
	
This script will call on the tweet_scraper script contained int he acquire_tweets directory, which uses the Twitter streaming 		API to collect some portion of the tweets as they are being sent out. The script will also run the tweet_cleaner script, which 		is also contained in the acquire_tweets directory. The cleaning script will check that the scraped tweets have 				appropriate/usable locations, and cleans up the text a little bit (discarding hashtags, etc). It also converts the tweets to a tab delimited text file, which is generally preferred by HDFS.

The run_me_to_get_tweets script will run an initial cleaning to take care of anything that may have been left behind from the last
	time that the script was run, and then runs the cleaning script once an hour. The tweet_scraper runs the dumpjson script once an 
	hour as well. This is to prevent a large build-up of data that could lead to large processing times if data was only dumped/cleaned once.
	
The dumpjson script will place timestamped json files in the directory unclean_tweets, located in the acquire_tweets directory. The 
	tweet_cleaner script will append all cleaned tweets to the file called tweets_ready_for_use, located inside the clean_tweetsdirectory,
	which in turn is located in the get_tweets directory.	

<b>To get a sentiment score for each tweet</b>

1) In the sentiment_analyzer folder, open the file named "textblobAnalyzer.py". On lines 23 and 24, you will see a place to specify the names of the input file (the tweets to be scores) and the output file (the file that will contain the name of the show a tweet was about, the state it originated from, and its sentiment score). Make sure the name of the input file matches the one you produced in the previous set of steps. You may choose whatever output file name you like.

2) Run the program by entering "python textblobAnalyzer.py" in the command line. Depending on the size of the input file, this may take up to 2 minutes. 

3) In the same folder, you will now find the output file that you named in step 1.

<b>To enter scores file into the Hadoop Distributed File System:</b>

1) To put the output file you just created into the HDFS (distributed across the three worker nodes), type "hdfs dfs -put <i>outputfilename</i> /databases"

2) Check that your file was transferred successfully by entering "hadoop fs -ls databases". The output file name should appear.


<b>To use hive:</b>

1)	From any location within the cluster instance, enter at command line: 'hive;' or 'hive' (different terminals need the semi-colon)**. This will launch the hive shell, where we will be able to use extract the tweet sentiment scores for shows and states from our HQL database.

2)	From the hive command line (denoted by the line starting with 'hive>') enter 'use testdb;' This tells Hive which database we want to use. testdb is the database that is currently storing the sentiment data.

3)	Enter at the hive command line (or copy and paste):
	INSERT OVERWRITE LOCAL DIRECTORY '<directory>***' 
	ROW FORMAT DELIMITED 
	FIELDS TERMINATED BY ','
	SELECT content_name, user_location, avg(score) FROM tweets_2_15 GROUP BY content_name, user_location;
	
	This will create a csv file called 000000_0 (kept in the /home/robitrav/temp directory). This will be the file**** that is used 	by Tableau to generate our maps and state graphs.

Outputting to a CSV file:
INSERT OVERWRITE LOCAL DIRECTORY '/home/robitrav/temp' 
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','
SELECT content_name, user_location, avg(score) FROM tweets_2_15 GROUP BY content_name, user_location;

*To allow yourself the ability to run other programs, navigate directories, etc it's recommended to run the run_me_to_get_tweets
script in the background, via the command line command python 'run_me_to_get_tweets.py &'

**It will most likely be easier to navigate to the main (the CS467) directory and enter at the command line 'hive -hiveconf dir='<your_choice_of_dir>' -f testscript.hql',
where <your_choice_of_dir> is the directory name you'd like to use. This will save the csv file in the directory name you specify. (You do need to specify your
user directory though; for example, my user name is robitrav, so to save to a directory called temp, I'd need to enter at the command line 
hive -hiveconf dir='robitrav/temp' -f testscript.hql).

***Your directory of choice, for testing purposes the directory 'home/robitrav/temp' was used, though due to permissions you may or may not be able to create a file or directory in the robitrav user directory

****The file will actually need to be converted to an Excel file, which can be done by most spreadsheet programs.
