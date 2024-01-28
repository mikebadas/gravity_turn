import math
angle = 1.5*0.0174533    # початковий кут відхилення
velocity = 102           # початкова швидкість
height = 1000            # початкова висота
distance = 0             # початкове переміщення

for t in range(0, 174):

	change = 6378000*velocity*math.sin(angle)/(6378000+height)                        # формула темпу переміщення
	distance += change                                                                # загальне переміщення

	acceleration = math.sqrt(math.pow(6379380/(521300-2184*t)-9.8*math.cos(angle), 2) 
	+ math.pow(9.8*math.sin(angle), 2))                                               # формула результуючого прискорення

	velocity += acceleration                                                          # швидкість

	angle += math.asin(math.sin(angle)*9.8/velocity) - 360*0.0174533*change/40000000  # формула кута

	height += velocity*math.cos(angle)                                                # формула висоти

	print(angle/0.0174533, velocity, height, distance)




























#for t in range(0, 140):
#	change = 6378000*velocity*math.sin(angle)/(6378000+height)
#	distance += change
#	drag = math.pow(velocity, 2)
#	x = 677020-9*drag
#	y = 185070-26*t
#	a = x/y
#	b = math.pow(a,2)
#	c = 4*9*drag/y
#	d = math.pow(c,2)
#	e = math.sqrt(b+d) - 9.8*math.cos(angle)
#	f = math.pow(e,2) + math.pow(9.8*math.sin(angle),2)
#	acceleration = math.sqrt(f)
#	#acceleration = math.sqrt(math.pow(math.sqrt(math.pow((677020-9*math.pow(velocity, 2))/(185070-26*t),2) + math.pow(4*9*math.pow(velocity, 2)/(185070-26*t),2))-9.8*math.cos(angle),2) + math.pow(9.8*math.sin(angle),2))
#	velocity += acceleration
#	angle -= (math.atan(4*9*math.pow(velocity, 2))/(677020-9*math.pow(velocity, 2))-math.asin(math.sin(angle-math.atan(4*9*math.pow(velocity, 2)/(677020-9*math.pow(velocity, 2))))*9.8/velocity)) + 360*0.0174533*change/40000000
#	height += velocity*math.cos(angle)
#	t += 1
#	print(angle/0.0174533, acceleration, velocity, height, distance)

#for k in range(0, 706):
#	velocity = math.sqrt(2*3.986*math.pow(10,14)*((1/(6367444+velocity*math.cos(angle)+height))-(1/(6367444+height)))+math.pow(velocity, 2))
#	change = 6367444*velocity*math.sin(angle)/(6367444+height)
#	distance += change
#	angle += math.asin(math.sin(angle)*9.8/velocity) - 360*0.0174533*change/40000000
#	height += velocity*math.cos(angle)
#	k += 1
#print(velocity, height, distance, angle/0.0174533)





































#for k in range(0, 500):
#	velocity = math.sqrt(math.pow(velocity-9.8*math.cos(angle), 2) + math.pow(9.8*math.sin(angle), 2))
#	change = 6367444*velocity*math.sin(angle)/(6367444+height)
#	distance += change
#	angle += math.asin(math.sin(angle)*9.8/velocity) - 360*0.0174533*change/40000000
#	height += velocity*math.cos(angle)
#	k += 1
#print(velocity, height, distance, angle/0.0174533)