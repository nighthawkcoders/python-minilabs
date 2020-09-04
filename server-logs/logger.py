

"""
This code will read the access log from the Nighthawk Coders Website

"""

import re # importing the python regex module (built into python)

with open("access.log") as access_log:
    log_data = access_log.read()

print("head", log_data[:200], "\n") #Print the first 200 characters of the access log, also known as a head


IP_REGEX = r"\d+\.\d+\.\d+\.\d+ - -"

ip_matches = re.findall(IP_REGEX, log_data)

print("visits", len(ip_matches))

print("unique visits", len(set(ip_matches)))