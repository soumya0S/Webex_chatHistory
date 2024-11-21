import json

def load_messages(file_path):
    """Load messages from a JSON file."""
    with open(file_path, 'r') as file:
        return json.load(file)

def organize_conversations(messages):
    """Organize messages into conversations with only text fields."""
    # Sort messages by creation time to handle chronological order
    messages.sort(key=lambda x: x['created'])

    # Dictionary to hold parent messages and their replies
    conversations = {}

    # Organize messages into conversations
    for message in messages:
        if "text" not in message:
            # Skip this message if it doesn't have a 'text' field
            print(f"Skipping message with ID {message.get('id', 'unknown')} due to missing 'text'")
            continue

        parent_id = message.get("parentId")
        text_only = {"text": message["text"]}
        
        if parent_id:
            if parent_id not in conversations:
                # Attempt to find the parent message
                parent_message = next((msg for msg in messages if msg['id'] == parent_id), None)
                if parent_message and "text" in parent_message:
                    conversations[parent_id] = {
                        "parentMessage": {"text": parent_message["text"]},
                        "replies": []
                    }
                else:
                    # Parent ID is not found or parent message doesn't have 'text'; treat as standalone
                    conversations[message['id']] = {
                        "parentMessage": text_only,
                        "replies": []
                    }
            else:
                conversations[parent_id]["replies"].append(text_only)
        else:
            # This is a standalone message or the start of a new conversation
            if message['id'] not in conversations:
                conversations[message['id']] = {
                    "parentMessage": text_only,
                    "replies": []
                }

    # Convert dictionary to a list for easy processing
    return list(conversations.values())

def main():
    # Load messages from the filtered JSON file
    file_path = 'filteredChatroomHistory.json'
    messages = load_messages(file_path)

    # Organize messages into conversations
    conversation_list = organize_conversations(messages)

    # Specify the output file name
    output_file_path = 'organizedConversations.json'

    # Write the organized conversations to the output file
    with open(output_file_path, 'w') as output_file:
        json.dump(conversation_list, output_file, indent=2)

    print(f"Organized conversations have been saved to {output_file_path}")

if __name__ == "__main__":
    main()