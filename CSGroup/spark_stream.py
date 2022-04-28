import findspark

## look for spark
findspark.init()

from pyspark import SparkContext
from pyspark.streaming import StreamingContext


## create local streaming context with 2 working threads
## & batch interval of 5 seconds
sc = SparkContext("local[2]", "Sample1")
ssc = StreamingContext(sc, 5)

## create Dstream connect to host & port
lines = ssc.socketTextStream("localhost", 3090)

## output results
lines.pprint()

## start computation & wait for termination
ssc.start()
ssc.awaitTermination()