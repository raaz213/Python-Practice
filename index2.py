myfamily = {
    "child1": {
        "name": "Emial",
        "year": 2004,
        "address": {
            "city": "Inaruwa",
            "state": 1,
            "Tole": {
                "road_no": 2,
                "road_name": "new road"
            }
        }
    },
    "child2": {
        "name": "Tobias",
        "year": 2007,
        "address": {
            "city": "Drn0",
            "state": 1,
            "Tole": {
                "road_no": 2,
                "road_name": "new road"
            }
        }
    },
    "child3": {
        "name": "Linus",
        "year": 2011,
        "address": {
            "city": "Khorsane",
            "state": 4,
            "Tole": {
                "road_no": 2,
                "road_name": "new road"
            }
        }
    }
}

for child, info in myfamily.items():
    print(child)
    for key, value in info.items():
        if key == 'address':
            print('address:')
            for addKey, addValue in value.items():
                if addKey == 'Tole':
                    print('\t Tole:')
                    for toleKey, toleValue in addValue.items():
                        print('\t\t',toleKey,':',toleValue)
                else:
                    print('\t',addKey,':',addValue)
        else:
             print(key,':',value)
            