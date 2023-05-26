from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

bot = ChatBot("GeorgianAIChatbot", read_only=False,
              logic_adapters=[

                  {
                      "import_path": "chatterbot.logic.BestMatch",
                      "default_response": "ამ კითხვაზე ჯერ არ მაქვს პასუხი :)",
                      "maximum_similarity_threshold": 0.9
                  }
              ])

list_to_train = [
    "გამარჯობა",
    "მოგესალმებით...",
    "რა გქვია?",
    "ჩემი სახელია ჩათ-ბოტი",
    "რამდენი წლის ხარ?",
    "მე ასაკი არ მაქვს",
    "რა გინდა?",
    "ჩემი მიზანია დავეხმარო ადამიანებს და ვუპასუხო მათ ყველა შეკითხვას",
    "რამე საიტი მითხარი",
    "აქ შედი https://google.com/",
    "ანეგტოდი მომიყევი",
    "სვანი ინტერნეტში შევიდა და დაიკარგა :)",


]


# trainer = ChatterBotCorpusTrainer(bot)
# trainer.train("chatterbot.corpus.english")


list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train)


# while True:
#     user_response = input("მომხმარებელი: ")
#     print("ჩათ-ბოტი: " + str(bot.get_response(user_response)))


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
