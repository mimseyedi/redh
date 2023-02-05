# Redhand
[![pypi](https://img.shields.io/pypi/v/redh.svg)](https://pypi.org/project/redh/) [![license](https://img.shields.io/github/license/mimseyedi/redh.svg)](https://github.com/mimseyedi/redh/blob/master/LICENSE)

![img1](https://raw.githubusercontent.com/mimseyedi/redh/master/docs/redhand-poster.png)

Redhand (redh) is a command line tool for managing files and directories. This is my first project to build a command line tool, which is supposed to be more advanced in the next versions. I would greatly appreciate your participation on this project.

## Table of Contents: <a class="anchor" id="contents"></a>
* [How to install](#install)
* [Quick look](#qlook)
* [Commands](#cmds)

  * [scan - Find files and directories in the system](#scan)
  * [grab - Getting files and directories from a specific location](#grab)
  * [open - Show captured content](#open)
  * [drop - Drop the collected contents in a specified place](#drop)
  * [throw - Remove the contents collected by their index](#throw)
  * [wash - Delete all collected content.](#wash)
  * [org - Sort and organize files and folders as desired](#org)
  

* [Contribute](#cont)
* [Resources](#res)


## How to install <a class="anchor" id="install"></a>
You can download and install this tool directly from `pypi` repository by `pip` module. (Make sure you are using Python3)

```
python3 -m pip install redh  
```

## Quick look <a class="anchor" id="qlook"></a>
Red Hand is a simple but useful tool for moving files and directories, which is very easy to work with. This tool also uses regex to filter contents.

You can ask anything you need to know from the --help option. Just write --help after each command to provide you with information about each command. You can also do this to get a general guide:
```
redh --help  
```

output:

```
Usage: redh [OPTIONS] COMMAND [ARGS]...

  Redhand is a command line tool for managing files and directories.

  To access the help of each command, use the --help option after
  writing the command.

  Github repo: https://github.com/mimseyedi/redh

Options:
  --version  Version of Redhand.
  --help     Show this message and exit.

Commands:
  drop   The Redhand leaves the files and directories it took in...
  grab   The Redhand takes the files and directories you specified.
  open   The contents of the hand will be displayed.
  org    Arranges and organizes the selected contents.
  scan   Search and check the desired files and directories.
  throw  It discards the contents of the hand by their index.
  wash   All contents in the hand are completely erased.  
```

Also, to find out about the Redhand version, you can do as follows:

```
redh --version  
```

output:

```
1.0.0  
```


## Commands <a class="anchor" id="cmds"></a>
The Redhand has very simple commands that you can easily learn how to use with the help of this guide.

## scan <a class="anchor" id="scan"></a>
With the help of this command, you can find the files or directories you are looking for with the help of regex. Also, this command gives you a safe space to create regex patterns.

The scan command accepts only one argument from you, which must be between two single quotes and follow a regex expression.

```
redh scan 'txt$' 
```

output:

```
1 - f - /home/user/Desktop/homeworks.txt
2 - f - /home/user/Desktop/about.txt
3 - f - /home/user/Desktop/note.txt
```

The output shows us 3 things:

* The `index` of each file or directory found.

* Type the content found. `f` means file and `d` means directory.

* The `full address` of the content found.


## grab <a class="anchor" id="grab"></a>
With the help of this command, you can ask the Redhand to take files and directories for you and carry them anywhere you want. Of course, you should consider that he only remembers the `addresses` and copies them when moving. Therefore, if you take a content by hand and then delete it on the spot, the Redhand will `not consider` it anymore.

You can directly point to what you want `one by one` or group them with the help of `regex`.

`Note:` To use regex here, you must use two single quotes between two double quotes.

```
redh grab about.txt "'^Big+.+mkv$'" homeworks.txt
```

output:

```
'/home/user/Desktop/about.txt' successfully grabbed by hand!
'/home/user/Desktop/Big_bang_theory_S1_E1.mkv' successfully grabbed by hand!
'/home/user/Desktop/Big_bang_theory_S1_E2.mkv' successfully grabbed by hand!
'/home/user/Desktop/Big_bang_theory_S1_E3.mkv' successfully grabbed by hand!
'/home/user/Desktop/homeworks.txt' successfully grabbed by hand!
```

## open <a class="anchor" id="open"></a>
With this command, all the contents of the hand that have already been taken will be displayed.

The output shows us 3 things:

* The `index` of each file or directory.

* Type the content. `f` means file and `d` means directory.

* The `full address` of the content.

Just enter the open command:
```
redh open
```

output:

```
1 - f - /home/user/Desktop/about.txt
2 - f - /home/user/Desktop/Big_bang_theory_S1_E1.mkv
3 - f - /home/user/Desktop/Big_bang_theory_S1_E2.mkv
4 - f - /home/user/Desktop/Big_bang_theory_S1_E3.mkv
5 - f - /home/user/Desktop/homeworks.txt
```

Also, the open command has an option called `-f`, which you can search among the contents with the help of regex:

```
redh open -f 'mkv$'
```

output

```
1 - f - /home/user/Desktop/Big_bang_theory_S1_E1.mkv
2 - f - /home/user/Desktop/Big_bang_theory_S1_E2.mkv
3 - f - /home/user/Desktop/Big_bang_theory_S1_E3.mkv
```

## drop <a class="anchor" id="drop"></a>
With this command, you can copy the contents of the Redhand to the place you choose.

Using the -a option, you can copy all the contents:

```
redh drop -a
```

output:

```
'/home/user/Desktop/about.txt' was copied successfully!
'/home/user/Desktop/Big_bang_theory_S1_E1.mkv' was copied successfully!
'/home/user/Desktop/Big_bang_theory_S1_E2.mkv' was copied successfully!
'/home/user/Desktop/Big_bang_theory_S1_E3.mkv' was copied successfully!
'/home/user/Desktop/homeworks.txt' was copied successfully!
```

Or you can directly copy them by referring to the content index:

```
redh drop 1 5
```


output:

```
'about.txt' was copied successfully!
'homeworks.txt' was copied successfully!
```

## throw <a class="anchor" id="throw"></a>
With this command, you can delete files or directories from the red hand by referring to the content index.

```
redh throw 2 3 4
```

output:

```
'/home/user/Desktop/Big_bang_theory_S1_E1.mkv' was successfully thrown away!
'/home/user/Desktop/Big_bang_theory_S1_E2.mkv' was successfully thrown away!
'/home/user/Desktop/Big_bang_theory_S1_E3.mkv' was successfully thrown away!
```

And then:

```
redh open
```

output:

```
1 - f - /home/user/Desktop/about.txt
2 - f - /home/user/Desktop/homeworks.txt
```

## wash <a class="anchor" id="wash"></a>
With this command, all contents inside the red hand will be deleted.
```
redh wash
```

output:

```
The Hand washed successfully!
```

And then:
```
redh open
```

output:

```
The Hand is empty!
```

## org <a class="anchor" id="org"></a>
With this command, you can transfer the desired contents that you specified with the help of regex to the directory you want:
```
redh org 'py$' Python
```

This command means to move all Python files to a directory called Python. If a directory with this name already exists, the files will be moved there, and if not, a directory with this name will be created.

## Contribute <a class="anchor" id="cont"></a>
I welcome your ideas to develop this tool. The options that I thought about for the next version include:

* An option for the grab command to make a `real copy` of a file or directory to preserve if it is deleted.

* Add an option for the drop command to use `cut` instead of copy.

* Adding `filtering` with the help of `regex` to the `drop` and `throw` commands.

* Add a `log system` to record and review all activities performed.

* And ...

## Resources <a class="anchor" id="res"></a>
* I used the `click` module to make this tool command.
* I also got help from the link below to convert this `script` into a `command line tool`:
https://towardsdatascience.com/how-to-build-and-publish-command-line-applications-with-python-96065049abc1

Thanks.
