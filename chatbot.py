from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import Terminal
# Create a chat bot called MegaBot
bot = ChatBot('MegaBot')

# Train the bot with some basic English
bot.set_trainer(ChatterBotCorpusTrainer)
bot.train('chatterbot.corpus.english')

# Let's give it a shot
res = bot.get_response('Good Morning!')
print (res)
# OUTPUT: I am doing well, how about you?


# Let's try something else
res = bot.get_response('Hello')
print (res)
# OUTPUT: Hi


# Another one
res = bot.get_response('Good Night!')
print (res)
# OUTPUT: I am doing well, how about you?