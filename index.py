students = {
    "name": "raj",
    "age":32,
    "address":{
        "city":"Inaruwa",
        "state": 1,
        "Tole":"chaudary tole"
    }
}

for key,value in students.items():
  if "name" in key  or "age" in key:
   print(key,value)
  if "address" in key:
     for a,b in students["address"].items():
        print(a,b)