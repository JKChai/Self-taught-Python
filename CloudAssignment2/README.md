# README

This is a readme file for CS 5123 assignment 2, due on February 27.

## Task 1

Command use to run the MapReduce task.

```linux
jchai@hadoop-nn001:~$ hadoop jar /usr/local/hadoop-3.3.0/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar -file /home/jchai/task1_HW2/task1_mapper.py -mapper /home/jchai/task1_HW2/task1_mapper.py -file /home/jchai/task1_HW2/task1_reducer.py -reducer /home/jchai/task1_HW2/task1_reducer.py -input /user/jchai/Assignment2Data -output /user/jchai/task1_output
```

```log
2022-02-25 23:10:57,398 WARN streaming.StreamJob: -file option is deprecated, please use generic option -files instead.
2022-02-25 23:10:57,502 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
packageJobJar: [/home/jchai/task1_HW2/task1_mapper.py, /home/jchai/task1_HW2/task1_reducer.py, /tmp/hadoop-unjar2296707696736324882/] [] /tmp/streamjob2456682865044643970.jar tmpDir=null
2022-02-25 23:10:58,341 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at hadoop-nn001.cs.okstate.edu/192.168.122.2:8032
2022-02-25 23:10:58,520 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at hadoop-nn001.cs.okstate.edu/192.168.122.2:8032
2022-02-25 23:10:58,804 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/jchai/.staging/job_1639774939292_0809
2022-02-25 23:10:59,209 INFO mapred.FileInputFormat: Total input files to process : 5
2022-02-25 23:10:59,302 INFO mapreduce.JobSubmitter: number of splits:5
2022-02-25 23:10:59,494 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1639774939292_0809
2022-02-25 23:10:59,494 INFO mapreduce.JobSubmitter: Executing with tokens: []
2022-02-25 23:10:59,733 INFO conf.Configuration: resource-types.xml not found
2022-02-25 23:10:59,734 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2022-02-25 23:10:59,829 INFO impl.YarnClientImpl: Submitted application application_1639774939292_0809
2022-02-25 23:10:59,886 INFO mapreduce.Job: The url to track the job: http://hadoop-nn001.cs.okstate.edu:8088/proxy/application_1639774939292_0809/
2022-02-25 23:10:59,888 INFO mapreduce.Job: Running job: job_1639774939292_0809
2022-02-25 23:11:06,000 INFO mapreduce.Job: Job job_1639774939292_0809 running in uber mode : false
2022-02-25 23:11:06,002 INFO mapreduce.Job:  map 0% reduce 0%
2022-02-25 23:11:11,107 INFO mapreduce.Job:  map 100% reduce 0%
2022-02-25 23:11:16,160 INFO mapreduce.Job:  map 100% reduce 100%
2022-02-25 23:11:16,176 INFO mapreduce.Job: Job job_1639774939292_0809 completed successfully
2022-02-25 23:11:16,326 INFO mapreduce.Job: Counters: 55
        File System Counters
                FILE: Number of bytes read=1299225
                FILE: Number of bytes written=4208813
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=1580224
                HDFS: Number of bytes written=145514
                HDFS: Number of read operations=20
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=2
                HDFS: Number of bytes read erasure-coded=0
        Job Counters
                Launched map tasks=5
                Launched reduce tasks=1
                Data-local map tasks=4
                Rack-local map tasks=1
                Total time spent by all maps in occupied slots (ms)=73800
                Total time spent by all reduces in occupied slots (ms)=13665
                Total time spent by all map tasks (ms)=14760
                Total time spent by all reduce tasks (ms)=2733
                Total vcore-milliseconds taken by all map tasks=14760
                Total vcore-milliseconds taken by all reduce tasks=2733
                Total megabyte-milliseconds taken by all map tasks=75571200
                Total megabyte-milliseconds taken by all reduce tasks=13992960
        Map-Reduce Framework
                Map input records=29503
                Map output records=116341
                Map output bytes=1066537
                Map output materialized bytes=1299249
                Input split bytes=681
                Combine input records=0
                Combine output records=0
                Reduce input groups=13355
                Reduce shuffle bytes=1299249
                Reduce input records=116341
                Reduce output records=13355
                Spilled Records=232682
                Shuffled Maps =5
                Failed Shuffles=0
                Merged Map outputs=5
                GC time elapsed (ms)=101
                CPU time spent (ms)=9480
                Physical memory (bytes) snapshot=2028445696
                Virtual memory (bytes) snapshot=38307737600
                Total committed heap usage (bytes)=4750049280
                Peak Map Physical memory (bytes)=362893312
                Peak Map Virtual memory (bytes)=6387412992
                Peak Reduce Physical memory (bytes)=271564800
                Peak Reduce Virtual memory (bytes)=6389358592
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Input Format Counters
                Bytes Read=1579543
        File Output Format Counters
                Bytes Written=145514
2022-02-25 23:11:16,331 INFO streaming.StreamJob: Output directory: /user/jchai/task1_output
```

