# Converting Python to JSON
import json

data = {
    "name": "Raj",
    "age": 24,
    "skills": ["Python", "JavaScript"]
}

json_data = json.dumps(data)
print(json_data)

# Converting JSON to Python
import json

json_string = '{"name": "Raj", "age": 24}'
data = json.loads(json_string)
print(data["name"])  # Output: Raj
print(data["age"])  # Output: 24

# Converting Python to CSV(Saving JSON to a file)
with open("data.json", "w") as f:
    json.dump(data, f)
    
# Converting CSV to Python(Loading JSON from a file)
with open("data.json", "r") as f:
    data = json.load(f)
    print(data["name"])
