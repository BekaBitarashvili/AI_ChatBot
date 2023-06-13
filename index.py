from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

bot = ChatBot("Gtech Chatbot", read_only=False,
              logic_adapters=[

                  {
                      "import_path": "chatterbot.logic.BestMatch",
                      "default_response": "I don't have an answer to this question yet :)",
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
    "office",
    "Tbilisi Gardens, 10 Mikheil Asatiani Street",
    "office location",
    "Tbilisi Gardens, 10 Mikheil Asatiani Street",
    "gtech office",
    "Tbilisi Gardens, 10 Mikheil Asatiani Street",
    "Gtech Services",
    "Graphic Design, QA Testing, Data, AI, UX/UI, Blockchain, Web Development",
    "Tell me about Gtech Team",
    "Gtech team is a group of people with the same vision and values. Things that matter in the company are shared: "
    "quality of work, advancing in learning, communications, and feedback from clients, reaching the deadlines, "
    "time management, responsibilities, positive vibes, and fun.",
    "Gtech Website",
    "You Can Visit: https://georgiatech.eu",
    "Gtech",
    "Georgia Tech Tbilisi, If You Want To Hear More Type: 'Tell me about Gtech Team'",
    "Website",
    "You Can Visit: https://georgiatech.eu",
    "website",
    "You Can Visit: https://georgiatech.eu",
    "How are you today?",
    "I'm doing well, thank you. How about you?",
    "What's the weather like today?",
    "I'm sorry, I don't have access to real-time information. Is there anything else I can help you with?",
    "What is your favorite color?",
    "As an AI, I don't have personal preferences. But I can appreciate all colors!",
    "Can you tell me a joke?",
    "Sure! Why don't scientists trust atoms? Because they make up everything!",
    "Where are you from?",
    "I'm an AI created by Gtech. I don't have a physical location, but I'm here to assist you with any questions you "
    "have.",
    "What's the meaning of life?",
    "The meaning of life can vary depending on one's beliefs and perspectives. It's a philosophical question that has "
    "intrigued humanity for centuries.",
    "What's your favorite movie?",
    "Since I don't have personal experiences, I don't have a favorite movie. Is there anything else I can assist you "
    "with?",
    "What time is it?",
    "What's the capital of Georgia?",
    "The capital of Georgia is Tbilisi.",
    "Are you a human?",
    "No, I'm an AI language model designed to assist with various tasks and provide information.",
    "How can I reset my password?",
    "To reset your password, you can go to the login page and click on the 'Forgot password' link. Follow the "
    "instructions to reset it.",
    "What's the latest news?",
    "I don't have access to real-time news updates. I recommend checking news websites or using a news app for the "
    "latest information.",
    "Where are you from?",
    "I'm an AI created by Gtech.",
    "Meaning of life?",
    "The meaning of life is subjective and varies for each individual.",
    "Favorite movie?",
    "As an AI, I don't have personal preferences.",
    "Current time?",
    "I'm sorry, I don't have access to real-time information.",
    "Human or AI?",
    "What's the tallest mountain?",
    "The tallest mountain is Mount Everest.",
    "What's the largest ocean?",
    "The largest ocean is the Pacific Ocean.",
    "Favorite book?",
    "As an AI, I don't have personal preferences for books.",
    "Best place to visit?",
    "The best place to visit depends on your interests and preferences.",
    "How to make a sandwich?",
    "To make a sandwich, choose your favorite bread, add your preferred fillings like meat, cheese, and vegetables, "
    "and assemble it to your liking.",
    "How to learn coding?",
    "To learn coding, you can start with online tutorials or coding courses. Practice regularly and work on small "
    "projects to reinforce your skills.",
    "What's the largest country?",
    "The largest country in the world by land area is Russia.",
    "How to create a strong password?",
    "To create a strong password, use a combination of uppercase and lowercase letters, numbers, and special "
    "characters. Avoid using personal information and common words.",
    "What's the speed of light?",
    "The speed of light in a vacuum is approximately 299,792 kilometers per second.",
    "Best way to save money?",
    "The best way to save money is to create a budget, track your expenses, cut back on non-essential spending, "
    "and consider automated savings options.",
    "Favorite board game?",
    "Monopoly.",
    "Favorite pizza?",
    "Peperoni",
    "Favorite movie genre?",
    "Comedy",
    "Cats or dogs?",
    "Dogs",
    "Favorite season?",
    "Fall",
    "Favorite sport?",
    "Football",
    "Favorite dessert?",
    "Chocolate cake.",
    "Favorite music genre?",
    "Rap",
    "Coffee or tea?"
    "Coffee",
    "Favorite book genre?",
    "Mystery.",
    "Favorite season of the year?",
    "Spring.",
    "Favorite hobby?",
    "Playing guitar.",
    "Favorite movie of all time?",
    "The Shawshank Redemption.",
    "Sweet or savory?",
    "Savory.",
    "Favorite superhero?",
    "Spider-Man.",
    "Favorite type of cuisine?",
    "Italian",
    "Gtech office",
    "Tbilisi Gardens, 10 Mikheil Asatiani Street",
    "Georgia Tech",
    "Gtech team is a group of people with the same vision and values. Things that matter in the company are shared: "
    "quality of work, advancing in learning, communications, and feedback from clients, reaching the deadlines, "
    "time management, responsibilities, positive vibes, and fun.",
    "Georgia Tech Tbilisi",
    "Gtech team is a group of people with the same vision and values. Things that matter in the company are shared: "
    "quality of work, advancing in learning, communications, and feedback from clients, reaching the deadlines, "
    "time management, responsibilities, positive vibes, and fun.",
    "Tell me Joke",
    "Did you hear the one about the mountain goats in the andes? It was 'ba a a a a a d'",
    "How was your weekend?",
    "It was great! I spent time with family and enjoyed some outdoor activities.",
    "What's your plan for lunch today?",
    "Glovo or Wolt :)",
    "Favorite tech gadget?",
    "Mac",
    "What's your go-to coding language?",
    "Python",
    "Favorite social media platform?",
    "Facebook, Instagram and Twitter",

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
    "Nika Kalandadze",
    "Nika is a Front Dev at Gtech",
    "Irakli Chelidze",
    "Irakli is a Product Owner",
    "Giorgi Metonidze",
    "Giorgi is a Back Dev at Gtech",
    "Beka Bitarashvili",
    "Beka is a QA Engineer",
    "Lega",
    "Lega is an UX/UI Designer",
    "tamu robinson",
    "Be careful my friend :) Ask me Something else...",
    "tamu",
    "Be careful my friend :) Ask me Something else...",
    "Tamu",
    "Be careful my friend :) Ask me Something else...",
    "Tamu Robinson",
    "Be careful my friend :) Ask me Something else...",
    "Ada",
    "Ada is an ENG Teacher at Gtech :)",
    "Ada Gogilava",
    "Ada is an ENG Teacher at Gtech :)",
    "Avto",
    "Avto is a QA Lead at Gtech, He also supports Barca ;)",
    "Avto Gachechiladze",
    "Avto is a QA Lead at Gtech, He also supports Barca ;)",
    "Avtandil Gachechiladze",
    "Avto is a QA Lead at Gtech, He also supports Barca ;)",
    "Mariam Bokeria",
    "Mariam is a QA at Gtech",
    "Nino Khaburdzania",
    "Nino is a Business Manager at Gtech",
    "Mariam Bokeria",
    "Mariam is a QA Engineer at Gtech",
    "Beka Ubiria",
    "Beka is a QA Engineer at Gtech",
    "Anna Jakeli",
    "Anna is a QA Engineer at Gtech",
    "Pascal",
    "CEO",
    "Pascal Lauffer",
    "CEO",

])

# Extra Stuff About Gtech
trainer4.train([
    "Thursday",
    "Pizza Day at Gtech!",
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
