from chatterbot import ChatBot
from time import time
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

bot = ChatBot("Crystal Chatbot", read_only=False,
              logic_adapters=[

                  {
                      "import_path": "chatterbot.logic.BestMatch",
                      "default_response": "ამ კითხვაზე ჯერ არ მაქვს პასუხი :)",
                      "maximum_similarity_threshold": 0.95
                  }
              ])


trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

# while True:
#     user_response = input("მომხმარებელი: ")
#     print("ჩათ-ბოტი: " + str(bot.get_response(user_response)))


trainer = ListTrainer(bot)
trainer2 = ListTrainer(bot)
trainer3 = ListTrainer(bot)
trainer4 = ListTrainer(bot)

# Basic Info about Crystal
trainer.train([
    "რა გქვია?",
    "ჩემი სახელია კრისტალ-ბოტი.",
    "რა გინდა?",
    "შევეცდები დაგეხმაროთ.",

])

# Beka's Stuff
trainer2.train([
    "ვინ შეგქმნა?",
    "მე შემქმნა ბექა ბიტარაშვილმა",
    "ვინ არის ბექა?",
    "ბექა არის QA ინჟინერი",
    "ვინ არის ბექა ბიტარაშვილი?",
    "ბექა არის QA ინჟინერი",

])

# Personal Stuff
trainer3.train([
    "ბექა ბიტარაშვილი",
    "QA ინჟინერი",

])

# Extra Stuff About Crystal
trainer4.train([
    "Work From Home or Office?",
    "Hybrid!!!",

])


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    user_text = request.args.get('userMessage')
    bot_response = str(bot.get_response(user_text))
    return bot_response


# @app.route("/get")
# def get_chatbot_response():
#     userText = request.args.get('userMessage')
#     return str(bot.get_response(userText))


if __name__ == "__main__":
    app.run(debug=True)
