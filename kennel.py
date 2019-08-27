animals_in_kennel = [
    {
        "id": 1,
        "breed": "German Shepherd",
        "age": 3,
        "name": "Jack"
    },
    {
        "id": 2,
        "breed": "Siamese",
        "age": 9,
        "name": "Shy"
    },
    {
        "id": 3,
        "breed": "Labradoodle",
        "age": 5,
        "name": "Avett"
    },
    {
        "id": 4,
        "breed": "Shnauzer",
        "age": 1,
        "name": "Gypsy"
    },
]

# Produce this output
# Key "id" = 1
# Key "breed" = German Shepherd
# Key "age" = 3
# Key "name" = Jack
# Key "id" = 2
# Key "breed" = Siamese
# Key "age" = 9
# Key "name" = Shy
# Key "id" = 3
# Key "breed" = Labradoodle
# Key "age" = 5
# Key "name" = Avett
# Key "id" = 4
# Key "breed" = Shnauzer
# Key "age" = 1
# Key "name" = Gypsy

# My answer
for eachitem in animals_in_kennel:
    holdtheid = eachitem["id"]
    holdthebreed = eachitem["breed"]
    holdtheage = eachitem["age"]
    holdthename = eachitem["name"]
    print('key "id" =', holdtheid)
    print('key "breed" =', holdthebreed)
    print('key "age" =', holdtheage)
    print('key "name" =', holdthename)

# vertical spacing
print(" ")
print("Output from Steve's method----->")
# Steve's answer:
for eachanimal in animals_in_kennel:
    for k, v in eachanimal.items():
        print(f'Key "{k}" = {v}')
