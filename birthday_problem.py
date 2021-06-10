# 1. Need to create an empty calendar
# 2. Need to fill it w/ random b-days
# 3. Need to figure out if there's any duplicates

import random

days = 365 
people = 25
trials = 1000000
found = 0
for t in range(trials):
    # 1. Create empty calendar
    calendar = [0] * days

    # 2. Fill calendar w/ random b-days
    for i in range(people):
        r = random.randint(0, days-1)
        calendar[r] += 1
    #print(calendar)

    # 3. Find duplicates of b-days
    duplicate = False
    for i in range(days):
        if calendar[i] > 1:
            duplicate = True
            break
    if duplicate: found += 1
print(found/trials)
"""
#1. Create empty calendar
# Can do it 3 ways

# 1st way: calendar = [0] * days

# 2nd way: calendar = []
#           for i in range(days):
#           calendar.append(0)

# 3rd way (list comprehension):
calendar = [i for i in range(days) if i % 2 == 1]
calendar2 = []
for i in range(1, 10, 2):
    calendar2 += [i, 0] # 2-item list
print(calendar2) # Glues this thing onto calendar2 list every time

# Shows can glue 2 lists together with plus opperator
c3 = calendar + calendar2
print(c3)
"""
"""
python3 birthday_problem.py 
0.569
"""