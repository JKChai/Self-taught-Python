#!/usr/bin/python3
"""mapper.py"""

# Jin Kun Chai
# Prof. Arun Bagavathi
# CS 5123
# Due FEB 27

## Run hadoop 
## mapred streaming -file /home/jchai/mapper.py -mapper /home/jchai/mapper.py -file /home/jchai/reducer.py -reducer /home/jchai/reducer.py -input /user/jchai/MapReduceTempFolder/stupidInput.txt -output /user/jchai/simpleOutput1

## import modules
import os
import sys
import re

## hard code stop-words
stop_words = {'just', 'while', 'me', 'further', 'no', 'any', 'up', 
            'whom', 'above', 'a', 'are', 'the', 'where', 'him', 'our', 
            'off', 'themselves', 'their', 'once', 'don', 'on', 'against', 
            'them', 'hers', 'after', 'will', 'himself', 'who', 'there', 
            'be', 'or', 'an', 'few', 'in', 'until', 'same', 'my', 'then', 
            'some', 'because', 'having', 'you', 'own', 'here', 'ours', 
            'does', 'he', 'below', 'she', 'only', 'out', 'again', 'most', 
            'its', 'his', 'being', 'theirs', 'been', 'is', 'ourselves', 
            'during', 'has', 'for', 'each', 'now', 'herself', 'very', 'when', 
            'that', 'did', 'am', 'yours', 'this', 'too', 'about', 'by', 'can', 
            'nor', 'yourselves', 'how', 'between', 'both', 'i', 'at', 'so', 
            'into', 'as', 'those', 'myself', 'but', 'should', 't', 'other', 
            'under', 'have', 'through', 'your', 'not', 'down', 'we', 'which', 
            'of', 'had', 'itself', 'yourself', 's', 'doing', 'before', 'what', 
            'do', 'and', 'her', 'to', 'all', 'from', 'than', 'these', 'more', 
            'they', 'were', 'why', 'if', 'such', 'it', 'over', 'with', 'was'}

## collect each line from the given file
for line in sys.stdin:

    ## remove all whitespace 
    line = line.strip()
    ## split line into list based on whitespace
    words = line.split()

    ## iterate each word from list of words
    ## this loop does 3 things
    ## 1. Convert uppercase to lowercase
    ## 2. Remove non-alphabetical characters
    ## 3. Prevent stopwords to output
    for word in words:
        ## convert upper case to lower case
        word = word.lower()
        ## only keep alphabetical character
        word = re.sub("[^a-zA-Z]+", '', word)
        ## prevent stop words from output
        if word not in stop_words:
            ## output key-value as (word, 1) 
            print('%s\t%s' % (word, 1))
