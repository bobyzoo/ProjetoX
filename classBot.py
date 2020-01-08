from conexaoBanco import *

class classBot(bancoDAO):

    def __init__(self, banco,mode_train = False):
        super().__init__(banco)
        self.mode_train = mode_train

    def procuraResposta(self, frase):
        escolhido = self.resposta(frase)
        print(escolhido[1])
        if escolhido[1] < 0.4:
            if self.mode_train == True:
                self.modoTrain(frase)
        else:
            sql = "SELECT rel.*,f.frase AS pergunta,f1.frase AS resposta FROM rel_per_res AS rel JOIN frases AS f ON rel.id_per = f.id JOIN frases AS f1 ON rel.id_res = f1.id WHERE pergunta = '{}'".format(
                escolhido[0])
            cursor = self.conn.cursor()
            cursor.execute(sql)
            respostas = []
            for linha in cursor.fetchall():
                respostas.append(linha[4])
            if len(respostas) > 0:
                return respostas[randint(0, len(respostas) - 1)]
            else:
                return 0

    def modoTrain(self, frase):
        escolhido = self.resposta(frase)

        if escolhido[1] < 0.8:
            print("Voc --------------{}".format(frase))
            print('Confiança baixa!\n -> Entendi:{}---{}'.format(escolhido[0], escolhido[1]))
            r = input('Deseja adicionar no banco esta nova frase? [S/N] ').strip().upper()
            if r == 'S':
                self.insertFrase(frase)
                self.insereResposta(frase)
                return 1
            else:
                if escolhido[1] == 0:
                    return 0
                else:
                    self.procuraRel(escolhido)

                r = input('Deseja incluir mais alguma resposta? [S/N]').strip().upper()
                if r == 'S':
                    self.insereResposta(frase)
                return 1

        self.procuraRel(frase)

        r = input('Deseja incluir mais alguma resposta? [S/N]').strip().upper()
        if r == 'S':
            self.insereResposta(frase)
        return 1

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
                conjuntoAtual = set(self.fraseChave(self.removeAcentuacao(self.removePontuacao(linha[1].upper()))))
                x = self.indexJacCard(conjuntoAtual, fraseVerdadeira)
                if (x > numJ):
                    numJ = x
                    frase = linha[1]
        return frase, numJ


    def resposta(self, frase):
        return self.maisProxima(frase)