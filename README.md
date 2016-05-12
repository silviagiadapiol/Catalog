## TABLE OF CONTENTS

* The program
* What's included
* Quick Start
* License


### THE PROGRAM
application.py is a Python file with a flask application that shows in a website a list of category with different items. Once the database has been created and populated, it can be interrogated through a browser; the file application.py defines the pages routes and all the functions to navigate them. It also manages the authentication system: it allows users to login and disconnect, and it consents only to logged-in users to add a new category; only the creator of each category can add, edit and delete items or edit and delete the category. Not logged-in users can see a pubblic (not editable) version of the app. It also gives a json serialized version of the data.


### WHAT'S INCLUDED

In Silvia Giada Piol GitHub fullstack-nanodegree-vm repository, inside vagrant/[catalog, ](https://github.com/silviagiadapiol/fullstack-nanodegree-vm/tree/master/vagrant/catalog) you can find the following files:

* db_setup.py _(it creates the catalog database (in this case babystuff.db) and its tables)_
* db_populator.py _(it adds a few categories and items to populate the database)_
* client_secrets.json _(it contains the client ID and the client secret for the google+ app)_
* fb_client_secrets.json _(it contains the client ID and the client secret for the facebook app)_
* application.py (it's a flask application that defines the pages routes and all the functions to navigate them; it also manages the authentication system with google+ or facebook)
* templates folder _(it contains the html files that can be rendered in order to view the different pages)_
* static folder _(it contains the style.css file that defines the style rules for the app)_
* README.md _(it contains the instructions for running the app)_


### QUICK START. 

* Fork the repository and clone it on local machine. 
* To create the empty database run the command `vagrant@vagrant-ubuntu-trusty-32:/vagrant/catalog$ python db_setup.py`
* To populate the database run the command `vagrant@vagrant-ubuntu-trusty-32:/vagrant/catalog$ python db_populator.py` 
* To run the application run the command `vagrant@vagrant-ubuntu-trusty-32:/vagrant/catalog$ python application.py`
* To test the application functionality open a browser at //localhost:8000/category and log in with google+ or facebook, then navigate the pages, create new categories and items, edit and delete what you created; also search for the json pages.


### LICENSE

Creator Silvia Giada Piol, this code is released under the [MIT LICENCE](http://choosealicense.com/licenses/mit/)