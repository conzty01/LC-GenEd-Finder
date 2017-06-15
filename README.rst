Luther College GenEd Course Database
====================================

Overview
--------

This is a web application that searches through the courses offered at Luther College and 
allows users to search through those courses based on the All College General Education 
requirements. Currently, users are allowed to search by a single GenEd or by multiple requirements.

A beta version of this web service is deployed on heroku here_. 

Requirements
------------

In order to run this application, you will need:

	1. Python 2.7 -- newer versions may work but have not been thoroughly tested.
		* psqcopg2
		* scrapy
		* flask

	2. PostgreSQL 9.5

Alternatively, you can just install the Python modules via the included requirements.txt:

::

	$ sudo pip install -r requirements.txt


Installation and Operation
--------------------------

Before running the server, run the resetGenEd.py script.  Alternatively, you can execute 
the following commands to set up the database.

::

	$ scrapy crawl courseSpider -o lcCourses.json
	$ python createDB.py
	$ python populateDB.py

Setting up the database in this manner can cause issues with the output of the spider 
where some instances of unicode are not properly escaped. A simple .read() and 
.replace(<unicode>,<alternateString>) fixes this issue and is taken care of in the 
resetGenEd.py script.

After the database is set up properly, execute the command

::

	$ python genEdServer.py

and open your browser. By default, the flask application uses port 5000 and can be 
accessed at http://localhost:5000/ .

.. _here: https://dry-lake-20339.herokuapp.com/
