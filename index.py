from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from flask import Flask, render_template, url_for, request


app = Flask(__name__)

bot = ChatBot("Gtech Chatbot", read_only=False,
              logic_adapters=[

                  {
                      "import_path": "chatterbot.logic.BestMatch"
                      # "default_response": "I don't have an answer to this question yet :)",
                      # "maximum_similarity_threshold": 0.95
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

# Basic Info about Gtech
trainer.train([
    "What is your name?",
    "My name is Gtech_Bot.",
    "What is Gtech?",
    "Georgia Tech is tech talent house :)",
    "Tell me about Gtech",
    "Gtech is team of skills and passion, consolidating our efforts to make a difference",
    "Who is the founder of Gtech?",
    "Tamu Robinson & Pascal Lauffer",
    "Where is the Gtech office?",
    "Tbilisi Gardens, 10 Mikheil Asatiani Street",
    "Gtech Services",
    "Graphic Design, QA Testing, Data, AI, UX/UI, Blockchain, Web Development",
    "Tell me about Gtech Team",
    "Gtech team is a group of people with the same vision and values. Things that matter in the company are shared: "
    "quality of work, advancing in learning, communications, and feedback from clients, reaching the deadlines, "
    "time management, responsibilities, positive vibes, and fun.",

])

# Beka's Stuff
trainer2.train([
    "Who made you?",
    "I was created by Beka Bitarashvili",
    "Who is Beka Bitarashvili?",
    "Beka is a QA Engineer in Gtech",


])

# Personal Stuff
trainer3.train([
    "Nika Kalandadze", "Nika is a Front Dev at Gtech",
    "Irakli Chelidze", "Irakli is a Product Owner",
    "Giorgi Metonidze", "Giorgi is a Back Dev at Gtech",
    "Beka Bitarashvili",
    "Beka is a QA Engineer",
    "Lega",
    "Lega is a UX/UI Designer",
    "Tamu",
    "Be careful my friend :) Ask me Something else...",
    "Tamu Robinson",
    "Be careful my friend :) Ask me Something else...",

])

# Extra Stuff About Gtech
trainer4.train([
    "Thursday",
    "Pizza Day at Gtech!",
    ""


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

