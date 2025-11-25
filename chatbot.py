print("Chatbot: Hello! I am your simple chatbot. Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hi" or user == "hello":
        print("Chatbot: Hello! How can I help you?")
    
    elif "your name" in user:
        print("Chatbot: I am a Python rule-based chatbot!")

    elif "how are you" in user:
        print("Chatbot: I'm doing great, thank you!")

    elif "help" in user:
        print("Chatbot: Sure! Tell me what you need help with.")

    elif "bye" in user:
        print("Chatbot: Goodbye! Have a nice day 😊")
        break

    else:
        print("Chatbot: Sorry, I didn't understand that.")
