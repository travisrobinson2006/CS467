import glob, os
import csv
import nltk

#http://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/

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

def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
        all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

def extract_features(document):
    word_features = get_word_features(get_words_in_tweets(document))

    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

def main():

    pos_list = get_pos_list()
    neg_list = get_neg_list()
    test_list = get_test_list()

    tweets = []

    for (words, sentiment) in pos_list + neg_list:
        filtered_words = [i.lower() for i in words.split() if len(i) >= 3]
        tweets.append((filtered_words, sentiment))

    #word_features = get_word_features(get_words_in_tweets(tweets))

    training_set = nltk.classify.util.apply_features(extract_features(tweets))
    print training_set


main()