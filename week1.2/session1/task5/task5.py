# Reference solution (rewritten after original work was lost)
# Week 1.2, Session 1: Task 5

rivers = {
    "London": "Thames",
    "Leeds": "Aire",
    "Liverpool": "Mersey"
}

print(rivers)

# Add two new entries to the rivers database
# assigning to a new key adds a new key:value pair
rivers["York"] = "Ouse"
rivers["Newcastle"] = "Tyne"
print(rivers)

# Display all the keys
print(rivers.keys())

# Display all the values
print(rivers.values())

# Display all the key:value pairs, as tuples
print(rivers.items())

# Delete an entry from the rivers database
# del removes the key and its value (rivers.pop("Liverpool") would also work)
del rivers["Liverpool"]
print(rivers)

# Additional work: multiple rivers per town/city
# make each value a LIST of rivers instead of a single string
rivers_multi = {
    "London": ["Thames", "Lea"],
    "Leeds": ["Aire"],
    "York": ["Ouse", "Foss"]
}
print(rivers_multi)
print(rivers_multi["York"])
