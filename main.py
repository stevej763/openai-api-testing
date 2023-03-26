import os
from dotenv import load_dotenv
import openai

load_dotenv()  # Load all the ENV variables into your os enviroment.
openai.api_key = os.getenv("OPENAI_API_KEY")  # Get your API key from env variable

reply_count = 0
msgs = []

session_name= input("Enter a unique session name: ")
os.makedirs(session_name)

assistant_type = input("What type of chatbot would you like to create?: ")
msgs.append({"role": "system", "content": assistant_type})
msgs.append({"role": "user", "content": "introduce yourself"})
introduction = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=msgs
)
introduction_response = introduction["choices"][0]["message"]["content"]
print(introduction_response)

print("Say hello to your new chatbot! Type quit() when done.")

while True:
    msg = input("YOU: ")
    if "quit()" in msg:
        break
    msgs.append({"role": "user", "content": msg})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=msgs
    )
    reply = response["choices"][0]["message"]["content"]
    with open(f"conversations/{session_name}/response-{reply_count}.md", "x") as file:
        file.write("Question:\n")
        file.write(msg)
        file.write("\n\nAnswer:\n")
        file.write(reply)
        file.close()

    msgs.append({"role": "assistant", "content": reply})
    reply_count += 1
    print("\nAI: " + reply + "\n")
