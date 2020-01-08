from classBot import *

Bot = classBot('Assistente.db', mode_train=True)

while True:
    Quest = input('You: ')
    answer = Bot.procuraResposta(Quest)
    print(f'Bot: {answer}')