Final solutions for the last 50 words with number of counts based on alphabetical order for all 5 text files given as input. 

```bash
jchai@hadoop-nn001:~$ hadoop fs -cat task1_output/part-00000 | tail -n 50
2022-02-25 23:14:14,018 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
yesi    1
yesif   2
yesit   1
yesof   1
yesterday       24
yesterdayde     1
yesterdays      2
yesterdaythats  1
yesthat 2
yesthe  2
yesthere        1
yet     195
yew     12
yield   4
yielded 2
yielding        2
yieldingcertainly       1
yoked   1
yonder  10
yonderhe        1
york    8
yorkers 1
yorkshire       2
youand  2
youare  1
yoube   1
youbut  2
youd    1
youhad  1
youhow  1
youll   14
youmr   1
young   207
younge  4
younger 36
youngest        15
youngshe        1
youngster       1
youngsters      1
youre   7
yourselfand     1
youth   16
youths  2
youve   7
zeal    2
zigzag  1
zigzagged       1
zion    2
zip     1
zoology 1
```

## Task 2

Command use to run the MapReduce task.

```bash
jchai@hadoop-nn001:~$ hadoop jar /usr/local/hadoop-3.3.0/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar -file /home/jchai/task2_HW2/task2_mapper.py -mapper /home/jchai/task2_HW2/task2_mapper.py -file /home/jchai/task2_HW2/task2_reducer.py -reducer /home/jchai/task2_HW2/task2_reducer.py -input /user/jchai/Assignment2Data -output /user/jchai/task2_output
```

```log
2022-02-25 23:32:27,703 WARN streaming.StreamJob: -file option is deprecated, please use generic option -files instead.
2022-02-25 23:32:27,814 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
packageJobJar: [/home/jchai/task2_HW2/task2_mapper.py, /home/jchai/task2_HW2/task2_reducer.py, /tmp/hadoop-unjar5187354964760640113/] [] /tmp/streamjob695395464843304363.jar tmpDir=null
2022-02-25 23:32:28,704 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at hadoop-nn001.cs.okstate.edu/192.168.122.2:8032
2022-02-25 23:32:28,888 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at hadoop-nn001.cs.okstate.edu/192.168.122.2:8032
2022-02-25 23:32:29,153 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/jchai/.staging/job_1639774939292_0813
2022-02-25 23:32:29,613 INFO mapred.FileInputFormat: Total input files to process : 5
2022-02-25 23:32:29,709 INFO mapreduce.JobSubmitter: number of splits:5
2022-02-25 23:32:29,902 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1639774939292_0813
2022-02-25 23:32:29,902 INFO mapreduce.JobSubmitter: Executing with tokens: []
2022-02-25 23:32:30,175 INFO conf.Configuration: resource-types.xml not found
2022-02-25 23:32:30,176 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2022-02-25 23:32:30,259 INFO impl.YarnClientImpl: Submitted application application_1639774939292_0813
2022-02-25 23:32:30,337 INFO mapreduce.Job: The url to track the job: http://hadoop-nn001.cs.okstate.edu:8088/proxy/application_1639774939292_0813/
2022-02-25 23:32:30,340 INFO mapreduce.Job: Running job: job_1639774939292_0813
2022-02-25 23:32:35,446 INFO mapreduce.Job: Job job_1639774939292_0813 running in uber mode : false
2022-02-25 23:32:35,451 INFO mapreduce.Job:  map 0% reduce 0%
2022-02-25 23:32:40,566 INFO mapreduce.Job:  map 100% reduce 0%
2022-02-25 23:32:45,617 INFO mapreduce.Job:  map 100% reduce 100%
2022-02-25 23:32:45,634 INFO mapreduce.Job: Job job_1639774939292_0813 completed successfully
2022-02-25 23:32:45,768 INFO mapreduce.Job: Counters: 56
        File System Counters
                FILE: Number of bytes read=678868
                FILE: Number of bytes written=2968093
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=1580224
                HDFS: Number of bytes written=182
                HDFS: Number of read operations=20
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=2
                HDFS: Number of bytes read erasure-coded=0
        Job Counters
                Killed map tasks=1
                Launched map tasks=5
                Launched reduce tasks=1
                Data-local map tasks=4
                Rack-local map tasks=1
                Total time spent by all maps in occupied slots (ms)=67705
                Total time spent by all reduces in occupied slots (ms)=11925
                Total time spent by all map tasks (ms)=13541
                Total time spent by all reduce tasks (ms)=2385
                Total vcore-milliseconds taken by all map tasks=13541
                Total vcore-milliseconds taken by all reduce tasks=2385
                Total megabyte-milliseconds taken by all map tasks=69329920
                Total megabyte-milliseconds taken by all reduce tasks=12211200
        Map-Reduce Framework
                Map input records=29503
                Map output records=29503
                Map output bytes=619856
                Map output materialized bytes=678892
                Input split bytes=681
                Combine input records=0
                Combine output records=0
                Reduce input groups=5
                Reduce shuffle bytes=678892
                Reduce input records=29503
                Reduce output records=5
                Spilled Records=59006
                Shuffled Maps =5
                Failed Shuffles=0
                Merged Map outputs=5
                GC time elapsed (ms)=88
                CPU time spent (ms)=7190
                Physical memory (bytes) snapshot=2075815936
                Virtual memory (bytes) snapshot=38308859904
                Total committed heap usage (bytes)=4718592000
                Peak Map Physical memory (bytes)=367792128
                Peak Map Virtual memory (bytes)=6386556928
                Peak Reduce Physical memory (bytes)=274980864
                Peak Reduce Virtual memory (bytes)=6394429440
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Input Format Counters
                Bytes Read=1579543
        File Output Format Counters
                Bytes Written=182
2022-02-25 23:32:45,768 INFO streaming.StreamJob: Output directory: /user/jchai/task2_output
```

