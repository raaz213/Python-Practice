import json

user = {
    "username": "rajkumar",
    "skills": ["Python", "React Native", "ML"],
    "active": True
}

# Write to file
with open("user.json", "w") as f:
    json.dump(user, f, indent=4) # indent=4 for better readability

# Read back
with open("user.json", "r") as f:
    loaded_user = json.load(f)

print("Username:", loaded_user["username"])
