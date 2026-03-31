import requests
import json


# Function to fetch data from API

def fetch_api_data(url):
    try:
        response = requests.get(url)

        # Check if request was successful
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Received status code {response.status_code}")
            return None

    except Exception as e:
        print(f"Exception occurred: {e}")
        return None



# Function to process JSON response

def process_data(data):
    processed = []

    for item in data:
        # Extract meaningful fields
        processed_item = {
            "id": item.get("id"),
            "title": item.get("title"),
            "status": "completed" if item.get("completed") else "pending"
        }
        processed.append(processed_item)

    return processed


# Function to save JSON to file

def save_to_file(data, filename):
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"\nData successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")



# Main execution

def main():
    api_url = "https://jsonplaceholder.typicode.com/todos"

    print("Fetching data from API...\n")

    raw_data = fetch_api_data(api_url)

    if raw_data:
        processed_data = process_data(raw_data)

        # Print output to terminal
        print("Processed Data (First 5 records):\n")
        for item in processed_data[:5]:
            print(item)

        # Save to JSON file
        save_to_file(processed_data, "output.json")


if __name__ == "__main__":
    main()