# Unix primer 2

## Topics to cover

- `man` pages
- bash_profile
- text viewing and in terminal text editors
- compression, decompression
- more Unix commands, redirection
- process monitoring
- package installation
- introduction to `grep`

- **Haddock and Dunn: last 5 pages of chapter 4; chapter 5.**
- **U10 through U27 in Bradnam and Korf primer (http://korflab.ucdavis.edu/Unix_and_Perl/current.html)**
<p>&nbsp;</p>

## 1. `man` pages and command line options
For any Unix command (there are many thousands) you can find the full information on that command by using  `man` (manual pages, essentially). We will get introduced to 15-25 commonly used unix commands today, looking at `man` pages is one way to learn about the flexibility and various command line options.

For example:

    $ man pwd
will tell you what `pwd` does.

Try:

    $ man grep

Here you will see the information on grep displayed in a text viewer called `less`. You will use `less` frequently, so here are some keys to making it efficient:

* `spacebar` will scroll forward a page 
* `b` will scroll up a page
* `q` to exit less and regain the terminal prompt 
* `/` to search file for pattern. 
* when in pattern search mode, `n` skips to next match, `N` skips to previous match


Upon scrolling through the `grep` man page, you will see that `grep` has many command options and is a flexible, powerful, and commonly used text processing tool.


Most commands also have command line options, which are typed following a `-` after the command. Try `ls` below with the additional options h or l, which could be specified in either format shown below

    $ ls -l -h
    $ ls -lh

Notice that when you use `man`, all of the command line options will be clearly listed and efficiently described. Try the below for command line option explanations for `ls`. As a reminder, type `q` to exit the `less` viewer and to regain your terminal prompt.

    $ man ls

Online manual pages (e.g., [less man page](https://man7.org/linux/man-pages/man1/less.1.html)) and other sites are also plentiful to read up on Unix commands or if you are looking for guidance.


## 2. Terminal profile settings

You can can customize the way a command works from shell by creating an **alias**. For example, the below command will change things so that when you type `ls`, your terminal will call `ls -lh`

    $ alias ls = 'ls -lh'

When you do type a command such as above during a terminal session, it will only work from within that session. Once you get more comfortable in Unix, you will likely want to customize the behavior of your shell uniformly. This can easily be done by modifying a file, `.zshrc` (or depending on flavor of Unix/Linux you are running: `.bashrc`, `.profile` or `.bash_profile`), that resides in your home directory. The `.` before the file names here renders them 'hidden'. Thus, to move to your home directory and look for these types of files use (note the -a option is shorthand for all, so it shows the hidden files as well):

    $ cd ~
    $ ls -a

- If you are running a newer Mac OS, you are probably running the zsh terminal application. If so, `.zshrc` is the name of the profile file. If you have one, consider adding alias's such as below. If you dont have one, use `touch` to make one, or better yet, just download the example `.zshrc` on the course github page under `unix_resources` or `week2_UnixII`, move to your home directory and name appropriately (e.g., **zshrc_eg** would need to be renamed **.zshrc**).

- If you are running an older Mac OS, or just prefer bash as a terminal application, the profile information is stored in `.bash_profile` or `.bashrc`. You can create such a file and insert alias commands as below or merely change the name of the `.zshrc` file above to `.bash_profile` or `.bashrc`).

- If you are running Ubuntu Linux, check which terminal application you are using and consult google.

I'd suggest the following alias list, or atleast this is similar to what I use:

    # helpful alias collection
    alias python='python3'
    alias ll="ls -laF"
    alias ls="ls -F"
    alias rm="rm -i"
    alias mv="mv -i"
    alias cp="cp -i"

The alias collection above has some useful features. `ll` and `ls`, when typed, will give you more complete, and/or more readable information. `rm`, `mv`, and `cp` have the `-i` option added, which is  HIGHLY recommended. This will change the behavior of `rm`, `mv`, or `cp` to always ask if you are sure you want to remove a file, or overwrite a file with the same name in terms of `cp` and `mv`.

IF you like this alias collection or want something similar, you can set in your **.zshrc** (or similar) profile as follows. These live in a hidden file in your home directory (.bash_profile, the "." in front of a file hides the file from showing up with normal use of `ls`). If you have such a profile file, set alias as above within that file. 

Go to your home directory:

    $ cd ~

View hidden files:

    $ ls .*

Note the above option will show just files that begin with `.`. If you wanted to see all files, regardless of whether they start with `.` or not, you could use:

    $ ls -a

If you do not have **.zshrc**, **.bashrc**, **.bash_profile** or **.profile** files, make one and open as below. Note, that depending on your system the name of the file will need to be one of the above.

    $ touch .zshrc
    $ open .zshrc

Copy and paste the alias settings ("helpful alias settings") above into .zshrc, and save. Then, 

    $ source .zshrc

Once you quit and restart your terminal app, your new alias settings should be working, but test this out to be sure. Make a test.txt file, and use `rm` to remove it. If things are correct, you should be prompted by the terminal with "remove test.txt?". Type Y to remove, N to leave alone. Note, these settings will protect you from terrible very bad accidents, and you will be able to easily override them when you are comfortable (to be covered later).

Haddock and Dunn (page 87) present an additional/aternative safety approach to prevent overwriting or accidentally deleting, by adding the below to .bash_profile:

    set -o noclobber

### `oh my zsh`: an open source, community-driven framework for managing your zsh configuration.

The `zsh` terminal featured on apple and some linux operating systems is an upgrade to bash due to its high level of customization. If you would like to explore such customization, I suggest trying `oh my zsh`.

You can find all necessary support and learn more about it [here](https://github.com/ohmyzsh/ohmyzsh).

Installing is super easy, just copy the below into your terminal.

    $ sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"


## 3. Text viewing *OR* text editing within the terminal

### Text viewers for quickly looking at small sections of files

We will make common use of text viewers such as `less`, `head`, `tail` or `more`; especially `less`. Why would we just want to "look" and not "open" large text files? Large amounts of data stored in text are often beyond the memory capacity of GUI programs, and most of what we will work with will be far too large to "look" at usefully anyway. `less` will allow you to have a peak at a file to understand its structure, which is ultimately what you will need to write code to manipulate and extract information. 

As `man` pages are by default viewed with `less`, look at the `man` page for `less` for guidance on how to control this text viewer.

    $ man less

You will use `less` regularly, a few tips, as above:
- `q` quits and renews the active terminal prompt
- `spacebar` moves one page forward
- `b` moves one page back
- `/` allows search, `/123` will go to instances of "123".
- after first match is found, `n` will go to the next match.


Use `less` to have a look at the top of **sample_passerina.fastq** file I have added under week2 on the course page (note, this will initially have to be decompressed as detailed below). You will see that DNA sequence data from an Illumina machine is stored in a structured and simple format with 4 lines of data per sequence (ID line, DNA sequence, Quality ID, quality score).

### In terminal text editors

To access and edit text *within* the terminal, there are many editors (`vim`, `emacs`, etc.) you can use. For this course, I suggest `nano`, which will be available on your system. Why would you want to use a keyboard controlled only in-terminal text editor instead of something like VScode or BBedit? Once you start working on remote servers, the time and place for such usage will become more clear. For now, just know it exists as an option, but do not make your life harder by trying to write your first bash or python programs in `nano`.

To open a file for editing within the terminal with `nano`:

```
$ nano myfile.txt
```

## 4. Compression and decompression using `gzip` and `gunzip`

Compression and de-compression are regular activities associated with large text data files, so get comfortable with it. `gzip` is a command for compressing and decompressing files. 

Compressed .gz files can be easily decompressed.

    $ gunzip sample_passerina.fastq.gz

And compression is similarly easy. The below command will create the compressed file "sample_passerina.fastq".

    $ gzip sample_passerina.fastq

All .txt files in a directory can be compressed (or decompressed) using a wildcard, `*` with this command. Note the below command would compress, one by one, all files ending in .txt. `*` will make your life easier.

    $ gzip *.txt 

`tar` is a unix command with more flexibility that is commonly used for compressing directories (`gzip` and `gunzip` work with files NOT directories). We will learn more about `tar` later.

`*` will make your life easier, and you will learn to use it in many contexts. `*` is short for wildcard, meaning it matches everything. So, `ls *.txt` would list all files that start with anything and end with `*txt` in the directory this command was executed from. Here is another simple example for now, which would copy all of the files starting with BS_1287 and ending in fastq.gz to a specified directory

    $ cp BS_1287*fastq.gz data_for_BS1287/

## 5. stdout, redirection (`>`)

**stdout** (standard out) is the text that is printed to screen when Unix commands are executed. The `cat` command is used to concatenate files and print file contents to standard output. Using it as below will print the entire contents of passerina.fastq to screen. Try it.

    $ cat passerina.fastq

That doesn't seem very useful in most cases. Instead, we can redirect the standard output of any Unix command to a file simply by using redirection with `>`. Here are some simple examples.

The below command would concatenate the data from all files in a directory ending in data.txt into one file. Note that `*` is a wildcard character that means "anything", so its use below with ***data.txt** will match all files in the directory that have any text followed by **data.txt**.

    $ cat *data.txt > all_data_in_directory.txt

The use of `>>` below will write the contents of **newdata.txt** to the end of **all_data_in_directory.txt**.

    $ cat newdata.txt >> all_data_in_directory.txt

Redirection of `ls -lh` below simply sends all that information on files in the directory to a text file.

    $ ls -lh > directory_contents.txt

`grep` is a powerful regular expression matching command, and later in the course we will learn extensively about using it to match and extract data matching characteristics that we can specify. The use of `grep` below will send all lines containing a match to "BS_1287" to a new file.

    $ grep "BS_1287" data_all_inds.txt > data_for_ind_BS1287.txt

## 6. Basic process monitoring 

On linux systems, it is often important or necessary to have a look at what the system is doing - to get an idea of how many jobs or processes are running and who is running them. It is also a useful way to recognize jobs you have started from the terminal that need to be stopped or **killed**.

*This is a simple start, we will revisit next week*

`top` will display information on processes running on the machine you are logged into. Try it, read the output. Doesn't matter what directory you call it from. As with `less`, type `q` to exit the system view.

    $ top

`top` doesnt have the prettiest or most obviously searchable output. `htop` is an upgrade that you may or may not have on your system. If you downloaded `oh my zsh`, you should have it. In the coming weeks, we will learn how to efficiently install whatever you want from the command line. In the meantime, if you dont have `htop`, you can downloand and install it using `brew`, following basic guide to package installation below.

`ps` will show your active process ids. Below I am using `ps aux`, piping (with `|` ) the output into `grep` and using my username as the match for `grep`. Try it with your username.

    $ ps aux | grep thomasparchman

If you have mutliple processes running, and want to kill one, use `kill` followed by the process ID, which you can locate with `top`, `htop` or `ps`

    $ kill 9031


## 7. Package installation

This is a bit extra for what we are doing this week, but I thought I would add it here as a guide for those interested. For installing on your personal mac computers, `brew` will be your most convenient option. I would stress here that this type of package installer/manager makes accomplishing these tasks in the Unix OS incredibly easy.

**B. Unix on Mac Unix systems**

`homebrew` manages and installs packages on Mac OS Unix. 
To install brew (homebrew):

    $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

`brew` is pretty easy to use. To look at a list of commands and their uses:

    $ brew help

To search for an installable program:

    $ brew search

To install a package:

    $ brew install packagename

As a simple example, lets install a more useful version of `top`, `htop`, that has some expanded information and visuals. Using brew is quite easy, as you can see.

    $ brew install htop

A more detailed, yet basic, tutorial can be found below. As with the above, carefully review before using.

- https://wpbeaches.com/installing-homebrew-on-macos-big-sur-11-2-package-manager-for-linux-apps/

**B. Linux distributions:**

`apt` is a package management system for most Linux distributions. It facilitates the installation, management, updates, and removal of software. Using apt-get requires superuser privileges (`sudo`), and will require password entry.


You can find useful tutorials on `apt` and `apt-get` below. We suggest reviewing information, and familiarizing yourself with `sudo` carefully before using.

- https://phoenixnap.com/kb/how-to-use-apt-get-commands
- https://itsfoss.com/apt-get-linux-guide/
- https://www.control-escape.com/linux/lx-swinstall.html


To install software using `apt-get`:

    $ sudo apt-get install <package_name>

To remove software using `apt-get`:

    $ sudo apt-get remove <package_name> 

Note, the above doesnt remove configuration files associated with a package. To remove the package along and configuration files:

    $ sudo apt-get purge <package_name> 

## 8. Regular expressions and text extraction with `grep`

`grep` is a powerful regular expression engine, among the most commonly used commands for data science. You can explore the examples below using sample_passerina.fastq, available under week1 on the [course github page](https://github.com/tparchman/BIOL792). This is an increbily versatile command, so we better learn more. In it simplest invocation, `grep` will output every line in a file that matches the specified pattern.

Since fastq files have a standard four line format (ID starting with @, DNA sequence, quality id starting with +, and quality score), we know that every sequence has a line starting with @ associated with it. 

We could write all of teh ID lines to a separate file:

    $ grep "^@" -c sample_passerina.fastq > idlines.txt

We can cound the number of sequences:

    $ grep "^@" -c sample_passerina.fastq

We can print the line with a match, plus any number of lines following it:

    $ grep "^@" -A 1 sample_passerina.fastq

SDN_AM_43432 is the ID of a specific bird represented in this data set. How many DNA sequences do we have for this bird?

    $ grep "SDN_AM_43432" -c sample_passerina.fastq


