#!/usr/bin/python3

# Jin Kun Chai
# Prof. Arun Bagavathi
# CS 5123
# Due FEB 27

###########
## TASK 1
###########

## import modules
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

## Data from each line is collected from the file
for line in sys.stdin:

    ## remove leading & trailing whitespace 
    line = line.strip()
    ## split line into list based on whitespace
    words = line.split()

    ## iterate each word from list of words
    ## this loop does 4 things
    ## 1. Convert uppercase to lowercase
    ## 2. Remove non-alphabetical characters
    ## 3. Ignore empty word with continue statement
    ## 4. Prevent stopwords to output
    for word in words:
        ## convert upper case letter to lower case letter
        word = word.lower()

        ## only keep alphabetical character such as 
        ## removing numerics & symbols & spaces character
        ## restrict to small or big cap letters
        word = re.sub("[^a-zA-Z]+", '', word)

        ## if statement below remove words that return nothing which
        ## cause by missing alphabetical words after regex filtering
        ## continue statement break the code process after its line
        ## then run from the for loop -- for word in words:
        ## this 2-line codes prevent empty word to output        
        if len(word) <= 1:
            continue      

        ## prevent stop words from output
        ## check the sets given from above
        if word not in stop_words:
            ## output key-value as (word, 1) 
            print('%s\t%s' % (word, 1))

##################################### End of Line #####################################
