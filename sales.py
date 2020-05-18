import sqlite3
from travel import Travel, Package

conn = sqlite3.connect(':memory:')

c = conn.cursor()
c.execute("PRAGMA table_info(table_name)")

c.execute(""" CREATE TABLE IF NOT EXISTS travel (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            tripName text,
            dest text,
            duration integer,
            package integer,
            price integer,
            available text,
            FOREIGN KEY(package)
            REFERENCES package
            ) """)

conn.commit()

c.execute(""" CREATE TABLE IF NOT EXISTS Package (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            package text,
            hotelStar integer,
            localTrans integer,
            guide integer

            ) """)

conn.commit()


def add_trip(trip):
    with conn:
        c.execute("INSERT OR REPLACE INTO travel (tripName, dest, duration, package, price, available) VALUES (:tripName, :dest, :duration,:package, :price, :available)", {
        'tripName':trip.tripName, 'dest':trip.dest, 'duration':trip.duration, 
        'package':trip.package, 'price':trip.price, 'available':trip.available})

def add_package(package):
    with conn:
        c.execute("INSERT OR REPLACE INTO package (package, hotelStar, localTrans, guide) VALUES(:package, :hotelStar,:localTrans, :guide)", {
        'package':package.package, 'hotelStar': package.hotelStar,
        'localTrans': package.localTrans,'guide': package.guide } )

def get_all_trip():
    c.execute("Select * from Travel")
    return c.fetchall()

def get_package_details():
    c.execute("Select * from package")
    return c.fetchall()

def get_trip_by_dest(dest):
    c.execute("Select * from Travel WHERE dest =:dest", {'dest': dest})
    return c.fetchall()

def update_price(trip, price):
    with conn:
        c.execute("""UPDATE travel SET price = :price where dest = :dest and package =:package""",
         {'dest': trip.dest, 'package': trip.package, 'price': price })

def delete_trip(dest, package):
    with conn:
        c.execute("""DELETE from travel where dest = :dest and package =:package""",
         {'dest': dest, 'package': package})
        





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

package_1 = Package('Basic', 1, 0, 0)
package_2 = Package('Deluxe', 2, 1, 0)
package_3 = Package('Exclusive', 4, 1, 1)


add_trip(trip_1)
add_trip(trip_2)
add_trip(trip_3)
add_trip(trip_4)
add_trip(trip_5)
add_trip(trip_6)
add_trip(trip_7)
add_trip(trip_8)
add_trip(trip_9)
add_trip(trip_10)

add_package(package_1)
add_package(package_2)
add_package(package_3)




#print(get_trip_by_dest('Stockholm'))

#delete_trip('Stockholm','Basic')

#print(get_all_trip())

print(get_package_details())





#dest, duration, package, price, available

# c.execute("INSERT OR REPLACE INTO travel (tripName, dest, duration, package, price, available) VALUES (:tripName, :dest, :duration,:package, :price, :available)", {
# 'tripName':trip_1.tripName, 'dest':trip_1.dest, 'duration':trip_1.duration, 
# 'package':trip_1.package, 'price':trip_1.price, 'available':trip_1.available})
# conn.commit()

# c.execute("Select * from Travel")
# conn.commit()
# print(c.fetchall())


# c.execute("Select * from Package")
# conn.commit()
# print(c.fetchall())

conn.close()
