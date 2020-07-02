import sqlite3


class DataBase:

    def __init__(self, banco):
        self.conn = sqlite3.connect(banco)

    def select(self, tabela,filter = ''):
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

    def insert_actions(self, command):
        cursor = self.conn.cursor()
        sql = f"INSERT INTO list_actions (description) values ('{command}')"
        cursor.execute(sql)
        self.conn.commit()
        print('Inserido com sucesso!')

    def insert_new_call_command(self, command,id_action):
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

    def search_by_token_in_commands(self,key):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM list_commands WHERE command LIKE '%{key}%';")
        return cursor.fetchall()
