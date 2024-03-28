import json
from difflib import get_close_matches

# Load JSON data into a Python dictionary
def load_data():
    with open("data.json") as f:
        data = json.load(f)
    return data

# Function to retrieve definition of a word
def get_definition(word):
    data = load_data()
    word = word.lower()  # Convert word to lowercase
    if word in data:
        return data[word]
    else:
        # Find similar words using difflib
        similar_words = get_close_matches(word, data.keys())
        if similar_words:
            suggestion = similar_words[0]
            yes_or_no = input(f"Did you mean '{suggestion}' instead? Enter Y if yes, or N if no: ").lower()
            if yes_or_no == 'y':
                return data[suggestion]
            else:
                return "Word not found. Please try again."
        else:
            return "Word not found. Please try again."

# Main function
def main():
    while True:
        word = input("Enter a word to get its definition (or 'q' to quit): ")
        if word.lower() == 'q':
            break
        definition = get_definition(word)
        print(definition)

if __name__ == "__main__":
    main()
