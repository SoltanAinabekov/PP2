# Write a Python program to drop microseconds from datetime.
from datetime import datetime

# Get current datetime
current_datetime = datetime.now()

# Drop microseconds
new_datetime = current_datetime.replace(microsecond=0)

print("Original Datetime:", current_datetime)
print("Datetime Without Microseconds:", new_datetime)
