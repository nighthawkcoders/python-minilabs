"""
This code will read the access log from the Nighthawk Coders Website

"""


with open("access.txt") as access_log:
    log_data = access_log.read()


import re # importing the python regex module (built into python)
from collections import Counter

def matches():
    
    IP_REGEX = r"\d+\.\d+\.\d+\.\d+ - -"
    ip_matches = re.findall(IP_REGEX, log_data)
    return ip_matches

def total_visits():
    ip_matches = matches()
    print(len(ip_matches), "total visits")

def unique_visits():
    ip_matches = matches()
    print(len(set(ip_matches)), "unique visits")

def search_by_ip():

    print("enter an ip to search for...")

    ip_selection = input()
    ip_selection = ip_selection.strip() #this gets rid of any leading or trailing spaces

    ip_matches = matches()
    counts = {}
    for ip in ip_matches:

        ip = ip[:-4] # This gets rid of the weird - - at the end of the ip 

        previous_val = counts.get(ip, 0)

        counts[ip] = previous_val + 1

    print(counts[ip_selection],"visits")
    


def most_active_ips():
    ip_matches = matches()
    ip_counter = Counter(ip_matches)

    most_common_5 = ip_counter.most_common()[:5]
    for ip, count in most_common_5:
        print("USER", ip[:-4], "USED THE WEBSITE", count, "TIMES")
    
    # A python Counter object can be accessed just like a python dict.

    # If we want to find who used the website the most we can used Counter's built in method most_common()
    # most_common() return a list of tuples like this [('172.69.35.51 - -', 18), ('104.2.87.139 - -', 17), ... ]
    # The tuples are in order from most seen to least seen so if we want to get the 5 most common we just select the first 5



def mot_popular_pages():

    PAGE_REGEX = r"\"http://.+\" "
    page_matches = re.findall(PAGE_REGEX, log_data)
    page_counter = Counter(page_matches)

    most_common_5 = page_counter.most_common()[:5]
    for page, count in most_common_5:
        print("PAGE", page, "WAS USED", count, "TIMES")






