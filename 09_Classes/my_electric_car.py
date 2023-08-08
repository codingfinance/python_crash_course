from car import ElectricCar

c1 = ElectricCar("tesla", "cybertruck", 2024)
print(c1.get_descriptive_name())

print(c1.battery.battery_size)

print(c1.battery.get_range())