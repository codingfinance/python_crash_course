from car import Battery, Car, ElectricCar

c1: Car = Car("ford", "f1", 2020)
print(c1.get_descriptive_name())

# Read Miles
c1.read_odometer()

# update miles
c1.update_odometer(250)
c1.read_odometer()

# try to roll back the odometer
c1.update_odometer(150)

# add incremental miles
c1.increment_odometer(miles_added=50)
c1.read_odometer()

