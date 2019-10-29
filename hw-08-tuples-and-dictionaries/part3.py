
state_capitals = {
    'Alaska' : 'Juneau',
    'Colorado' : 'Denver',
    'Oregon' : 'Salem',
    'Texas' : 'Austin'
}

def reverse_lookup(state_capitals, town):
    for k,v in state_capitals.items():
        if v == town:
            return k

# inverted_dict = dict([[v,k] for k,v in state_capitals.items()])   fun try...does not handle None correctly
# print (inverted_dict["Denver"], inverted_dict["Salem"], inverted_dict["Sacramento"])
s
print(reverse_lookup(state_capitals, 'Denver'))
print(reverse_lookup(state_capitals, 'Salem'))
print(reverse_lookup(state_capitals, 'Sacramento'))
