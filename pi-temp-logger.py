import pigpio, MySQLdb, DHT22, schedule, datetime, time

pi = pigpio.pi()
# Set second parameter to GPIO port of DHT22 data pin:
s = DHT22.sensor(pi, 4) 
# Set database info:
db_info = {'host':'localhost', 'user':'pi_login', 'pw':'Pa$$w0rd', 'db':'DHT22Readings'}

def get_readings_and_save_to_db():
    s.trigger()
    dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    con = MySQLdb.connect(db_info['host'], db_info['user'], db_info['pw'], db_info['db'])
    time.sleep(1)
    print('Reading for ' + dt + ":")
    print('Temperature: ' + '{:3.2f}'.format(s.temperature() / 1.))
    print('Humidity: ' + '{:3.2f}'.format(s.humidity() / 1.))
    with con:
        con.cursor().execute("INSERT INTO Reading(Datetime, Temperature, Humidity) \
                    VALUES ('" + dt + "'," + str(s.temperature()) + "," + str(s.humidity()) + ")")

for t in range(0,24):
    schedule.every().day.at(str(t) + ":00").do(get_readings_and_save_to_db)

print('Running... first readings at: ' + str(schedule.next_run()))

while True:
    schedule.run_pending()
    time.sleep(1)
