import requests
import pandas as pd
from bs4 import BeautifulSoup

req = requests.get('https://sites.google.com/site/thesaurusdalinguaportuguesa/home')
if req.status_code == 200:
    print('Requisição bem sucedida!')
    content = req.content

soup = BeautifulSoup(content, 'html.parser')

list = soup.findAll(name='a', attrs={'class': 'sites-navigation-link'})
print(type(str(list).split(',')))
listPages = []
for i in list:
    i = str(i)
    i = i.replace('<a class="sites-navigation-link" href="', '')
    i = i.replace(i[i.index('"'):], '')
    nm = i.replace("/site/thesaurusdalinguaportuguesa/", '')
    if len(nm) > 2 and nm.isalpha():
        listPages.append(i)

for i in listPages:
    print(i)
    print('-------------+')
    contexto = i.replace('/site/thesaurusdalinguaportuguesa/', '')
    req = requests.get('https://sites.google.com' + i)
    if req.status_code == 200:
        print('Requisição bem sucedida!')
        content = req.content

    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find(name='table', attrs={'class': 'sites-layout-name-one-column sites-layout-hbox'})
    table_str = str(table)
    print(table)
    df = pd.read_html(table_str)[0]
    print(df)
    print(50 * '-')
    df.columns = ['nome', 'palavras']
    df.drop([0, 1])
    for t in df['palavras']:
        print(t)
    break
