# Define a function to respond to user inputs
def chatbot_response(user_input):
    # Convert user input to lowercase for easier comparison
    input_lower = user_input.lower()

    # Simple if-else statements based on predefined rules
    if "hello" in input_lower or "hi" in input_lower:
        return "Hello! How can I assist you today?"

    elif "how are you" in input_lower:
        return "I'm just a bot, but thanks for asking!"

    elif "your name" in input_lower:
        return "I'm a chatbot. You can call me ChatGPT."

    elif "bye" in input_lower or "goodbye" in input_lower:
        return "Goodbye! Have a great day."

    else:
        return "I'm sorry, I don't understand that. Could you please ask something else?"

# Main function to run the chatbot
def main():
    print("Welcome! Ask me something or say goodbye to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit' or user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        
        response = chatbot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
