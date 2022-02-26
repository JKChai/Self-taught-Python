#!/usr/bin/python3

from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    ## input from stdin
    data = read_mapper_output(sys.stdin, separator=separator)
    ## groupby groups multiple word-count pairs by word,
    ## & creates an iterator taht returns consecutive keys and their groups
    ##   current_word - string containing a word (the key)
    ##   group - iterator yielding all ["&lt;current_word&gt;", "&lt;count&gt;"] items
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            print("%s%s%d" % (current_word, separator, total_count))
        except ValueError:
            ## count was not a number, silently discard them
            pass

if __name__ == "__main__":
    main()
