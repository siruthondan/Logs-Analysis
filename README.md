# Logs-Analysis
Project as part of Full Stack Developer nano degree by Udacity

### DESCRIPTION:

The logs Analysis project is part of the Full Stack Developer nano degree course by Udacity. The project aims to showcase the DB-API, SQL and Python skills and the database used in PostgreSQL.

It is required to build an internal reporting tool that use information from the database to discover what kind of articles the sites readers like.

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using this information, the code answers questions about the sites user activity. The Python script uses the psycopg2 library to query the database to produce the report.

The tool reports the below considering the database is Dynamic, 
- What are the most popular three articles of all time?
- Who are the most popular article authors of all time?
- On which days did more than 1% of requests lead to errors?

###RUNNING THE PROGRAM:

This project makes use of the same Linux-based virtual machine (VM) which comes preinstalled with Python and PostgreSQL Database.

	1. Download [Vagrant](https://www.vagrantup.com/downloads.html) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads) to install and manage your virtual machine. Use `vagrant up` to bring the virtual machine online and `vagrant ssh` to login.
	2. Download the data provided by Udacity [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Unzip the file in order to extract newsdata.sql. This file should be inside the Vagrant folder.
	3. Load the database using` psql -d news -f newsdata.sql`.
	4. Connect to the database using `psql -d news` and verify the created tables and column types.
	5. Now execute the Python file -` python ReportingTool_v1.py`.
