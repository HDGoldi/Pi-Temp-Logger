# Pi-Temp-Logger #
A Python application for Raspberry Pi that logs temperature and humidity readings from a DHT22 sensor to a MySQL database every hour.

## Setup ##
1. [Install MySQL, Create database, database user and table.] 
	- CREATE TABLE script is in DHT22Readings.sql 
2. Set database info in the python script.
3. Set GPIO pin used for DHT22 data in the python script.
4. Download [pigpio], make sure pigpio.py is in the same dir as the script.
5. Download [DHT22] for PIGPIO, make sure DHT22.py is in the same dir as the script. 
6. Download [Schedule], make sure schedule.py is in the same dir as the script. (rename \__init\__.py)
7. Run command: *sudo apt-get install python-mysqldb*

## Start ##
1. Run command: *pigpiod* (from PIGPIO directory).
2. Run the python script.



## Start at boot ##
Make a file called startupscript.sh with this content:

```bash
#!/bin/sh
/<path>/pigpiod &
nohup python /<path>/pi-temp-logger.py &
```

Edit the file /etc/rc.local and add this line:
```bash
/<path>/startupscript.sh &
```

*Replace each `<path>` with your path to the files.*
[Install MySQL, Create database, database user and table.]: http://www.raspipress.com/2014/06/tutorial-install-mysql-server-on-raspbian/
[pigpio]: http://abyz.co.uk/rpi/pigpio/download.html
[DHT22]: http://abyz.co.uk/rpi/pigpio/examples.html
[Schedule]: https://github.com/dbader/schedule
