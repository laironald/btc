btc
=======

### Environment

 * Ubuntu 13.10
 * Python 2.7
 * Redis
 * Apache2
 * SciPy
 * IPython + Friends (matplotlib 1.2.1, numpy 1.7.1, scipy 0.12.0, pandas 0.12.0)
 * App: Flask, Scss, SQLAlchemy
 * Bootstrap, AngularJS, jQuery, underscore.js
 * IPython Notebook: [https://btc.goideas.org:8888/](https://btc.goideas.org:8888/) -- password:btc

### Data Sources

 * [Bitcoin charts Markets API](http://bitcoincharts.com/about/markets-api/)

### Charts

 * [Bitcoinwidsom](http://bitcoinwisdom.com)
 * [Bitcoinity](http://bitcoinity.org/markets)

### Coin Apps

 * Kraken (advanced trading platform)
 * Coinbase (easiest way to get $ into BTC)
 * BTC-E (shady bulgarian website, with alt currency exposure)
 * Coin Ticker (iPhone app for Crypto portfolio tracking)

### Install

```
sudo apt-get update
sudo apt-get install -y git

sudo apt-get install -y python-pip
sudo apt-get install -y python-matplotlib
sudo apt-get install -y python-numpy python-scipy python-pandas
sudo apt-get install -y redis-server

sudo pip install -r requirements.txt --upgrade
```

### Launch the App
```
python app.py
```

Head to your browser: localhost:5000

# Bonus

### Setup VirtualBox Shared Folders

  * Enable shared folders (be sure to Auto Mount)
  * `sudo adduser USERNAME vboxsf` replace USERNAME with your username
  * Restart Ubuntu
  * `ln -s /directory shortcut` to create a shortcut to the directory

### Install MySQL

```
sudo apt-get install -y mysql-server
sudo apt-get install -y python-mysqldb
```

### Apache for Flask (Optional)

```
sudo apt-get install -y apache2
sudo apt-get install -y libapache2-mod-wsgi
```

Add the code below to the Apache default `sudo pico /etc/apache2/sites-available/btc.conf`.

```
<VirtualHost *:80>

    ServerName btc.goideas.org
    ServerAdmin btc@goideas.org

    WSGIScriptAlias / /var/www/btc/start.wsgi
    <Directory /var/www/btc>
        Order deny,allow
        Allow from all
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/error.log
    LogLevel warn
    CustomLog ${APACHE_LOG_DIR}/access.log combined

</VirtualHost>
```

 * Place file in `/var/www/btc/start.wsgi`
 * make sure to reference the path of the app

```
import sys
sys.path.append("/home/ubuntu/btc")

from app import app as application
```

  * Enable the site

``` 
sudo a2ensite btc
sudo service apache2 restart
```

  * Some basic (guidance)[https://www.digitalocean.com/community/articles/how-to-deploy-a-flask-application-on-an-ubuntu-vps]

### Setup Ipython Notebook (Optional)

  * Create a profile for the server `ipython profile create nbserver`
  * Create a self-signed certificate file `openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout mycert.pem -out mycert.pem`
  * Install Python dependencies `sudo pip install pyzmq tornado`
  * Create a password & save the SHA hash

```
sudo pip install py

from IPython.lib import passwd
passwd("btc")
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
# Optional
c.FileNotebookManager.notebook_dir = u'/home/ubuntu/btc/nbook'
```

  * Launch the IPython Notebook: `ipython notebook --profile=nbserver`
  * [More detailed instructions](http://nbviewer.ipython.org/github/Unidata/tds-python-workshop/blob/master/ipython-notebook-server.ipynb)

