#!/usr/bin/python3

# Jin Kun Chai
# Prof. Arun Bagavathi
# CS 5123
# Due FEB 27

###########
## TASK 2
###########

## import modules
import sys

## intialize variables
current_filename = None
current_wordcount = 0
filename = None
line_count = 1

## collect each line of information from each file
for line in sys.stdin:
    # remove leading and trailing whitespace
    # Similar to mapper, reducer also processes the input line by line from the intermediate mapper output
    line = line.strip()
    # parse the input we got from mapper.py
    filename, wordcount = line.split('\t', 1) 

    # convert wordcount (currently a string) to int
    try:
        wordcount = int(wordcount)
    except ValueError:
        # wordcount was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: filename) before it is passed to the reducer
    # The below statements increments the counter only if the filename from "line" is the filename
    # this is performed for both number of lines from the file & number of words 
    # Else writes the current_filename and its count along with updating the current_filename
    # calculate average word of each line from each file & reset all initialize variables
    if current_filename == filename:
        current_wordcount += wordcount
        line_count += 1

    else:
        ## perform average computation
        current_wordcount = current_wordcount / line_count
        if current_filename:
            # write result to STDOUT
            print('%s\t%s' % (current_filename, current_wordcount))
        current_wordcount = wordcount
        current_filename = filename
        line_count = 1

# do not forget to output the last file name if needed!
if current_filename == filename:
    ## perform average computation
    current_wordcount = current_wordcount / line_count
    print('%s\t%s' % (current_filename, current_wordcount))

##################################### End of Line #####################################
