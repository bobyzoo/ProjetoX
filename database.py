import sqlite3


class DataBase:

    def __init__(self, banco):
        self.conn = sqlite3.connect(banco)
        self.last_id = 0

    def select(self, tabela, filter=''):
        cursor = self.conn.cursor()
        if filter != '':
            filter = f'WHERE {filter}'
        cursor.execute(f"SELECT * FROM {tabela} {filter}")
        print('-' * 50)
        for line in cursor.fetchall():
            for item in line:
                print('|', end='')
                print(item, end='')
            print('|', end='')
            print(' ')
            print('-' * 50)

    def selectTable(self, tabela, filter=''):
        cursor = self.conn.cursor()
        if filter != '':
            filter = f'WHERE {filter}'
        cursor.execute(f"SELECT * FROM {tabela} {filter}")
        table = []
        for line in cursor.fetchall():
            table.append(line)
        return table

    def getIDPhrase(self,phrase):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM phrases WHERE sentence = '{phrase}' ")
        print(f"SELECT * FROM phrases WHERE sentence = '{phrase}'")
        if len(cursor.fetchall()) > 0:
            print(cursor.fetchall())
            return cursor.fetchone()
        return False
    def getLastId(self):
        return self.last_id
    def insert_actions(self, command):
        cursor = self.conn.cursor()
        sql = f"INSERT INTO list_actions (description) values ('{command}')"
        cursor.execute(sql)
        self.conn.commit()
        print('Inserido com sucesso!')

    def insert_new_phrase(self, command, id_context=0):
        cursor = self.conn.cursor()
        sql = f"INSERT INTO phrases (sentence,id_contexts) values ('{command}',{id_context})"
        cursor.execute(sql)
        self.conn.commit()
        self.last_id = cursor.lastrowid
        print('Inserido frase com sucesso!')

    def verify_phrase(self, phrase):
        cursor = self.conn.cursor()
        sql = f"SELECT * FROM phrases WHERE sentence = '{phrase}'"
        cursor.execute(sql)
        if len(cursor.fetchall()) > 0:
            print('Existe a frase')
            return True
        print('nao existe a frase')
        return False

    def verify_phrase_conn(self, phrase1, phrase2):
        cursor = self.conn.cursor()
        sql = f"SELECT * FROM answer_for_quest WHERE id_quest = '{phrase1}' and id_answer = '{phrase2}'"
        print(sql)
        cursor.execute(sql)
        if len(cursor.fetchall()) > 0:
            return True
        return False

    def insert_phrase_conn(self, phrase1, phrase2):
        cursor = self.conn.cursor()
        print(phrase1)
        print(phrase2)
        sql = f"INSERT INTO answer_for_quest (id_quest,id_answer) values ('{phrase1}',{phrase2})"
        print(sql)
        cursor.execute(sql)
        self.conn.commit()
        print('Inserido conexao sucesso!')

    def insert_new_call_command(self, command, id_action):
        cursor = self.conn.cursor()
        sql = f"INSERT INTO list_commands (command,id_action) values ('{command}',{id_action})"
        cursor.execute(sql)
        self.conn.commit()
        print('Inserido com sucesso!')

    def select_lycris_accentuation(self):
        """
        Função retorna letras acentuadas
        """
        cursor = self.conn.cursor()
        cursor.execute(
            "select * from rel_class_word join letras_acentuadas on letras_acentuadas.id_letra = rel_class_word.id")
        return cursor.fetchall()

    def stop_words(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM rel_class_word where id_class=2")
        return cursor.fetchall()

    def lycris_accentuation(self):
        """
        Função retorna letras acentuadas
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM rel_class_word where id_class=3")
        return cursor.fetchall()

    def search_by_token_in_commands(self, key):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM list_commands WHERE command LIKE '%{key}%';")
        return cursor.fetchall()

    def search_by_response_in_contexts(self, key):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM phrases WHERE sentence LIKE '%{key}%';")
        return cursor.fetchall()
