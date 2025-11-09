year = int(input("What's your year of birth?: "))

"""
Play Computer identified the bug: >= should be there
1994 was the year where GenZ commenced, but > 1994 means 
that GenZ started from 1995 whereas we know GenZ began frm 1994: 

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year > 1994 and year < 2013:
    print("You are a Gen Z.")
    
"""

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year >= 1994 and year < 2013:
    print("You are a Gen Z.")
