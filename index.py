from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


bot = ChatBot("GeorgianAIChatbot", read_only=False, logic_adapters=["chatterbot.logic.BestMatch"])

list_to_train = [
                "გამარჯობა",
                "მოგესალმებით...",
                "რა გქვია?",
                "ჩემი სახელია ჩათ-ბოტი",
                "რამდენი წლის ხარ?",
                "მე ასაკი არ მაქვს",
                "რა გინდა?",
                "ჩემი მიზანია დავეხმარო ადამიანებს და ვუპასუხო მათ ყველა შეკითხვას"

]

list_trainer = ListTrainer(bot)

list_trainer.train(list_to_train)
while True:
    user_response = input("მომხმარებელი: ")
    print("ჩათ-ბოტი: " + str(bot.get_response(user_response)))
