import json
import re
import requests
import orodja


glavni_vzorec = re.compile(
    r'<meta name=\"title\" content=\"(?P<ime>.+?)\">.+?'
    r'{\"gameid\":\[\"(?P<id>.+?)\"\],.+?'
    r'\"yearpublished\":\"(?P<leto>\d+?)\",'
    r'\"minplayers\":\"(?P<minplay>\d+?)\",'
    r'\"maxplayers\":\"(?P<maxplay>\d+?)\",'
    r'\"minplaytime\":\"(?P<mintime>\d+?)\",'
    r'\"maxplaytime\":\"(?P<maxtime>\d+?)\",'
    r'\"minage\":\"(?P<minage>\d+?)\".+?'
    r'\"ratingValue\": \"(?P<ocena>.+?)\".+?'
    r'\"reviewCount\": \"(?P<glasovi>\d+?)\"',
    flags=re.DOTALL
)

kategorije_blok = re.compile(
    r'\"boardgamecategory\":\[(.+?)\].+?',
    flags=re.DOTALL
)

mechanic_blok = re.compile(
    r'\"boardgamemechanic\":\[(.+?)\].+?',
    flags=re.DOTALL
)

km_vzorec = re.compile(
    r'\"name\":\"(.+?)\"',
    flags=re.DOTALL
)

'''
problemi = []
for i in range(1,100):
    print(i)
    try:
        with open("igra_{}.html".format(i), encoding='utf-8') as dat:
            stran = dat.read()
        print(glavni_vzorec.search(stran).groupdict())
        print(re.findall(km_vzorec, re.findall(kategorije_blok, stran)[0]))
        print(re.findall(km_vzorec,re.findall(mechanic_blok, stran)[0]))
    except:
        print("Napaka")
        problemi.append(i)

print(problemi)
'''

podatki = []
for i in range(1,501):
    try:
        with open("igra_{}.html".format(i), encoding='utf-8') as dat:
            stran = dat.read()
        slovar = glavni_vzorec.search(stran).groupdict()
        slovar['kategorije'] = re.findall(km_vzorec, re.findall(kategorije_blok, stran)[0])
        slovar['mechanic'] = re.findall(km_vzorec,re.findall(mechanic_blok, stran)[0])
        podatki.append(slovar)
    except:
        print("Napaka pri primeru {}".format(i))

orodja.zapisi_csv(podatki, ['ime', 'id', 'leto', 'minplay', 'maxplay', 'mintime', 'maxtime', 'minage', 'ocena', 'glasovi', 'kategorije', 'mechanic'], "test.csv")