import sqlite3

# occultation_name = 4

con = sqlite3.connect('measurements.db')
cur = con.cursor()
cur.execute("CREATE TABLE occultation(occultation_name, latitude, longitude, event_type, start_time, end_time, beta_angle, month)")

cur.execute("CREATE TABLE plotData(occultation_name, altitude, concentration)")

cur.execute("INSERT INTO plotData values (?, ?, ?)", (1, 4, 2))



# altitude

#     fname		char(12),
#   lname		char(12),
#   bdate		date,
#   bplace	char(20), 
#   address	char(30),
#   phone		char(12),
#   primary key (fname, lname)


