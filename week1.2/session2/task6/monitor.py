# Reference solution (rewritten after original work was lost)
# Week 1.2, Session 2: Task 6

from datetime import datetime

# Step 1: Get user inputs (int() converts the typed text into whole numbers)

temperature = int(input("Enter machine temperature (°C): "))
pressure = int(input("Enter machine pressure (PSI): "))
status = int(input("Enter operational status (1 = operating, 0 = stopped): "))

# Step 2: Evaluate operating conditions
# Each if/elif/else chain picks exactly ONE message.
# We store each message in a variable too, so it can be logged later.

# Temperature
if temperature > 80:
    temp_message = "Temperature too high! Recommend shutting down the machine."
elif temperature >= 50:
    # we only get here if temperature <= 80, so this means 50 to 80
    temp_message = "Temperature is within safe limits."
else:
    temp_message = "Machine temperature is low. No action needed."
print(temp_message)

# Pressure
if pressure > 100:
    pressure_message = "High pressure detected! Recommend maintenance."
elif pressure >= 70:
    pressure_message = "Pressure is stable."
else:
    pressure_message = "Pressure is low. System operating normally."
print(pressure_message)

# Step 3: Determine status
# 'or' -> unsafe if EITHER reading is too high

if status == 1:
    if temperature > 80 or pressure > 100:
        status_message = "WARNING: Machine running in unsafe conditions! Shut it down."
    else:
        status_message = "Machine is running normally."
else:
    status_message = "Machine is stopped. No immediate action needed."
print(status_message)

# Extension: log the results to machine_log.txt with a timestamp
# "a" (append) mode adds to the end of the file instead of overwriting it

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("machine_log.txt", "a") as log:
    log.write(f"[{timestamp}] Temperature: {temperature}°C, Pressure: {pressure} PSI, Status: {status}\n")
    log.write(f"[{timestamp}] {temp_message}\n")
    log.write(f"[{timestamp}] {pressure_message}\n")
    log.write(f"[{timestamp}] {status_message}\n")
