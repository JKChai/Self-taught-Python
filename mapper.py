#!/usr/bin/python3
"""mapper.py"""

# Jin Kun Chai
# Prof. Arun Bagavathi
# CS 5123
# Due FEB 27

import os
import sys

### make change to stop words
# stop_words = "‘ourselves’, ‘hers’, ‘between’, ‘yourself’, ‘but’, ‘again’, ‘there’, " + \ 
#             "‘about’, ‘once’, ‘during’, ‘out’, ‘very’, ‘having’, ‘with’, ‘they’, " + \
#             "‘own’, ‘an’, ‘be’, ‘some’, ‘for’, ‘do’, ‘its’, ‘yours’, ‘such’, ‘into’, " + \
#             "‘of’, ‘most’, ‘itself’, ‘other’, ‘off’, ‘is’, ‘s’, ‘am’, ‘or’, ‘who’, " + \
#             "‘as’, ‘from’, ‘him’, ‘each’, ‘the’, ‘themselves’, ‘until’, ‘below’, " + \
#             "‘are’, ‘we’, ‘these’, ‘your’, ‘his’, ‘through’, ‘don’, ‘nor’, ‘me’, " + \
#             "‘were’, ‘her’, ‘more’, ‘himself’, ‘this’, ‘down’, ‘should’, ‘our’, " + \
#             "‘their’, ‘while’, ‘above’, ‘both’, ‘up’, ‘to’, ‘ours’, ‘had’, ‘she’, " + \
#             "‘all’, ‘no’, ‘when’, ‘at’, ‘any’, ‘before’, ‘them’, ‘same’, ‘and’, " + \
#             "‘been’, ‘have’, ‘in’, ‘will’, ‘on’, ‘does’, ‘yourselves’, ‘then’, " + \
#             "‘that’, ‘because’, ‘what’, ‘over’, ‘why’, ‘so’, ‘can’, ‘did’, ‘not’, " + \
#             "‘now’, ‘under’, ‘he’, ‘you’, ‘herself’, ‘has’, ‘just’, ‘where’, " + \
#             "‘too’, ‘only’, ‘myself’, ‘which’, ‘those’, ‘i’, ‘after’, ‘few’, " + \
#             "‘whom’, ‘t’, ‘being’, ‘if’, ‘theirs’, ‘my’, ‘against’, ‘a’, ‘by’, " + \
#             "‘doing’, ‘it’, ‘how’, ‘further’, ‘was’, ‘here’, ‘than’"
### 
# stop_words = stop_words.replace(u"\u2018", "").replace(u"\u2019", "")
# stop_words = set(stop_words.split(', '))

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



