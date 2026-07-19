# Basic Linux Commands

Basic Linux commands are beneficial to developers when interacting with a Linux operating system through the command line interface. They are used when working with files and directories. Typically, they are easy to learn and apply, and provide developers with additional commands for more advanced situations. If needed, these commands are also easy to look up on your preferred search engine.

In this reading, you will review basic Linux commands with examples provided along the way.

## Managing Files and Directories

Many applications configure themselves by reading files. They are designed to read and write files in specific directories. Because of this, developers need to understand how to move and rename files, change their permissions, and do simple operations on their contents. Here are some common commands:

**`mv`** is used to move one or more files to a different directory, rename a file, or both at the same time.

> **Note:** Linux is case-sensitive, so `mv` can also be used to change the case of a filename.

```bash
mv myfile.txt dir1/
```
This command moves a file to the directory.

```bash
mv file1.txt file2.txt file3.txt dir1/
```
This command moves multiple files.

**`cp`** is used to copy one or more files. Some examples include:

```bash
cp file1.txt file2.txt
```

```bash
cp file1.txt file2.txt file3.txt dir1/
```

**`chmod`/`chown`/`chgrp`** is used to make a file readable to everyone on the system before moving it to a public directory. A common example is:

```bash
chmod +r file.html && mv file.html /var/www/html/index.html
```

## Operating with the Content of Files

Every programmer will use files for something. Whether it's for configuration, data, or input and output, programmers work with files and need to know how to operate with their contents.

**`cut`** is a command that extracts fields from a data file. Two examples are:

```bash
cut -f1 -d"," addressbook.csv
```
This command extracts the first field from a .csv file.

```bash
cut -c1-3,5-7,9-12 phones.txt
```
This command extracts only the digits from a list of phone numbers.

**`sort`** is a command that sorts the contents of a file. Some examples include:

```bash
sort names.txt
```
This command sorts inputs alphabetically.

```bash
sort -r names.txt
```
This command sorts inputs in reverse alphabetical order, starting with the letter z.

```bash
sort -n numbers.txt
```
This command treats the inputs as numbers and then sorts them numerically.

Some examples that include combining multiple commands are:

```bash
ls -l | cut -w -f5,9 | sort -rn | head -10
```
This command displays the 10 largest files in the current directory.

```bash
cut -f1-2 -d"," addressbook.csv | sort
```
This command extracts the first and last names from a .csv file and sorts them.

## Managing Streams

These are the redirectors that we can use to take control of the streams of our programs:

* `command > file`: redirects standard output, overwrites file
* `command >> file`: redirects standard output, appends to file
* `command < file`: redirects standard input from file
* `command 2> file`: redirects standard error to file
* `command1 | command2`: connects the output of command1 to the input of command2

## Operating with Processes

These are some commands that are useful to know in Linux when interacting with processes. Not all of them are explained in videos, so feel free to investigate them on your own.

* `ps`: lists the processes executing in the current terminal for the current user
* `ps ax`: lists all processes currently executing for all users
* `ps e`: shows the environment for the processes listed
* `kill PID`: sends the SIGTERM signal to the process identified by PID
* `fg`: causes a job that was stopped or in the background to return to the foreground
* `bg`: causes a job that was stopped to go to the background
* `jobs`: lists the jobs currently running or stopped
* `top`: shows the processes currently using the most CPU time (press "q" to quit)

## Additional Commands

Additional commands that programmers commonly use are:

**`id`** is a command that prints information about the current user. This command is useful if you are getting a permissions denied error and think you should be granted access to a file.

```bash
$ id
uid=3000(tradel) gid=3000(tradel) groups=3000(tradel),0(root),100(users),545(builtin_users),999(docker)
```

**`free`** is a command that prints information about memory on the current system.

```bash
free -h
```
This command prints in human-readable units instead of bytes.

## Key Takeaways

Basic Linux commands assist developers in different types of tasks related to managing files and directories and working with the content of each file. These commands allow developers to work more efficiently and effectively.
