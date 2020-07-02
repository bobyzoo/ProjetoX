from database import *
import spacy


class MainBrain(object):
    def __init__(self) -> None:
        super().__init__()
        self.nlp = spacy.load('pt_core_news_lg')
        self.db = DataBase("Assistente.db")
        self.train_mode = False

    def brain(self, command):
        command = self.format_command(command)
        command = self.key_words(command)
        return command

    def format_command(self, command):
        if "\r\n" in command:
            command = command[:command.find('\r\n')]
        final = ''
        doc = self.nlp(command)
        for token in doc:
            if not self.nlp.vocab[token.text].is_punct:
                final = final + str(token.text)
                final += ' '

        return final

    @staticmethod
    def index_jac_card(setA, setB):
        '''
        Function return how confiability set A for set B
                                                        0.0-1.0
        :param setA:
        :param setB:
        '''
        # print(setA,setB,(len(setA & setB)) / (len(setA | setB)))
        return (len(setA & setB)) / (len(setA | setB))

    def key_words(self, command):
        if "\r\n" in command:
            command = command[:command.find('\r\n')]
        final = ''
        doc = self.nlp(command)
        for token in doc:
            if not self.nlp.vocab[token.text].is_stop:
                final = final + str(token.text)
                final += ' '

        return final

    def search_response(self, context, command):
        command_compleate = set(context.split())
        response = ''
        numJ = 0
        id_action = 0
        for key in context.split():
            for line in self.db.search_by_token_in_commands(key):
                command_found = set(self.brain(line[1]).split())
                indexFinal = self.index_jac_card(command_compleate, command_found) + self.index_jac_card(
                    set(command.split()), set(line[1].split())) + self.similarity_index(command, line[1])
                if indexFinal > numJ:
                    numJ = indexFinal
                    id_action = line[2]
                    response = line[1]
        print(numJ)
        return response, id_action, numJ

    def similarity_index(self, p1, p2):
        return self.nlp(p1).similarity(self.nlp(p2))

    # Area Train
    def train_session(self):
        while 1:
            r = input("Você desejar treinar com audio[1] ou por texto[2]? ")

            if r == '1':
                pass
            elif r == '2':
                while 1:
                    if self.train_by_text() == 0:
                        break

    def learn_new_command(self, command: object) -> object:
        self.db.insert_actions(command)

    def learn_new_call_command(self, command, id_action):
        self.db.insert_new_call_command(self.format_command(command), id_action)

    def train_by_text(self):
        self.db.select('list_actions')
        r = input('Novo comando[1] ou existente[2]: ')
        if r == '1':
            while 1:
                command = input("Digite a descrição do novo comando, ou '0' para sair: ")
                if command == '0':
                    return 0
                self.learn_new_command(command)

        elif r == '2':

            while 1:
                id = input('Digite o ID da ação que desejas adicionar um comando de voz: ')
                filter = 'id_action == ' + id
                self.db.select('list_commands', filter)
                command = input("Digite o comando de voz que desejas, ou '0' para sair: ")
                if command == '0':
                    return 0
                self.learn_new_call_command(command, id)
