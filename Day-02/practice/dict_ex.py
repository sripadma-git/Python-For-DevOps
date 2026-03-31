info = {
    "name": "sri padma",
    "city": "kakinada",
    "age": 22,
    "hobbies": ["coding", "cooking", "dancing"]
}

print("I live in", info["city"])
print("my hobbies are", info["hobbies"])
print("my name is", info["name"])

info.update({"occipation": "student"})
print("my occipation is", info["occipation"])


for i in info:
    print(i, ":", info[i])