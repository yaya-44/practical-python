bills_thickness = 0.11 * 0.001 # Meters (0.11 mm)
sears_height = 442 # Height (meters)
num_bills = 1
day = 1

while num_bills * bills_thickness < sears_height:
    print(day, num_bills, num_bills * bills_thickness)
    num_bills = num_bills * 2
    day = day + 1

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bills_thickness)