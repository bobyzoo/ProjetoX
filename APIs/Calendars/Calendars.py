from datetime import datetime


class Calendar():
    def __init__(self):
        self.now = datetime.now()
        self.Holiday = {'AnoNovo': '01-01', 'Carnaval': '04-03', 'Paixao': '19-04', 'Tiradentes': '21-04',
                        'Trabalho': '01-05', 'CorpusChristi': '20-06', 'Independencia': '07-09',
                        'NossaSenhora': '12-10', 'Finados': '02-11', 'Proclamacao': '15-11', 'Natal': '25-12'}

    def setNow(self):
        self.now = datetime.now()

    def getNow(self):
        return self.now

    def getHour(self):
        return self.now.hour

    def getMin(self):
        return self.now.min

    def getDate(self):
        return str(self.now.strftime("%d-%m"))

    def getNextHoliday(self):
        dataAtual = '26-12'
        for festa in self.Holiday.values():
            if dataAtual[3:] == festa[3:] and int(dataAtual[:2]) < int(festa[:2]):
                return festa
            elif int(dataAtual[3:]) < int(festa[3:]):
                return festa

        return self.Holiday['AnoNovo']

    def isHoliday(self):
        return 0
