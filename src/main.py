# main.py
from assistant import Assistant

def run_assistant(assistant):
    """Defines the initial interaction with the assistant."""
    print("✨ LILAI is waking up… How can I assist you today?")

    while True:
        user_input = input("> ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("👋 Bye for now! LILAI is powering down.")
            break
        reponse = assistant.generate_response(user_input)
        print(reponse)

        if _name_ == "_main_":
            assistant = Assistant()
            run_assistant(assistant)