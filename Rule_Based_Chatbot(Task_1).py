def chatbot():
    print("Hello! I'm a simple chatbot. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello", "hey"]:
            print("Bot: Hello there! I'm glad to chat with you. ")

        elif "your name" in user_input:
            print("Bot: I'm ChatBot, your simple rule-based assistant .")

        elif "who are you" in user_input or "about you" in user_input:
            print("Bot: I'm a basic chatbot created using Python. I respond with predefined rules!")

        elif "about me" in user_input or "introduce yourself" in user_input:
            print("Bot: Sure! I'm a friendly Python chatbot built to demonstrate simple rule-based responses.")

        elif "how are you" in user_input:
            print("Bot: I'm doing great, thanks for asking! How about you?")

        elif "what can you do" in user_input:
            print("Bot: I can chat with you, tell the time/date, introduce myself, and more. Try asking!")

        elif "time" in user_input:
            from datetime import datetime
            now = datetime.now()
            print(f"Bot: The current time is {now.strftime('%H:%M:%S')}.")

        elif "date" in user_input:
            from datetime import datetime
            today = datetime.today().strftime('%Y-%m-%d')
            print(f"Bot: Today's date is {today}.")

        elif "bye" in user_input:
            print("Bot: Goodbye! Have a wonderful day 😊")
            break

        else:
            print("Bot: Sorry, I don’t understand that. Can you try something else?")

chatbot()