### Word Count Average For Each File

Below Proves that the equation in `mapper.py` performs correctly by returning the correct number of rows and total word counts for each file with file name.

```bash
jchai@hadoop-nn001:~$ hadoop fs -cat task2_output/part-00000
2022-02-25 21:36:02,935 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
hdfs://hadoop-nn001.cs.okstate.edu:9000/user/jchai/Assignment2Data/CommonSense.txt      2652
hdfs://hadoop-nn001.cs.okstate.edu:9000/user/jchai/Assignment2Data/MoonlightSonata.txt  95
hdfs://hadoop-nn001.cs.okstate.edu:9000/user/jchai/Assignment2Data/PridePrejudice.txt   14229
hdfs://hadoop-nn001.cs.okstate.edu:9000/user/jchai/Assignment2Data/ScarletStudy.txt     5156
hdfs://hadoop-nn001.cs.okstate.edu:9000/user/jchai/Assignment2Data/SherlockHolmes.txt   7371
jchai@hadoop-nn001:~$ wc -l Assignment2Data/*
   2652 Assignment2Data/CommonSense.txt
     94 Assignment2Data/MoonlightSonata.txt
  14229 Assignment2Data/PridePrejudice.txt
   5155 Assignment2Data/ScarletStudy.txt
   7370 Assignment2Data/SherlockHolmes.txt
  29500 total

jchai@hadoop-nn001:~$ hadoop fs -cat task2_output/part-00000
2022-02-25 21:49:25,319 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
CommonSense.txt 24863
MoonlightSonata.txt     1475
PridePrejudice.txt      121639
ScarletStudy.txt        46761
SherlockHolmes.txt      59308
jchai@hadoop-nn001:~$ cp task2_mapper.py task2_mapper_localtest.py
jchai@hadoop-nn001:~$ ls
Assignment2Data  jk_mapper.py  last50wc_task1.txt  mapper.py  reducer.py  SimpleInput.txt  SimpleOutput  task2_mapper_localtest.py  task2_mapper.py  task2_reducer.py  testFile  try_reducer.py
jchai@hadoop-nn001:~$ nano task2_mapper_localtest.py
jchai@hadoop-nn001:~$ cat Assignment2Data/CommonSense.txt | python3 task2_mapper_localtest.py | sort -k1,1 | python3 task2_reducer.py
filename        24863
jchai@hadoop-nn001:~$ cat Assignment2Data/MoonlightSonata.txt | python3 task2_mapper_localtest.py | sort -k1,1 | python3 task2_reducer.py
filename        1475
jchai@hadoop-nn001:~$ cat Assignment2Data/PridePrejudice.txt | python3 task2_mapper_localtest.py | sort -k1,1 | python3 task2_reducer.py
filename        121639
jchai@hadoop-nn001:~$ cat Assignment2Data/ScarletStudy.txt | python3 task2_mapper_localtest.py | sort -k1,1 | python3 task2_reducer.py
filename        46761
jchai@hadoop-nn001:~$ cat Assignment2Data/SherlockHolmes.txt | python3 task2_mapper_localtest.py | sort -k1,1 | python3 task2_reducer.py
filename        59308
```

```bash
jchai@hadoop-nn001:~$ hadoop fs -cat task2_output/part-00000
2022-02-25 23:33:06,996 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
CommonSense.txt 9.375188536953242
MoonlightSonata.txt     15.526315789473685
PridePrejudice.txt      8.548668212804834
ScarletStudy.txt        9.069239720713732
SherlockHolmes.txt      8.046126712793379
```
