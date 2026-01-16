# Defining the Tuple
myTuple = ("Apple", 10, "Orange", "Grapes", 20.0, 10)

# 1. Accessing by index (index 3 is the 4th item)
print(myTuple[3])        

# 2. Accessing the last item using negative indexing
print(myTuple[-1])       

# 3. Slicing from index 2 up to (but not including) index 4
print(myTuple[2:4])      

# 4. Slicing from the beginning up to index 4
print(myTuple[:4])       

# 5. Slicing from index 2 to the end
print(myTuple[2:])       


print("----sensor readings----")
sensor_readings = ("2026-01-16", 22.5, "Sunny", 1013.2, 45, "North", "Active")
print(sensor_readings[-1])  
print(sensor_readings[-3:])
print(sensor_readings[:4])
print(sensor_readings[1:5])