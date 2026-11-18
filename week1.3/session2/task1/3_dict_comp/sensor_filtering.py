# Reference solution (rewritten after original work was lost)
# Week 1.3, Session 2: Home Sensor Filtering

home_sensors = {"Living Room Thermostat": 85, "Front Door Lock": 15, "Kitchen Smoke Detector": 90, "Basement Flood Sensor": 8}

# dictionary comprehension to filter all sensors with battery level less than 20
# Expected Output: {'Front Door Lock': 15, 'Basement Flood Sensor': 8}
# Key idea: {key: value for key, value in dict.items() if condition}
# .items() gives us each (sensor name, battery level) pair to test.
low_battery = {sensor: level for sensor, level in home_sensors.items() if level < 20}


# print the new dictionary with battery less than 20 to verify
print(low_battery)
