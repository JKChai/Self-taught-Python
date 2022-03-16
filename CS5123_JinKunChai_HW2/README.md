# README

**Author :: Jin Kun Chai** <br>
**Course :: CS 5123** <br>
**Due :: February 27** <br>
**Professor :: Arun Bagavathi** <br>

This is a readme file for CS 5123 assignment 2 which contains the information needed to understand the process for perfoming the 2 given tasks, word count and average word count of line from each file.

This file is broken down into mainly 3 sections: *Task 1*, *Task 2*, and *Miscellaneous*. Both *Task 1* and *Task 2* sections present the command uses to run the MapReduce tasks, overview of the mapper and reducer scripts for running the MapReduce tasks, and show the output returned from these tasks. For details understanding of the scripts, please review the mapper and reducer scripts in which are stored in `task1_HW2` and `task2_HW2` folders. *Miscellaneous* section talks about some findings and take-aways from completing this assignment.

---

## Task 1

This section performs the MapReduce word count task. The python scripts for running both mapper and reducer tasks are including in the `task1_HW2` directory and the output file is named as `task1_output.txt`.

### MapReduce Command

The command used for running the MapReduce task is provided below.

```shell
jchai@hadoop-nn001:~$ hadoop jar /usr/local/hadoop-3.3.0/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar -file /home/jchai/task1_HW2/task1_mapper.py -mapper /home/jchai/task1_HW2/task1_mapper.py -file /home/jchai/task1_HW2/task1_reducer.py -reducer /home/jchai/task1_HW2/task1_reducer.py -input /user/jchai/Assignment2Data -output /user/jchai/task1_output
```

The output log given from the MapReduce task is provided below. There is no exception or errors for this command but do note that there are 2 warning logs in regard to `-file` deprecation and the common `util.NativeCodeLoader`

```shell
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

### Scripts Overview

The mapper script that is use to run mapper and reducer tasks are `task1_mapper.py` and `task1_reducer.py`. Mapper file takes information from each line given from the input file as `sys.stdin`. Each line is then broken down into words and convert into lower case word. The word is later checked if there are any non-alphabetical characters, if so, those non-alphabetical characters will be removed, and if the word does not have any alphabetical characters then it will not be output; otherwise, the word with alphabetical characters are check against the set of stop words. Only those that passes the stop words check will output as key-value pair separated by tab with word as key and assigned numerical 1 as value `(word    1)` for the reducer task.

The reducer script takes the input (key sorted alphabetically by MapReduce) as, `(word    1)`, output structure created from mapper task, and break this down into a string and integer variables, respectively. A `try/exception` statement is use to check if the integer variable has any value. If data exists for both `(word    1) == (word, count)` word and count from the input, then the word is checked against the previous word to see if the number of count is needed to be incremented. This logic can be done due to the input key is being sorted by Hadoop MapReduce intermediate functions. When the current word is not the same as the previous word, then the code will output the key-value pair as `(word, total_word_count)`. Notice that the last line of code is use to capture the last line of word that is not capture by the `if/else` statement.

The output is stored in `task1_output/part-00000` in the hadoop user environment and the last 50 words based on alphabetical order is output to the local home directory as `task2_output.txt`.

### Output

The last 50 words with number of counts based on alphabetical order are output as below.

```shell
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

---

## Task 2

Task 2 performs the word count average based on number of lines for each file. The python scripts for running both mapper and reducer tasks are including in the `task2_HW2` directory and the output file is named as `task2_output.txt`.

### MapReduce Command

The command used for running the MapReduce task is provided below.

```shell
jchai@hadoop-nn001:~$ hadoop jar /usr/local/hadoop-3.3.0/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar -file /home/jchai/task2_HW2/task2_mapper.py -mapper /home/jchai/task2_HW2/task2_mapper.py -file /home/jchai/task2_HW2/task2_reducer.py -reducer /home/jchai/task2_HW2/task2_reducer.py -input /user/jchai/Assignment2Data -output /user/jchai/task2_output
```

The output log given from the MapReduce task is provided below. There is no exception or errors for this command but do note that there are 2 warning logs in regard to `-file` deprecation and the common `util.NativeCodeLoader`.

