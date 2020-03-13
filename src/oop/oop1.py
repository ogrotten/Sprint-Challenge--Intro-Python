# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
	pass

class FlightVehicle(Vehicle):
	# the parent is vehicle
	pass

class Starship(FlightVehicle):
	# the parent is FlightVehicle
	pass

class Airplane(FlightVehicle):
	# the parent is FlightVehicle
	pass

class GroundVehicle(Vehicle):
	# the parent is vehicle
	pass

class Car(GroundVehicle):
	# the parent is GroundVehicle
	pass

class Motorcycle(GroundVehicle):
	# the parent is GroundVehicle
	pass

