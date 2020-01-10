from classBot import *

Bot = classBot('Assistentde.db', mode_train=False)

while True:
    Quest = input('You: ')
    answer = Bot.procuraResposta(Quest)
    print(f'Bot: {answer}')
