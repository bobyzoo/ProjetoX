from requests import get
from bs4 import BeautifulSoup

class Notices:
    @staticmethod
    def lastNotices():
        site = get('https://news.google.com/rss?hl=pt-BR&gl=BR&ceid=BR:pt-419')
        notices=[]
        siteNotice = BeautifulSoup(site.text, 'html.parser')
        for item in siteNotice.find_all('item')[:3]:
            notices.append(item.title.text)
        return notices


