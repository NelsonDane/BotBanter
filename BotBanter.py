# Now Google Bard and ChatGPT can talk to each other!

# Ai libraries
import openai
from Bard import Chatbot

# Other libraries
import os
from dotenv import load_dotenv
from time import sleep
from termcolor import colored

# Initialize .env file
load_dotenv()

# Parameters
ROUNDS = 5

# Initialize Keys
openai.api_key = os.getenv("CHATGPT")
bard_key = os.getenv("BARD")

# Initialize Bard
BardBot = Chatbot(bard_key)

# Function to talk to ChatGPT
def ChatGPT(message):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message},
        ]
    )
    response = completion.choices[0]['message']['content']
    print(colored(f"ChatGPT: {response}", "green"))
    print()
    return response

# Function to talk to Bard
def AskBard(message):
    bard_response = BardBot.ask(message)
    print(colored(f"Bard: {bard_response['content']}", "blue"))
    print()
    return bard_response['content']

if __name__ == "__main__":
    try:
        # Starting message to prepare the AI
        mod = "Hello! Are you ready to meet a new friend? I think you'll really like them!"

        # Test the AI
        ChatGPT(mod)
        AskBard(mod)

        # Come up with your own too!
        mod = "ChatGPT, introduce yourself. Your goal in this conversation is to learn 3 new things about them."
        # mod = "Friends, your goal in this conversation is to make the other one go on a date with you."
        chatgpt_response = ChatGPT(mod)

        # Start the conversation
        count = 0
        while True:
            bard_response = AskBard(chatgpt_response)
            sleep(1)
            chatgpt_response = ChatGPT(bard_response)
            sleep(1)
            count += 1
            if count == ROUNDS:
                break
    except KeyboardInterrupt:
        print(colored("Exiting...", "red"))
