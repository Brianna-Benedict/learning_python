import sys
import random

# Import variables from command line:
# print(sys.argv)

assert(len(sys.argv) == 4)
trials = int(sys.argv[1]) # Converts string to int
days = int(sys.argv[2])
people = int(sys.argv[3])

# print((trials, days, people))

collisions = 0
for t in range(trials):
    
    # 1. Create an empty calendar
    calendar = [] # Empty list w/ 365 0's
    for i in range(days):
        calendar.append(0)
    # print(calendar)
    
    # 2. Fill w/ random b-days
    for i in range(people):
        bd = random.randint(0, days-1)
        calendar[bd] += 1
    # print(calendar)
    
    # 3. Are there any collisions?
    found = False
    for v in calendar: # Will give you the #
        if v > 1:
            found = True
            break
    
    # 4. Add 1 if we find any collisions
    if found: collisions += 1
print(collisions/trials)

"""
python3 new_birthday.py 100 365 25
0.58
"""