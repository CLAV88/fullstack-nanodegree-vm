# Getting Started

Author: Calvin Bissett & with excerpts from Udacity.com FD Nanodegree program. credit: <https://github.com/udacity/fullstack-nanodegree-vm>

## Pre-Requisites

1. vagrant
2. virtualbox

## Starting the vm

1. start her up after following the instructions below and by command:
2. vagrant up
3. cd /vagrant
4. cd newsPy
5. run python newsdb.py

## Installation

### Install VirtualBox

VirtualBox is the software that actually runs the virtual machine. [You can download it from virtualbox.org, here.](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) Install the _platform package_ for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.

Currently (October 2017), the supported version of VirtualBox to install is version 5.1. Newer versions do not work with the current release of Vagrant.

**Ubuntu users:** If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center instead. Due to a reported bug, installing VirtualBox from the site may uninstall other software you need.

### Install Vagrant

Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. [Download it from vagrantup.com.](https://www.vagrantup.com/downloads.html) Install the version for your operating system.

**Windows users:** The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

![vagrant --version](https://d17h27t6h515a5.cloudfront.net/topher/2016/December/584881ee_screen-shot-2016-12-07-at-13.40.43/screen-shot-2016-12-07-at-13.40.43.png)

_If Vagrant is successfully installed, you will be able to run_ `vagrant --version`
_in your terminal to see the version number._
_The shell prompt in your terminal may differ. Here, the_ `$` _sign is the shell prompt._

### Download the VM configuration

Use Github to fork and clone, or download, the repository [https://github.com/udacity/fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm).

You will end up with a new directory containing the VM files. Change to this directory in your terminal with `cd`. Inside, you will find another directory called **vagrant**. Change directory to the **vagrant** directory:

![vagrant-directory](https://d17h27t6h515a5.cloudfront.net/topher/2016/December/58487f12_screen-shot-2016-12-07-at-13.28.31/screen-shot-2016-12-07-at-13.28.31.png)

_Navigating to the FSND-Virtual-Machine directory and listing the files in it._
_This picture was taken on a Mac, but the commands will look the same on Git Bash on Windows._

## Instructions

### Start the virtual machine

From your terminal, inside the **vagrant** subdirectory, run the command `vagrant up`. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.

![vagrant-up-start](https://d17h27t6h515a5.cloudfront.net/topher/2016/December/58488603_screen-shot-2016-12-07-at-13.57.50/screen-shot-2016-12-07-at-13.57.50.png)

_Starting the Ubuntu Linux installation with `vagrant up`._
_This screenshot shows just the beginning of many, many pages of output in a lot of colors._

When `vagrant up` is finished running, you will get your shell prompt back. At this point, you can run `vagrant ssh` to log in to your newly installed Linux VM!

![linux-vm-login](https://d17h27t6h515a5.cloudfront.net/topher/2016/December/58488962_screen-shot-2016-12-07-at-14.12.29/screen-shot-2016-12-07-at-14.12.29.png)

_Logging into the Linux VM with `vagrant ssh`._

### Logged in

If you are now looking at a shell prompt that starts with the word `vagrant` (as in the above screenshot), congratulations — you've gotten logged into your Linux VM.

If not, take a look at the [Troubleshooting](#troubleshooting) section below.

### The files for this course

Inside the VM, change directory to `/vagrant` and look around with `ls`.

The files you see here are the same as the ones in the `vagrant` subdirectory on your computer (where you started Vagrant from). Any file you create in one will be automatically shared to the other. This means that you can edit code in your favorite text editor, and run it inside the VM.

Files in the VM's `/vagrant` directory are shared with the `vagrant` folder on your computer. But other data inside the VM is not. For instance, the PostgreSQL database itself lives only inside the VM.

### Running the database

The PostgreSQL database server will automatically be started inside the VM. You can use the `psql` command-line tool to access it and run SQL statements:

![linux-vm-PostgreSQL](https://d17h27t6h515a5.cloudfront.net/topher/2016/December/58489186_screen-shot-2016-12-07-at-14.46.25/screen-shot-2016-12-07-at-14.46.25.png)

_Running `psql`, the PostgreSQL command interface, inside the VM._

### Logging out and in

If you type `exit` (or `Ctrl-D`) at the shell prompt inside the VM, you will be logged out, and put back into your host computer's shell. To log back in, make sure you're in the same directory and type `vagrant ssh` again.

If you reboot your computer, you will need to run `vagrant up` to restart the VM.

## Troubleshooting

### I'm not sure if it worked

If you can type `vagrant ssh` and log into your VM, then it worked! It's normal for the `vagrant up` process to display a lot of text in many colors, including sometimes scary-looking messages in red, green, and purple. If you get your shell prompt back at the end, and you can log in, it should be OK.

### `vagrant up` is taking a long time

Because it's downloading a whole Linux operating system from the Internet.

### I'm on Windows, and when I run `vagrant ssh`, I don't get a shell prompt

Some versions of Windows and Vagrant have a problem communicating the right settings for the terminal. There is a workaround: Instead of `vagrant ssh`, run the command `winpty vagrant ssh` instead.

### I'm on Windows and getting an error about virtualization

Sometimes other virtualization programs such as Docker or Hyper-V can interfere with VirtualBox. Try shutting these other programs down first.

In addition, some Windows PCs have settings in the BIOS or UEFI (firmware) or in the operating system that disable the use of virtualization. To change this, you may need to reboot your computer and access the firmware settings. [A web search](https://www.google.com/search?q=enable%20virtualization%20windows%2010) can help you find the settings for your computer and operating system. Unfortunately there are so many different versions of Windows and PCs that we can't offer a simple guide to doing this.

### Why are we using a VM, it seems complicated

It is complicated. In this case, the point of it is to be able to offer the same software (Linux and PostgreSQL) regardless of what kind of computer you're running on.

### I got some other error message

If you're getting a specific textual error message, try looking it up on your favorite search engine. If that doesn't help, take a screenshot and post it to the discussion forums, along with as much detail as you can provide about the process you went through to get there.

### If all else fails, try an older version

Udacity mentors have noticed that some newer versions of Vagrant don't work on all operating systems. Version 1.9.2 is reported to be stabler on some systems, and version 1.9.1 is the supported version on Ubuntu 17.04. You can download older versions of Vagrant from [the Vagrant releases index](https://releases.hashicorp.com/vagrant/).

## Supporting Materials

[Virtual machine repository on GitHub](https://github.com/udacity/fullstack-nanodegree-vm)

[(Back to TOC)](#table-of-contents)

## Download the data

1. Next, download the data here. You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.

2. To build the reporting tool, you'll need to load the site's data into your local database. Review how to use the psql command in this lesson: (FSND version)

3. To load the data, cd into the vagrant directory and use the command psql -d news -f newsdata.sql.

* Here's what this command does:

* psql — the PostgreSQL command line program
* -d news — connect to the database named news which has been set up for you
* -f newsdata.sql — run the SQL statements in the file newsdata.sql
*.. Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

## Getting an error

If this command gives an error message, such as —

psql: FATAL: database "news" does not exist
psql: could not connect to server: Connection refused

* — this means the database server is not running or is not set up correctly. This can happen if you have an older version of the VM configuration from before this project was added. To continue, download the virtual machine configuration into a fresh new directory and start it from there.

## The db schema \dt

          List of relations
 Schema |   Name   | Type  |  Owner
--------+----------+-------+---------
 public | articles | table | vagrant
 public | authors  | table | vagrant
 public | log      | table | vagrant
(3 rows)

## Notes on the Articles Table of the news db

news=> \d articles;
                                  Table "public.articles"
 Column |           Type           |                       Modifiers
--------+--------------------------+-------------------------------------------------------
 author | integer                  | not null
 title  | text                     | not null
 slug   | text                     | not null
 lead   | text                     |
 body   | text                     |
 time   | timestamp with time zone | default now()
 id     | integer                  | not null default nextval('articles_id_seq'::regclass)

### Notes on the Authors Table of the news db

                          Table "public.authors"
 Column |  Type   |                      Modifiers
--------+---------+------------------------------------------------------
 name   | text    | not null
 bio    | text    |
 id     | integer | not null default nextval('authors_id_seq'::regclass)
Indexes:
    "authors_pkey" PRIMARY KEY, btree (id)
Referenced by:
    TABLE "articles" CONSTRAINT "articles_author_fkey" FOREIGN KEY (author) REFERENCES authors(id)

### Notes on the Logs Table of the news db

                                  Table "public.log"
 Column |           Type           |                    Modifiers
--------+--------------------------+--------------------------------------------------
 path   | text                     |
 ip     | inet                     |
 method | text                     |
 status | text                     |
 time   | timestamp with time zone | default now()
 id     | integer                  | not null default nextval('log_id_seq'::regclass)
Indexes:
    "log_pkey" PRIMARY KEY, btree (id)

## Status Line Codes

1. 1xx — Informational. The request is in progress or there's another step to take.
2. 2xx — Success! The request succeeded. The server is sending the data the client asked for.
3. 3xx — Redirection. The server is telling the client a different URI it should redirect to. The headers will usually contain a Location header with the updated URI. Different codes tell the client whether a redirect is permanent or temporary.
4. 4xx — Client error. The server didn't understand the client's request, or can't or won't fill it. Different codes tell the client whether it was a bad URI, a permissions problem, or another sort of error.
5. 5xx — Server error. Something went wrong on the server side.

## Intstructions for using the python functions

run py, then run py program when @ newsPy sudirectory with command py newsdb.py, the program will print the three database responses with a live query.

### Functions in newsdb.py file

1. Top three articles of all time.
2. Top Three authors for articles in db.
3. Days where site experienced >1% errors in server requests.

## Views

### Either

run psql -d news -f create_views.sql

### or

*..Used to select the numerrors per day (logs Table) => http_errors_per_day view

* create view http_errors_per_day select time::date as datelog, count(*) as numerrors from log where left(log.status,3)::integer > 400 group by datelog order by numerrors desc;

*.. Used to select the numhttprequests per day (logs Table) => http_requests_per_day view

* create view http_requests_per_day select time::date as datelog, count(*) as numhttprequests from log group by datelog order by numhttprequests desc;
