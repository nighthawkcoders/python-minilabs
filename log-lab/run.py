from analyzer import *

intro_text = """
Log-Lab:
1. Total Visits
2. Unique Visitors
3. Search by IP
4. Most Active IP's
5. Most Popular Pages
q/Q to quit

enter a number to choose an option...
"""

option_methods = {
    1:total_visits,
    2:unique_visits,
    3:search_by_ip,
    4:most_active_ips,
    5:mot_popular_pages
}


while True:

    print(intro_text)
    selection = input()

    if selection.lower() == 'q':
        break

    try:

        
        selection = int(selection)
        
        selected_method = option_methods[selection]

        selected_method()

    except Exception as e:
        print(e)
        print("Whoops that didn't exist")

