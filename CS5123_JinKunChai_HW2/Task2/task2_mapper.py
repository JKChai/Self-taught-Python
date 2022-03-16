#!/usr/bin/python3

# Jin Kun Chai
# Prof. Arun Bagavathi
# CS 5123
# Due FEB 27

###########
## TASK 2
###########

## import modules
import os
import sys
import re

## hard code stop-words
## this is use for removing words that are in this set
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

## collect file name from path
## file name is located at the end of list
## which is done after the split()
filepath = os.environ['map_input_file']
filepath = filepath.split('/')
filename = filepath[-1]

## Data from each line is collected from the file
for line in sys.stdin:

    ## remove leading & trailing whitespace 
    line = line.strip()
    ## split line into list based on whitespace
    words = line.split()

    ## iterate each word from list of words
    ## this loop does 3 things
    ## 1. Convert uppercase to lowercase
    ## 2. Remove non-alphabetical characters
    ## 3. count word if there is at least 1 alphabetical character

    ## initialize counter use for count number of words in a line
    counter = 0

    for word in words:
        ## convert upper case letter to lower case letter
        word = word.lower()

        ## only keep alphabetical character such as 
        ## removing numerics & symbols & spaces character
        ## restrict to small or big cap letters
        word = re.sub("[^a-zA-Z]+", '', word)

        ## if statement below remove words that return nothing which
        ## cause by missing alphabetical word after regex filtering
        ## increment word only is alphabtical word
        ## this 2-line codes prevent empty word to output        
        if len(word) > 0:
            counter += 1      

    ## print by line
    ## output as (<file_name>, <number of word in line>)
    print('%s\t%s' % (filename, counter))

##################################### End of Line #####################################
