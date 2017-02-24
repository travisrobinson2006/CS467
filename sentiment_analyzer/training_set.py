import glob, os
import csv
import nltk

#Source http://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/

def get_pos_list():
    with open('pos_set.csv', 'rU') as pos_list:
        reader = csv.reader(pos_list)
        mylist = map(tuple, reader)
    return mylist

def get_neg_list():
    with open('neg_set.csv', 'rU') as neg_list:
        reader = csv.reader(neg_list)
        mylist = map(tuple, reader)
    return mylist

def get_test_list():
    with open('test_set.csv', 'rU') as test_list:
        reader = csv.reader(test_list)
        mylist = map(tuple, reader)
    return mylist

#function to remove all non-ascii characters from the tweet text
def stripNonAscii(string):
        stripped = (c for c in string if 0 < ord(c) < 127)
        return ''.join(stripped)

def downsize(list, tweets):
    for words, sentiment in list:
        filtered_words = [i.lower() for i in words.split() if len(i) >= 3]
        tweets.append((filtered_words, sentiment))
    return tweets


def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
        all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

def get_extract_features(document, word_features):
    features = {}
    document_words = set(document)
    for i in document:
        document_words.add(i)
        for word in word_features:
            features['contains(%s)' % word] = (word in document_words)
    return features

def main():

    pos_list = get_pos_list()
    neg_list = get_neg_list()
    test_list = get_test_list()

    tweets = []
    test_tweets = []
    agg_list = pos_list + neg_list

    tweets = downsize(agg_list, tweets)
    test_tweets = downsize(test_list, test_tweets)

    word_features = get_word_features(get_words_in_tweets(tweets))

    def extract_features(document):
        document_words = set(document)
        features = {}
        for word in word_features:
            features['contains(%s)' % word] = (word in document_words)
        return features

    training_set = nltk.classify.apply_features(extract_features, tweets)
    test_set = nltk.classify.apply_features(extract_features, test_tweets)

    classifier = nltk.NaiveBayesClassifier.train(training_set)
    print classifier.show_most_informative_features(25)

    tweet = 'This house is great'
    #print extract_features(tweet.split())
    sentiment = classifier.classify(extract_features(tweet.split()))
    print "'This house is great': "
    print sentiment

    tweet = 'Your song is annoying'
    #print extract_features(tweet.split())
    sentiment = classifier.classify(extract_features(tweet.split()))
    print "'Your song is annoying': "
    print sentiment

    accuracy = nltk.classify.accuracy(classifier, test_set)
    print "Accuracy against test_set:"
    print accuracy

    #output to big file
    '''
    inputfilename = "tweets_ready_for_use"
    outputfilename = "chase_test"

    # define columns
    showCol = 0
    textCol = 1
    stateCol = 2

    outputfile = open(outputfilename, 'w')

    with open(inputfilename, 'r') as tweetsfile:
        reader = csv.reader(tweetsfile, delimiter='\t')
        for row in reader:
            fixedText = stripNonAscii(row[textCol])
            sentiment = classifier.classify(extract_features(fixedText.split()))
            outputfile.write(row[showCol] + '\t' + row[stateCol] + '\t' + str(sentiment) + '\n')
    '''

main()