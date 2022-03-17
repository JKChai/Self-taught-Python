#!/usr/bin/python3
"""mapper.py"""

# Jin Kun Chai
# Prof. Arun Bagavathi
# CS 5123
# Due FEB 27

import os
import sys
import re

## stop words
stop_words = {'just', 'while', 'me', 'further', 'no', 'any', 'up', 
            'whom', 'above', 'a', 'are', 'the', 'where', 'him', 'our', 
            'off', 'themselves', 'their', 'once', 'don', 'on', 'against', 
            'them', 'hers', 'after', 'will', 'himself', 'who', 'there', 
            'be', 'or', 'an', 'few', 'in', 'until', 'same', 'my', 'then', 
            'some', 'because', 'having', 'you', 'own', 'here', 'ours', 'does', 
            'he', 'below', 'she', 'only', 'out', 'again', 'most', 'its', 'his', 
            'being', 'theirs', 'been', 'is', 'ourselves', 'during', 'has', 'for', 
            'each', 'now', 'herself', 'very', 'when', 'that', 'did', 'am', 'yours', 
            'this', 'too', 'about', 'by', 'can', 'nor', 'yourselves', 'how', 'between', 
            'both', 'i', 'at', 'so', 'into', 'as', 'those', 'myself', 'but', 'should', 
            't', 'other', 'under', 'have', 'through', 'your', 'not', 'down', 'we', 
            'which', 'of', 'had', 'itself', 'yourself', 's', 'doing', 'before', 
            'what', 'do', 'and', 'her', 'to', 'all', 'from', 'than', 'these', 'more', 
            'they', 'were', 'why', 'if', 'such', 'it', 'over', 'with', 'was'}

## In hadoop environment
# for line in sys.stdin:
#     line = line.strip()
#     words = line.split()
#     for word in words:
#         print('%s\t%s' % (word, 1))

## In local environment
# i = 0
filename = os.environ['./stupidInput.txt']
print(filename)


# with open('./stupidInput.txt') as file:
#     for line in file:


#         ## remove all whitespace 
#         line = line.strip()
#         ## split line into list based on whitespace
#         words = line.split()

#         ## 
#         for word in words:
#             ## convert upper case to lower case
#             word = word.lower()
#             ## only keep alphabetical character
#             word = re.sub("[^a-zA-Z]+", '', word)
#             ## prevent stop words from output
#             if word not in stop_words:
#                 print('%s\t%s' % (word, 1))
#                 with open('stupidOutput.txt', 'a') as Ofile:
#                     Ofile.write('%s\t%s' % (word, 1))
#                     Ofile.write('\n')

        # i+=1
        # if i == 4:
        #     break

