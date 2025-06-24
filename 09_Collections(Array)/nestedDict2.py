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
  if key == 'address':
    print('address:')
    for add_key,add_value in value.items():
        print('\t',add_key,':', add_value)
  else: 
    print(key,':',value)