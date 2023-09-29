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
trainer5 = ListTrainer(bot)

# Basic Info about Crystal
trainer.train([
    "რა გქვია?",
    "ჩემი სახელია კრისტალ-ბოტი.",
    "რა გინდა?",
    "შევეცდები დაგეხმაროთ.",
    "რა ხარ?",
    "ბოტი",
    "დამელაპარაკე",
    "რაზე გნებავთ საუბარი?",

])

# Beka's Stuff
trainer2.train([
    "ვინ შეგქმნა?",
    "მე შემქმნა ბექა ბიტარაშვილმა",
    "ვინ არის ბექა?",
    "ბექა არის QA ინჟინერი",
    "ვინ არის ბექა ბიტარაშვილი?",
    "ბექა QA ინჟინერი",

])

# Greeting Stuff
trainer3.train([
    "გამარჯობა",
    "მოგესალმებით",
    "გაუ",
    "ბარო",
    "როგორ ხარ?",
    "მე ვარ ხელოვნური ინტელექტი, ამიტომ არ გამაჩნია გრძნობები",
    "საიდან ხარ?",
    "საქართველოდან",
    "დამეხმარები?",
    "დიახ შევეცდები ყველა კითხვაზე გაგცეთ ამომწურავი პასუხი",
    "სალამი",
    "მოგესალმებით",
    "სად მუშაობ?",
    "არსად, უბრალოდ დამხმარე ჩათ-ბოტი ვარ",


])

# Extra Stuff About Crystal
trainer4.train([
    "რას მეტყვი კრისტალზე?",
    "კრისტალი არის ფინანსური ინსტიტუტი",
    "რა არის კრისტალი?",
    "კრისტალი არის ფინანსური ინსტიტუტი",
    "კრისტალი რას აკეთებს?",
    "კრისტალი ეწევა ფინანსურ საქმიანობას",
    "კრისტალი",
    "კრისტალი არის ფინანსური ინსტიტუტი",

])

# Employee Stuff
trainer4.train([
    "მათე",
    "მათე რომელი? სახელი და გვარი მომწერე და შეიძლება ვიცნობდე",
    "მათე ბუკია",
    "მათე არის QA სპეციალისტი(ჭადრაკსაც კარგად თამაშობს ამასთან ერთად)",
    "დათო",
    "მხოლოდ სახელით გამიჭირდება, სახელი გვარი მომწერე, რომ მივხვდე ვისზეა საუბარი",
    "დათო ბურკიაშვილი",
    "დათო არის QA სპეციალისტი",
    "ნატა",
    "სახელი და გვარი მომწერე სრულად",
    "ნატა გოიაშვილი",
    "ნატა არის QA განყოფილების ხელმძღვანელი",

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
