import sqlite3
from travel import Travel

conn = sqlite3.connect('travel.db')

c = conn.cursor()


c.execute(""" CREATE TABLE IF NOT EXISTS travel (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            tripName text,
            dest text,
            duration integer,
            package integer,
            price integer,
            available text
            ) """)

conn.commit()



trip_1 = Travel('Stockholm', 3, 'Basic', 450, 1)
trip_2 = Travel('Tallinn', 3, 'Basic', 300, 1)
trip_3 = Travel('Bali', 8, 'Basic', 1200, 1)
trip_4 = Travel('Bali', 8, 'Deluxe', 1750, 1)
trip_5 = Travel('Singapore-Malaysia', 8, 'Deluxe', 2500, 1)
trip_6 = Travel('Quebec', 5, 'Basic', 1200, 1)
trip_7 = Travel('Quebec', 6, 'Deluxe', 1800, 0)
trip_8 = Travel('Rwanda', 5, 'Basic', 800, 0)
trip_9 = Travel('Kenya', 7, 'Exclusive', 1600, 1)
trip_10 = Travel('Rusia', 6, 'Basic', 500, 1)


c.execute("INSERT OR REPLACE INTO travel (tripName, dest, duration, package, price, available) VALUES (:tripName, :dest, :duration,:package, :price, :available)", {
'tripName':trip_1.tripName, 'dest':trip_1.dest, 'duration':trip_1.duration, 
'package':trip_1.package, 'price':trip_1.price, 'available':trip_1.available})
conn.commit()

c.execute("Select * from Travel")
conn.commit()
print(c.fetchall())

conn.close()



#dest, duration, package, price, available

