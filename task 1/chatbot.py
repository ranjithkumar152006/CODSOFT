print("Bot: Hello! I am a simple chatbot. You can ask me a few questions.")
print("Type 'exit' to end the chat.\n")

while True:
    user_input = input("You: ").lower()  # Convert input to lowercase

    if user_input == "byee":
        print("Bot: Goodbye! Have a nice day.")
        break
    elif "hello" in user_input or "hi" in user_input:
        print("Bot: Hello! How can I help you today?")
    elif "how are you" in user_input:
        print("Bot: I'm just a bot, but I'm doing great! How about you?")
    elif "your name" in user_input:
        print("Bot: I am ChatBot 1.0, your friendly assistant!")
    elif "time" in user_input:
        from datetime import datetime
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"Bot: Current time is {current_time}")
    else:
        print("Bot: Sorry, I don't understand that. Can you ask something else?")