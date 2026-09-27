import json #module

student = {
"name": "Rahul",
"age": 20,
"skills": ["Python", "HTML"]
}
# Serialization: Python dictionary + JSON file
with open("student.json", "w") as file:
    json.dump(student, file)

# Deserialization: JSON file > Python dictionary
with open("student.json", "r") as file:
    data = json.load(file)

print(data)
print(data["skills"])