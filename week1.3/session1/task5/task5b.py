# Reference solution (rewritten after original work was lost)
# Week 1.3, Session 1: Task 5b

rivers = {
  "London": "Thames", 
  "Leeds": "Aire", 
  "Liverpool": "Mersey",
  "York": "Ouse"
}

# loop through the dict extracting key and value

for c, r in rivers.items():
    print(c, r)


# create 2 further for loops to iterate: 1. just through the keys, 2. just through the values
# hint: we looked at built in function for dicts last session

# 1. just the keys - .keys() (looping over the dict directly also gives the keys)
print("--- cities ---")
for c in rivers.keys():
    print(c)

# 2. just the values - .values()
print("--- rivers ---")
for r in rivers.values():
    print(r)
