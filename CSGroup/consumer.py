import sys
import findspark

findspark.init()

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

sc = SparkContext('local[*]')

ssc = StreamingContext(sc, 2)
lines = ssc.socketTextStream('localhost', 3090)

lines.pprint()

ssc.start()
ssc.awaitTermination()