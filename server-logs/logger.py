

"""
This code will read the access log from the Nighthawk Coders Website

"""

import re # importing the python regex module (built into python)

with open("access.txt") as access_log:
    log_data = access_log.read()

print("head", log_data[:200], "\n") #Print the first 200 characters of the access log, also known as a head


IP_REGEX = r"\d+\.\d+\.\d+\.\d+ - -"

ip_matches = re.findall(IP_REGEX, log_data)

print("visits", len(ip_matches))

print("unique visits", len(set(ip_matches)), "\n")

print("sample matches", ip_matches[:3])


#Next count how many times each IP accessed the website

# Method 1: for loops

counts = {}

for ip in ip_matches:

    ip = ip[:-4] # This gets rid of the weird - - at the end of the ip 

    previous_val = counts.get(ip, 0)

    counts[ip] = previous_val + 1


# Lets see how many times user 172.69.33.149 accessed the website
print("172.69.33.149 accessed the website", counts["172.69.33.149"], "times!")

# Method 2: using the counter module
# Python has many useful little modules like this one. Not only are they easier to use but run faster and more efficently

from collections import Counter

ip_counter = Counter(ip_matches)

# A python Counter object can be accessed just like a python dict.

# If we want to find who used the website the most we can used Counter's built in method most_common()
# most_common() return a list of tuples like this [('172.69.35.51 - -', 18), ('104.2.87.139 - -', 17), ... ]
# The tuples are in order from most seen to least seen so if we want to get the 5 most common we just select the first 5

most_common_5 = ip_counter.most_common()[:5]


print("This is a list of tuples", most_common_5)

for ip, count in most_common_5:
    print("USER", ip[:-4], "USED THE WEBSITE", count, "TIMES")