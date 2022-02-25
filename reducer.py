#!/usr/bin/python3
"""reducer.py"""

# Jin Kun Chai
# Prof. Arun Bagavathi
# CS 5123
# Due FEB 27

## import modules
from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
    # remove leading and trailing whitespace
    # Similar to mapper, reducer also processes the input line by line from the intermediate mapper output
    line = line.strip()
    # parse the input we got from mapper.py
    word, count = line.split('\t', 1) 

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    # The below statements increments the counter only if the word from "line" is the current_word
    # Else writes the current_word and its count along with updating the current_word
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            print('%s\t%s' % (current_word, current_count))
        current_count = count
        current_word = word

# do not forget to output the last word if needed!
if current_word == word:
    print('%s\t%s' % (current_word, current_count))

