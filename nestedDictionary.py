myfamily = {
  "child1" : {
    "name" : "Emial",
    "year" : 2004,
    "address":{
        "city":"Inaruwa",
        "state": 1,
        "Tole":{
            "road_no":2,
             "road_name":"new road"
        }   
    }
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007,
    "address":{
        "city":"Drn0",
        "state": 1,
        "Tole":{
            "road_no":2,
             "road_name":"new road"
        }   
    }
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011,
    "address":{
        "city":"Khorsane",
        "state": 4,
        "Tole":{
            "road_no":2,
             "road_name":"new road"
        }   
    }
  }
}
for a,b in myfamily.items():
    print(a)
    for x,y in myfamily[a].items():
        print(x,y)
        if "address" in x:
            for key,value in y.items():
                print(key,value)
