btc
=======

### Environment

 * Ubuntu 12.10
 * Python 2.7
 * Redis
 * Apache2

### Structure

 *  app.py  #
 *  base    # core framework libraries
 *  pg      # class for postgres interaction
 * recipes # 

### PG (PostGres Interaction)

##### methods

 * `cursor`, returns the cursor
 * `tables`, returns all the tables in the database
 * `columns(table)`, returns the columns related to the table
 * `records(table, limit, header)`, returns the first limit# of records related to the table
 * `count(table)`, returns the number of records related to the table
 * `csv(data, filename)`, outputs data in a csv file


### Install

```
sudo apt-get update
sudo apt-get install -y git

sudo apt-get install -y python-pip
sudo apt-get install -y python-matplotlib python-scipy python-pandas python-sympy python-nose
sudo apt-get install -y python-psycopg2

sudo apt-get install -y apache2
sudo apt-get install -y libapache2-mod-wsgi

sudo apt-get install -y redis-server

sudo apt-get install -y libpq-dev postgresql

sudo pip install -r requirements.txt
```

Note: easy Install using `go.sh` in the `defaults` directory.


### Setup Ipython Notebook (Optional)

  * Create a profile for the server `ipython profile create nbserver`
  * Create a self-signed certificate file `openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout mycert.pem -out mycert.pem`
  * Create a password & save the SHA hash

```
from IPython.lib import passwd
passwd("storefront")
```

  * Configure the notebook profile `~/.ipython/profile_nbserver/ipython_notebook_config.py`

```
c.IPKernelApp.pylab = 'inline'  # if you want plotting support always
# Notebook config
c.NotebookApp.certfile = u'/home/ubuntu/mycert.pem'
c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False
c.NotebookApp.password = u'[your hashed password]'
# It's a good idea to put it on a known, fixed port
c.NotebookApp.port = 8888
```

  * Launch the IPython Notebook: `ipython notebook --profile=nbserver`
  * [More detailed instructions](http://nbviewer.ipython.org/github/Unidata/tds-python-workshop/blob/master/ipython-notebook-server.ipynb)

### Configure PostgreSQL (not necessary for API)

```
adduser u44nfta1khmrf1
sudo su - postgres
psql template1
```

Once in psql

```
psql (9.1.10)
Type "help" for help.

template1=# CREATE USER u44nfta1khmrf1 WITH PASSWORD 'p62cd01rjlb43ra8alincsn50je';
template1=# CREATE DATABASE dc1ef4tl4qmafe;
template1=# GRANT ALL PRIVILEGES ON DATABASE dc1ef4tl4qmafe TO u44nfta1khmrf1;
template1=# \q
```

Login to user (specify password)

```
sudo su - u44nfta1khmrf1
psql -h ec2-50-19-252-217.compute-1.amazonaws.com -p 5612 -U u44nfta1khmrf1 dc1ef4tl4qmafe
```

### Configuring Apache for Flask (Optional)

Add the code below to the the Apache default `sudo pico /etc/apache2/sites-available/default`.

```
<VirtualHost *:80>
    ServerAdmin webmaster@localhost

    ...

    WSGIDaemonProcess front user=www-data group=www-data threads=5
    WSGIScriptAlias / /var/www/front/start.wsgi

    <Directory /var/www/front>
        WSGIProcessGroup front
        WSGIApplicationGroup %{GLOBAL}
        Order deny,allow
        Allow from all
    </Directory>

    ...

</VirtualHost>
```

#### Sample start.wsgi file for Apache2

 * Place file in `/var/www/front` (or equivalent)
 * make sure to reference the path of the app

```
import sys
sys.path.append("/home/ubuntu/pyfront")

from app import app as application
```
