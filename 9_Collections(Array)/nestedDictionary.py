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
    print(f"\n{child}")
    for key, value in info.items():
        if key == "address":
            print("address:")
            for addr_key, addr_value in value.items():
                if addr_key == "Tole":
                    print("  Tole:")
                    for tole_key, tole_value in addr_value.items():
                        print(f"    {tole_key}: {tole_value}")
                else:
                    print(f"  {addr_key}: {addr_value}")
        else:
            print(f"{key}: {value}")
