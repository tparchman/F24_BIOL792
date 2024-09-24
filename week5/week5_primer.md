# Why Python ?

One goal of this course is to introduce biologists without any, or much, prior programming experience to a language that can be useful for their needs. The choice of the first programming language to learn may not be as important as you think; once you have learned one, learning others will be much much easier, and you are nearly guaranteed to utilize additional languages at some point in your career. Nonetheless, the two scripting languages that have been most heavily used in bioinformatics and data science are **Perl** and **Python**. I had primarily used **Perl** for my needs, and have taught this course with Perl in the past. However, given a general shift in usage trends and training opportunities, beginning this semester, Ive decided to shift to Python both for teaching and for research purposes. There are a number of reasons for this:

- It is one of the most common languages used in biology and other fields of science. Thus, you will be able to find a lot of documentation, guidance, examples, and opinion on the web (see useful resources at the bottom of this page).
- It has excellent capabilities for manipulating text, suiting it well to bioinformatics and data science more generally.
- It uses consistent syntax, which makes learning specific code relatively easy.
- It has many built in libraries to facilitate common tasks
- Python is very widely used, across science, industry, and life in general 

<p>&nbsp;</p>

# Getting started with Python. 

## Topics to cover
- installing/updating python
- writing your first python script(s), `print` statements
- introduction to variable types in python
- Haddock and Dunn chapter 8, and first few pages of chapter 9

# 1. Installing/updating to python 3 current version
As we did with Unix, we are going to start slow and basic, ramping up as the weeks go on. First we are going to make sure everyone has the most recent version of Python installed. While doing this, we are going to take a slight detour to learn how incredibly easy it can be to download and install packages for Unix commands or programs that are not installed in the base system. For this, we will demonstrate the use of `brew`, which is command line utility for locating, downloading, and installing Unix packages on Mac computers. See past primers for guides on using `apt-get` (Linux) and `yum` (CentOS).

First check to see if you have python3 installed.  Open the shell and type

    $ python --version

If you get anyting that looks like version 2 not 3 or if you get an error that you dont have python, you will need to install version 3.


## Installing or updating Python on Mac Unix using homebrew

If you have already installed Homebrew - you dont need to do this. Check if you have it:

    $ which brew
  
If you dont have it, then:

    $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Then install python3 

    $ brew install python3


### Python downloads, also potentially useful
Go to python.org and download the latest release

    https://www.python.org/downloads/mac-osx


## Ubuntu
It is probably already installed but if not try with the package manager `apt-get`

    $ sudo apt-get install python3 idle
	
# 2. Writing your first python program

As with shell scripts, the first line of python scripts should be the shebang followed by the location of python:

    #!/usr/local/bin/python3

or, depending on your system:

    #!/usr/bin/python3


If you are unsure where you installed python3, you can easily figure out where it is:

    $ which python3


As covered in Haddock and Dunn, pg 127, you can also use the below text as your first line. This allows you to send script to `env` first, which should then locate python3, wherever it resides.

    #!/usr/bin/env python3

Either of the above will do, and are important **IF** or when you wish to convert your scripts to executable. If you want to do this, change the file mode: 

    $ chmod u+x first_python.py

And run as follows:

    $ ./first_python.py

## Accessing, testing, and writing python

There are multiple options for writing or testing python code, you will learn each of these during this semester, and will learn which suit your needs best as time goes on.

1. The python interpretter can be accessed in "interactive mode" from the terminal, by typing `python3`. This allows an efficient means of testing simple statements or doing simple things on the fly. This is **NOT** a good mechanism for writing much working code, and will not be used to write programs or code that you would generally want to document.

2. You similarly access python in "interactive mode" using the Jupyter QtConsole, available in the anaconda navigator suite described at the bottom of this primer. This can be used much as the terminal can (it recognizes linux commands as well), but has enhanced abilities that will help you write and understand your code. Try it a bit this week, and you will understand how it may aid you. I would recommend this over the base interactive mode that you can activate from the linux terminal.

3. Jupyter notebooks offer the ability to switch between blocks of markdown enhanced text (such as you are reading in these primers) and active python code blocks. Jupyter notebooks are excellent for teaching, and for learning, as you can keep detailed descriptions of what, how and why you are doing things, along with alternating code blocks that can be executed on the fly from within the notebooks. You will all learn to use jupyter notebooks, and as time goes on, will understand when or if they will be most useful for some of your needs.

4. Python is written in stored as text in scripts with the `.py` extension as a custom. Scripts allow you to keep your code organized in one place, in executable format if desired, and allow you to organize code for different work as you deem useful. I will generally ask you to turn in your work for each week either in jupyter notebooks or in scripts (e.g., Parchman_hashpractice.py).

## Your first simple program, using a `print` statement.

Sending information from your python scripts to stdout is accomplished with the `print` function. Our first script will simply illustrate how to print specified text, and will serve to convince you that this might not be as hard as you thought it was. Use `touch` to make a blank text file, but give it a `.py` extension as is customary for python scripts. This script needs only two simple parts. First, your customary first line that should go in all of your scripts, which should be:

    #!/usr/bin/env python3