```shell
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

### Scripts Overview

The mapper script that is use to run mapper and reducer tasks are `task2_mapper.py` and `task2_reducer.py`. Mapper file first starts with collecting the file path by using `os.environ` method referencing the key `'map_input_file'`. To get the file name, the file path directory is broken down into smaller elements stored in a list and extract only the last element, which appear to be the file name. The `for` loop then start by taking information from each line which is given from the input file as `sys.stdin`. Before the processing the word, a `counter` variable is initialize referencing 0. The purpose of the `counter` is to count number of words in a line that will eventually output as a value for the key (i.e., file name) and act as an input for reducer task to perform average computation. The `for` loop is similar to the mapper task for task 1 by broken down line into words and convert into lower case word and remove non-alphabetical characters. The differences between this task and task 1 for mapper process is that the `counter` variable is incremented when the word contains any alphabetical characters. This process is use to count number of words in a line, so that when the `for` loop ended, the `counter` has total number of words for that line and output with the file name as a key-value pair separated by tab, `(file_name     total_words_in_a_line)`, for the reducer task.

Moving down to the reducer task, the logic of the script is similar to the task 1 reducer logic; however, an additional variable is added, `line_count`, to compute number of lines in a file. Note that the input for reducer task is the key-value pair of `(file_name    total_words_in_a_line)`; hence, `line_count` is use to compute total number of lines based on total number of key-value pair when the given keys are the same. Thus, the only differences between both task 1 and task 2 reducer scripts is that the `line_count` and added average computation `avg_wordcount = current_wordcount / line_count` is added to the `if/else` statement and the last `if` process to take account of the last input.

The output is a key-value pair that consists of file name and the average count of words based on total number of line in a file `(file_name    avg_wordcount)`. The results are stored in `task2_output/part-00000` in the hadoop user environment and this output is copy to the local home directory as `task2_output.txt`.

### Output

The results for average words per line in each file is presented as below.

```shell
jchai@hadoop-nn001:~$ hadoop fs -cat task2_output/part-00000
2022-02-25 23:33:06,996 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
CommonSense.txt 9.375188536953242
MoonlightSonata.txt     15.526315789473685
PridePrejudice.txt      8.548668212804834
ScarletStudy.txt        9.069239720713732
SherlockHolmes.txt      8.046126712793379
```

To check if the results output are computed correctly, a set of command processes are run to compute number of rows and number of words for each file as shown below. Taking the number of words divided by number of line for each file returns exactly the same result as shown in the code block above. This indicate that both mapper and reducer scripts written for task 2 should perform correctly.

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

---

## Miscellaneous

This assignment is actually quite simple but running the MapReduce command is a big headache because of sudden unknown errors that was thrown by the program itself, which eventually took me a non-continuous 4 days to complete this assignment. The first issue was found when running the given command where pipeline execution error is thrown and prevent the MapReduce process to run. This is fix by given `-file` as a flag to reference the mapper and reducer scripts. The second issue is the file and directory not found error where the mapper script does not run, which is later solved by the Admin when he found that the mapper python script that I created contains bug that prevent the right output for reducer task. This is fix and run, then another error was thrown telling me that reducer task cannot be run. This is super headache because the reducer script does not contain any bugs, the issue for this is that the script needed to be removed and imported again, if not the MapReduce program will keep throwing errors. With all of this in mind, I then came up with 4 steps to help resolve all current issues when running MapReduce tasks in our CS hadoop cluster.

1. Check your `mapper.py` files and see if the python script can run by entering the command below. If error is being thrown, fix your `mapper.py`.

```shell
<username>@hadoop-nn001:~$ cat ./<All5TextFilesFolderName>/* | python3 mapper.py
```

2. Then check if `reducer.py` is working fine by running the command below. If error is thrown, fix the code in the script.

```shell
<username>@hadoop-nn001:~$ cat ./<All5TextFilesFolderName>/* | python3 mapper.py | sort -k1,1 | python3 reducer.py
```

3. If the command above works fine but MapReduce tasks is still showing errors. Check your path and make sure it is formatted exactly as below. Note that the directory has to be your linux local home directory `/home/<username>` for these 3 flags: `-file`, `-mapper`, & `-reducer`; whereas `-input` & `-output` flags has to be your hadoop home directory `/user/<username>`.

```shell
<username>@hadoop-nn001:~$ hadoop jar /usr/local/hadoop-3.3.0/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar -file /home/<username>/mapper.py -mapper /home/<username>/mapper.py -file /home/<username>/reducer.py -reducer /home/<username>/reducer.py -input /user/<username>/<All5TextFilesFolderName>/ -output /user/<username>/<OutputFolderName>
```

4. If all of the above steps are checked but still receiving the same errors. Remove your `mapper.py` and `reducer.py` from your linux local directory and copy a new one from your local computer to your local linux directory. Then start the process from step 1 again.

All python scripts, input and output files from this assignment is included in the `CS5123_JinKunChai_HW2.zip` folder.
