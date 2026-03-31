import requests
import json

# Call API
response = requests.get("https://api.github.com")

# Convert to JSON
data = response.json()

# Save to file
with open("github_data.json", "w") as f:
    json.dump(data, f)

# Read file
with open("github_data.json") as f:
    saved_data = json.load(f)

print(saved_data["current_user_url"])