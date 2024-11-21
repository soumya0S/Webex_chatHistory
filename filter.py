import json

def filter_messages(input_file, output_file):
    # Read data from the input JSON file
    with open(input_file, 'r') as file:
        messages = json.load(file)
    
    # Filter each message to include only the desired keys
    filtered_messages = [
        {key: message[key] for key in ('id', 'text', 'created', 'parentId') if key in message}
        for message in messages
    ]
    
    # Write the filtered messages to the output JSON file
    with open(output_file, 'w') as file:
        json.dump(filtered_messages, file, indent=2)

# Specify the input and output file names
input_file = 'chatroomHistory.json'
output_file = 'filteredChatroomHistory.json'

# Call the function to filter messages
filter_messages(input_file, output_file)

print(f"Filtered messages have been saved to {output_file}")