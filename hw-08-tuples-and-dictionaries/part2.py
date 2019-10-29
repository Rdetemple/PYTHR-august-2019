
humandict = {
    'emp1': {'name' : 'Jill Swanson', 'age' : '55', 'title' : 'Management', 'phone_number' : '555-1234', 'money': '$87,000'},
    'emp2': {'name': 'Leslie Knope', 'age' : '14','title' : 'Middle Management','phone_number' : '555-4321','money':'$87,020'},
    'emp3': {'name': 'Andy Dwyer', 'age' : '13','title' : 'Shoe Shining','phone_number' : '555-1122','money':'$87,002'},
    'emp4': {'name': 'April Ludgate', 'age' : '12','title' :'Administration', 'phone_number' :'555-3345','money':'$87,001'},
}

for key in humandict:
    #print(humandict[key]['name'], humandict[key]['title'])
    print(humandict[key]['name'],"in", humandict[key]['title'], "can be reached at",humandict[key]['phone_number'])

# Jill Swanson in Management can be reached at 555-1234.
# Leslie Knope in Middle Management can be reached at 555-4321.
# Andy Dwyer in Shoe Shining can be reached at 555-1122.
# April Ludgate in Administration can be reached at 555-3345.
#
# for key in my_dictionary:
#   print(my_dictionary[key])
#
# for key in my_dictionary:
#   print(key, ':', my_dictionary[key])
