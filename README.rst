Luther College GenEd Course Database
====================================

Overview
--------

This is a web application that searches through the courses offered at Luther College and allows users to search through those courses based on the All College General Education requirements. Currently, users are allowed to search by a single GenEd or by multiple requirements.

A beta version of this web service is deployed on heroku here_. 

Requirements
------------

In order to run this application, you will need:

	* Python 2.7 -- newer versions may work but have not been thoroughly tested.
	* psqcopg2
	* Flask
	* Jinja2

Alternatively, you can just install the modules via pip:

::

	$ sudo pip install -r requirements.txt

.. _here: https://dry-lake-20339.herokuapp.com/
