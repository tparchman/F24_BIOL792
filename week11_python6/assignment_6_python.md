# Python assignment 6, Data Science for Biology
## Topics to cover
- Working with files: Input/Output
- Dictionaries
- More regular expressions
<p>&nbsp;</p>

### I. Intro to dictionary assignment. 
The purpose of this problem is for you to learn and practice how to assign keys and values to a dictionary, to use some dictionary functions to demonstrate that your dictionary is working, and to print out some useful information. We are first going to use the file SG_ref.fasta that is available on the course website. Read in the SG_ref.fasta file from `sys.argv[]` or `glob.glob` and try the following:
<p>&nbsp;</p>

A. You will want to use a `for` loop to go through your file line by line, but for this problem, you will want to access two lines at a time. This is a fairly common situation (and one we have seen before) and here is a hint of one way to do this:

    for Line in IN:
        ID = Line
        Seq = Line.readline()


	
While executing the `for` loop, make one dictionary that has the fasta ids (the line that starts with `>`) as keys, and the sequences themselves as values (Seq as above).  Inside the same loop make a separate dictionary that has the fasta ids as keys and the sequence length as a value (remember that calculating the length of a scalar is easy). Now you should have two dictionaries, and you could do some things with either or both of them.

B. Use the `keys` function to put the keys for your dictionaries into their own lists and print those arrays to make sure your dictionaries are set up the way you want them to be set up. 

C. Use a `for` loop to go through your dictionary and then to print out the fasta Ids and their associated sequence length to an outfile.  This file should have a line for each key-value pair, that is each line should start with a sequence id, which should be followed by the length of the sequence associated with that id.

D. Now use a `for` loop to print out the dictionary in the same way as above, except in this case we want the keys sorted and the dictionary printed in sorted order. What does the difference between these two outputs (C and D) tell you about how dictionaries are organized?

<p>&nbsp;</p>


## II. A an additional dictionary challenge

The `collections` module in Python is a built-in library that provides specialized container data types (lists and dictionaries) beyond the default list, dict, tuple, and set. It includes a variety of container types that are useful in different situations, offering more flexibility and functionality. There are multiple data containers that are used from `collections`. One of these would be especially useful for this problem, and it can be imported as below

```Python

from collections import defaultdict

```

`defaultdict` is a dictionary subclass that provides a default value for a nonexistent key. It can be used to start at 0 and count the number of times a value is changed for the same key, see example below.

```Python
dd = defaultdict(int)  # int() returns 0 by default
ID_Ctr['a'] += 1
print(ID_Ctr['a'])  # Output: 1
print(ID_Ctr['b'])  # Output: 0 (since 'b' does not exist, it defaults to 0)
```

`sample_passerina.fastq` is Illumina sequencing data from a pooled genotyping-by-sequencing library for lazuli buntings (a bird species). There are 190 unique individual names, indicated on the lines that start with `@`, that look like `NVP_CY_48144`. There are many sequences per individual, and lets say we want to count the number of sequences generated for each individual. One way to do this would be to build a dictionary where the individual bird IDs are keys, and each time you hit a key that already exists, you add the value plus 1. Eg., Seq_Ctr[ID] =+ 1. This way, as you go through the file one ID line at a time, the ID can be specified as a dictionary key, and if that key already had a value (an integer in this case), you would add one. So, each time you encounter a value that already exists as a key, the value, which is a count, increases by one. When the dictionary is fully built, you could loop through it by key to print the bird ID and the number of times it occurs in the data, like below.

```Python
for thing in ID_Ctr.keys():
	print(thing, ID_Ctr[thing]) 
```

Use `defaultdict` to build a dictionary that tracks the number of sequences for each individual with data in `sample_passerina.fastq`. Have the script print to screen, or write to a file, the IDs and counts of DNA sequences for each, as below.

    SDC_CY_55115 22
    NVP_CY_48142 51
    NEB_CY_55154 34
    NEW_AM_55139 37
    WBA_AM_43425 26 