Or the path to the specific location where python lives:

    #!/usr/local/bin/python3

To illustrate the use of `comment` text, marked with `#`, lets add a comment that is for you to read, not python. 

    #this is a comment: testing my first program with a simple print statement

Note the line above will not be part of the interpretted code. Instead, you can make use of `#` to leave annotations for yourself or others in your code to explain what you are doing.

Now lets add a print statement:

    print ("It is time to learn Python")

You can now run your program in two ways. Simply (which we strongly recommend for this class):

    $ python3 first_script.py 

Or, change to executable, then run:

    $ chmod u+x first_script.py
    $ ./first_script.py

If all is in order, "t is time to learn Python" should print to the screen, and you are ready for more.


<p>&nbsp;</p>
<p>&nbsp;</p>


# 3. Variable types in python

Four types of ariables are used to store information in python:

- Scalars: These can be of type integer, Float, String, or Boolean. Scalar variables store one 'thing'
- Lists: are one dimensional arrays of scalars
- Tuples: immutable lists
- Dictionaries: associative arrays, or unordered sets of key:value pairs

Variables can be named almost anyway you like. However, they can not start with a digit (e.g., 1dog) or with `$` or `#` (e.g., $stop, #pound), and they can not be among the 33 python3 keywords (see https://docs.python.org/3/library/keyword.html). Keywords are reserved for specific functionality in python, examples include `False`, `if`, `else`, `elif`, `import`, `for`, and `True`.

## Scalars

Scalars are the first type of variable we will work with in python. They include:

- **Integers**: whole numbers 
    - 1
    - 5
    - 999999
- **Floats**: : any number, with decimal, also referred to as“floating point”. 
    - 11.23 
    - 0.0222 
    - 3 x 10-10 
    - 3e12

- **Strings**: sequence of text characters
    - “ACGGGTTAACCCTTT”
    - “Western Conference Finals”
    - “3.14159 approximates Pi”

- **Boolean**: True or False

Assigning variables in python is easy. You can name variables that store information any way you like. You may want to use a format that will allow you to recognize different types of variables, but the rules are flexible. Below, I am assigning a float to the variable Pi, an integer to the variable Place, and a string to the variable Team. 

```python
Pi = 3.14159
Iteration = 5
Team = "Bengals"
DNAseq = "AAATCGTTGTCTGTGTG"
```

The `print` function, use first above, can be used anytime you would like to print a variable to screen (e.g., the terminal window)

We will do more of this next week, but we can do math operations on integers and floats and the variables which they are assigned to. Note the code below will print 21.

```python
x = 7
y = 3
z = x * y
print(z)
```

We can use the `.type` function to check the type of variable>

```python
type(x) ## will return int
type(DNAseq) ## will return string
```

## Lists

Lists store multiple scalars, of the same, or of different types. Lists are heavily used in python, as they are in other programming languages, and offer a variable type that can be iterated through with loops. 

One dimensional lists can be hard coded as below. Note that print here is used to print the entire list.

```python
ColorList = ('blue', 'red', 'green', 'violet', 'orange')
NumList = ('9', '83', '85', '11','52')
print(NumList)
```
Individual list elements by the name of the list and the list index enclosed in brackets. The index of the first element is `0`.

```python
ColorList = ('blue', 'red', 'green', 'violet', 'orange')
print(ColorList[1]) # will return red
```

# 4. Additional resources to help with learning Python

## Jupyter

**Jupyter notebooks** offer a convenient format/interface for providing text in markdown that can alternate with active code boxes for running python. This is a great way to keep yourself organized as you learn python, although it does have some drawbacks (which we will get to later in the semester). Past experience tells me that jupyter notebooks work great for students as they are learning python, so I will strongly suggest that everyone gets comfortable with jupyter this week so it can be used if preferred. In the **jupyter_start** directory (under week5) you can find a tutorial for installing and using jupyter notebooks.

## Jupyter QtConsole (enhanced interactive prompt), and Spyder IDE

Python has command line interactive prompt (we will get into this next week), but I suggest using one of these additional tools to aid your exploration of Python syntax while writing scripts or testing code.

Download the [Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/) suite of tools. From within this you can start the Spyder IDE and or the Jupyter QtConsole from the launch menu.


# Python documentation and other useful resources. 

I strongly recommend you explore several of the below resources and tutorials. They will all facilitate your progress greatly.

[Python documentation](https://www.python.org/doc/)

[Python for Biologists](https://pythonforbiologists.com/tutorial.html)
- Excellent tutorials and primers for introductory python. Follows similar topics to what cover in this class, with lots of variation on themes.

[Learn Python Interactive](https://www.learnpython.org/)
 - This has a built in interpretter, so you can test code or play with code under the tutorial examples. Excellent resource.

[Python guru ](https://thepythonguru.com/)
 - This also has a built in interpretter, so you can test code or play with code under the tutorial examples. Excellent resource.


## Note on Python 3 syntax updates and Haddock and Dunn.

 If you are using Haddock and Dunn text, be aware that it is based on python2, and there are some important differences between python2 and python3 (syntax changes that will require slight modification of book examples)


1. print statements in python3 should use (). 
2. `raw_input()` has become just `input()`

