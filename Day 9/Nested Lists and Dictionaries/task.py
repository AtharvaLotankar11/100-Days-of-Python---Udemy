#Lists of Country-Capitals
capitals = {
    "India": "New Delhi",
    "France": "Paris",
    "Germany": "Berlin",
    "United Kingdoms": "London",
    "Japan": "Tokyo"
}

#Nested List in Dictionary
travel_log = {
    "India": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
    "France": ["Paris", "Versailles", "Dijon", "Lille"],
    "Germany": ["Berlin", "Frankfurt", "Stuttgart", "Rhine"],
    "United Kingdoms": ["London", "Newcastle", "Wales", "Scotland"],
    "Japan": ["Tokyo", "Kyoto", "Hiroshima", "Hokkaido"]
}

#print Lille and Wales
print(travel_log["France"][3])
print(travel_log["United Kingdoms"][2])

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

#Nested Dictionaries
dict_travel_log = {
    "India": {
        "numTimesVisited": 120,
        "cities_Visited": ["Mumbai", "New Delhi", "Kolkata", "Chennai"]
    },
    "France": {
        "numTimesVisited": 3,
        "cities_Visited": ["Paris", "Versailles", "Dijon", "Lille"]
    },
    "Germany": {
        "numTimesVisited": 8,
        "cities_Visited": ["Berlin", "Frankfurt", "Stuttgart", "Rhine"]
    },
    "United Kingdoms": {
        "numTimesVisited": 10,
        "cities_Visited":["London", "Newcastle", "Wales", "Scotland"]
    },
    "Japan": {
        "numTimesVisited": 1,
        "cities_Visited":["Tokyo", "Kyoto", "Hiroshima", "Hokkaido"]
    }
}

#print Stuttgart frm dict_travel_log
print(dict_travel_log["Germany"]["cities_Visited"][2])
