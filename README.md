# BE DAL #

Thanks for checking out our repository. We love this project, hope you do too.

**DO NOT RUN IN PRODUCTION. ONLY LOCALLY.**

# How to run this code #

##You need to install *Python Programming Language*, *PIL*, *Git* 
and/or *SQLite3*, *MySQLdb*.##

		# installs python and PIL
		sudo apt-get install python python-imaging 
		# for sqlite
		sudo apt-get install python-pysqlite2 sqlite3
		# for mysql
		sudo apt-get install python-mysqldb
		
##Django##

		# try
		sudo apt-get install python-django
		# if it does not work, download the latest version of django from [here](http://www.djangoproject.com/download/).

##Git##
		
		# download it !
		sudo apt-get install git-core
		
		# configure it !
		git config --global user.name "your_username"
		git config --global user.email your@email.com
		
		# clone the repo
		git clone git://github.com/be-dal/be_dal.git
		
		# change dir
		cd be_dal/

##Configure##

From the **root dir** open **settings.py** with a text-editor (gedit, vim, emacs, or any other...)
Open the python command line and type this:

		from random import choice
		
		print ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
		
		# Copy the result.
		# In **settings.py** find this line:
		SECRET_KEY = ''
		
		# REPLACE IT WITH
		SECRET_KEY = '[what_you_copied]'
		
###Then if you are planning to use SQLite:###

		# In **settings.py** find the next lines:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': '',                      # Or path to database file if using sqlite3.
            'USER': '',                      # Not used with sqlite3.
            'PASSWORD': '',                  # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }
    
    # REPLACE IT WITH:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'db/db.db',                      # Or path to database file if using sqlite3.
            'USER': '',                      # Not used with sqlite3.
            'PASSWORD': '',                  # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }

###If you are planning to use MySQL:###

		# In **settings.py** find the next lines:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': '',                      # Or path to database file if using sqlite3.
            'USER': '',                      # Not used with sqlite3.
            'PASSWORD': '',                  # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }
    
    # REPLACE IT WITH:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': '[the database name]',                      # Or path to database file if using sqlite3.
            'USER': '[mysql user]',                      # Not used with sqlite3.
            'PASSWORD': '[mysql password]',                  # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }
    
    # DO NOT FORGET CHANGING all that is between [text]


##Sync the database and run the dev server##

Go to the **root dir** from your terminal and run:

    python manage.py syncdb

Say 'yes' if it asks you to create a superuser, otherwise, when `syncdb` is finished
run:

    python manage.py createsuperuser
    
We can now start the **dev** server, have fun and write awesome code !

    # To start the dev server run from the **root dir**:
    python manage.py runserver
    # To use another port or IP run:
    python manage.py runserver [the_ip]:[the_port]
    # Example
    python manage.py runserver 0.0.0.0:5000

Now you can visit from your browser: http://localhost:8000/
Or: http://[the_ip]:[the_port]

##HELP##

**root dir**: It is when you go to `be_dal/` directory
**dev**: development

For more help contact us at "bedal75@gmail.com"
