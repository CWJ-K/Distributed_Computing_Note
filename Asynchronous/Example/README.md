<!-- omit in toc -->
# Table of Contents
- [Introduction](#introduction)
- [Structure](#structure)
  - [Example1](#example1)
  - [Example2](#example2)
- [Command](#command)
  - [Download the text file](#download-the-text-file)
  - [Run Scripts](#run-scripts)

<br />

# Introduction
Create a tool to count the occurrences of a given word from a given text file.

The text file is derived from https://www.gutenberg.org/cache/epub/2600/pg2600.txt .

<br />


# Structure 
## Example1
* Counting the occurrence of only one pattern
```mermaid
graph LR;
    cat -- file lines --> grep;
    grep -- occurrences of substring in each line --> count;
    count -- total sum of all the numbers --> stdout;
```

<br />

## Example2
* Counting the occurrence of multiple patterns
```mermaid
graph LR;
    cat -- file lines --> grep;
    grep -- occurrences of substring in each line --> count;
    count -- total sum of all the numbers of all patterns --> fanout;
    fanout -- results of each pattern --> stdout
```


<br />

# Command
## Download the text file
```linux
    curl -sO https://www.gutenberg.org/cache/epub/2600/pg2600.txt
```

<br />

## Run Scripts

```s
    # e.g. <your_substring> = love
    python example_simple.py -i <your_substring> pg2600.txt
```  

```s
    python example_complex.py -i <your_substring> <your_substring> pg2600.txt
```  