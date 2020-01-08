import sqlite3
from random import *

class bancoDAO():

    def __init__(self, banco):
        self.conn = sqlite3.connect(banco)

    def selectAll(self, tabela):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM {} ".format(tabela))
        for linha in cursor.fetchall():
            print(linha)

    def insertFrase(self, frase):
        cursor = self.conn.cursor()
        if frase.find('\r\n') >= 1:
            frase = frase[:frase.find('\r\n')]
        sql = "INSERT INTO frases (frase) values('{}')".format(self.removeAcentuacao(frase.upper()))

        try:
            cursor.execute(sql)
            self.conn.commit()
            print('Inserido com sucesso!')
        except:
            print('Erro ao inserir no banco!')

    def resposta(self, frase):
        return self.maisProxima(frase)

    def maisProxima(self, frase):
        '''
        Função tras a frase mais proxima existente no banco
        :param frase:
        :return fraseMaisProxima,indiceDeConfiabilidade:
        '''

        # remove Acentuação,pontuação. returna um set com palavas chaves
        fraseVerdadeira = set(self.fraseChave(self.removeAcentuacao(self.removePontuacao(frase.upper()))))

        frase = ''
        numJ = 0

        for key in fraseVerdadeira:

            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM frases WHERE frase LIKE '%{}%';".format(key))
            for linha in cursor.fetchall():
                # print(linha,end='->')
                conjuntoAtual = set(self.fraseChave(self.removeAcentuacao(self.removePontuacao(linha[1].upper()))))
                # print(conjuntoAtual,'-',fraseVerdadeira,end='->')
                x = self.indexJacCard(conjuntoAtual, fraseVerdadeira)
                # print(x)
                if (x > numJ):
                    numJ = x
                    frase = linha[1]
        print(frase)
        return frase, numJ

    def fraseChave(self, frase):
        '''
        função retorna somente as palavras chaves da frase
        
        :param frase: 
        :return fraseFinal: 
        '''
        fraseFinal = frase.split()
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM rel_class_word where id_class=2")
        for linha in cursor.fetchall():
            if linha[1] in fraseFinal:
                fraseFinal.remove(linha[1])
        return fraseFinal

    def removePontuacao(self, frase):
        '''
        Função remove todos tipos de pontuação ". , ? ! ( )"

        :param frase:
        :return frase:
        '''
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM rel_class_word where id_class=3")
        for linha in cursor.fetchall():
            while linha[1] in frase:
                frase = frase.replace(linha[1], ' ')
        return frase

    def indexJacCard(self, conjuntoA, conjuntoB):
        '''
        Função retorna o indice de quão confiavel uma item A esta com item B
        
        0.0-1.0
        
        :param conjuntoA: 
        :param conjuntoB: 
        :return: 
        '''
        return (len(conjuntoA & conjuntoB)) / (len(conjuntoA | conjuntoB))

    def removeAcentuacao(self, frase):
        '''
               Função remove todos tipos de acentuação em letra

               :param frase:
               :return frase:
               '''
        frase = frase.upper()
        cursor = self.conn.cursor()

        cursor.execute(
            "select * from rel_class_word join letras_acentuadas on letras_acentuadas.id_letra = rel_class_word.id")
        for linha in cursor.fetchall():
            while linha[1] in frase:
                frase = frase.replace(linha[1], linha[5])
        return frase


    def procuraRel(self, frase):
        sql = "SELECT rel.*,f.frase as pergunta,f1.frase as resposta FROM rel_per_res as rel JOIN frases as f ON rel.id_per = f.id JOIN frases as f1 ON rel.id_res = f1.id where rel.id_per={}".format(self.idFrase(frase))
        cursor = self.conn.cursor()
        cursor.execute(sql)
        print(6 * '-', end='')
        print('RELAÇÕES', end='')
        print(6 * '-')
        print('Pergunta X Resposta')
        for linha in cursor.fetchall():
            print(linha[3],'X',linha[4])
        print(20 * '-')

    def insereRelPerResId(self, id_per, id_res):
        ids = str(id_res).split()
        for id in ids:
            sql = "INSERT INTO rel_per_res (id_per,id_res) values({},{})".format(id_per, int(id))
            cursor = self.conn.cursor()
            try:
                cursor.execute(sql)
                self.conn.commit()
                print('Inserido com sucesso!')
            except:
                print('Erro ao inserir no banco!')

    def idFrase(self, frase):
        cursor = self.conn.cursor()
        if frase.find('\r\n') >= 1:
            frase = frase[:frase.find('\r\n')]
        cursor.execute("SELECT * FROM frases WHERE frase='{}' ".format(self.removeAcentuacao(frase.upper())))
        for linha in cursor.fetchall():
            return linha[0]

    def insereResposta(self, frase):
        print('Adicione uma resposta a frase inserida: ')
        self.selectAll('frases')
        r = input('A resposta esta na lista a cima? [S/N]').upper().strip()
        if r == 'S':
            self.insereRelPerResId(self.idFrase(frase), (input('Quais os IDs? [1 2 3 4 5]')))
            r=input('Deseja adicionar uma resposta não existente? [S/N]').strip().upper()
            if r=='S':
                resposta = input('Digite a resposta: ')
                self.insertFrase(resposta)
                self.insereRelPerResId(self.idFrase(frase), self.idFrase(resposta))
            else:
                return 1
        else:
            r = input('Deseja adicionar uma resposta não existente? [S/N]').strip().upper()
            if r == 'S':
                resposta = input('Digite a resposta: ')
                self.insertFrase(resposta)
                self.insereRelPerResId(self.idFrase(frase), self.idFrase(resposta))
        return 1

        def close(self):
            return self.conn.close()