from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from flask import Flask, render_template


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
    "აქ შედი https://google.com/"

]
list_to_train2 = [
    "გამარჯობა",
    "გაგიმარჯოს",
    "რა გქვია?",
    "ასისტენტი",
    "რამდენი წლის ხარ?",
    "მე შემქმნეს 2023 წელს...",
    "რა გინდა?",
    "მშვიდობა :) ... რა უნდა მინდოდეს გეხმარები..."

]

# list_trainer = ListTrainer(bot)
#
# list_trainer.train(list_to_train)
# list_trainer.train(list_to_train2)

# while True:
#     user_response = input("მომხმარებელი: ")
#     print("ჩათ-ბოტი: " + str(bot.get_response(user_response)))


@app.route("/")
def main():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

