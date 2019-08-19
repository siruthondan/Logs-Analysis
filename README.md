# Logs-Analysis
Project as part of Full Stack Developer nano degree by Udacity

DESCRIPTION

For this project, my task was to create a reporting tool that prints out reports( in plain text) based on the data in the given database. This reporting tool is a Python program using the psycopg2 module to connect to the database. This project sets up a mock PostgreSQL database for a fictional news website. The provided Python script uses the psycopg2 library to query the database and produce a report that answers the following three questions:

What are the most popular three articles of all time?
Who are the most popular article authors of all time?
On which days did more than 1% of requests lead to errors?

RUNNING THE PROGRAM

To get started, I recommend the user use a virtual machine to ensure they are using the same environment that this project was developed on, running on your computer. You can download Vagrant and VirtualBox to install and manage your virtual machine. Use vagrant up to bring the virtual machine online and vagrant ssh to login.

Download the data provided by Udacity. Unzip the file in order to extract newsdata.sql. This file should be inside the Vagrant folder.

Load the database using psql -d news -f newsdata.sql.

Connect to the database using psql -d news.

Now execute the Python file - python ReportingTool.py.

PS: Views are not created as part of this project as the Database is considered to be Dynamic and not Static.
